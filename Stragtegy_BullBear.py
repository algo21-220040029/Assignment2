from backtest import *

# 数据基类
class Data():
    def __init__(self, path):
        # 导入基础数据
        self.close = pd.read_csv(path + "qfq/close_of_all_stocks.csv",
                                 index_col=0)
        self.pct_chg = pd.read_csv(path + "qfq/pctChg_of_all_stocks.csv",
                                  index_col=0)
        self.tradestatus = pd.read_csv(path + "qfq/tradestatus_of_all_stocks.csv",
                                  index_col=0)
        self.isST = pd.read_csv(path + "qfq/isST_of_all_stocks.csv",
                                  index_col=0)



# 策略基类
class Strategy():

    # 用构造因子需要的数据初始化
    def __init__(self, data):
        self.data = data

    # 一些工具函数

    #
    def rank(self, frame):
        return frame.rank(axis=1, method='first', pct=True)
        # return frame.rank(axis=1, method='first')
        # return frame.rank(axis=1,ascending=False,method='first')

    # 将数据下移一个日期
    def delay(self, frame, days):
        return frame.shift(days)

    # 求两个dataframe的相关系数
    def correlation(self, frame1, frame2, days):
        # dataframe的apply函数就是对所有元素进行同一种函数操作的意思
        # frame1.apply(lambda x:x.astype(float))
        # frame2.apply(lambda x:x.astype(float))
        # print(frame1.info())
        # print(frame2.info())
        return frame1.rolling(days).corr(frame2)

    # 求两个dataframe的协方差
    def covariance(self, frame1, frame2, days):
        return frame1.rolling(days).cov(frame2)

    # 这个函数是针对整体的,这里的a不表示天数，而是表示整体放缩至的大小
    def scale(self, frame, a=1):
        return frame.mul(a).div(np.abs(frame).sum())

    # 计算dataframe在时间上的差值
    def delta(self, frame, days):
        return frame.diff(days)

    def decay_linear(self, frame, days):
        return frame.rolling(days).apply(self.decay_linear_apply)

    def decay_linear_apply(self, slice):
        # print(slice)
        # 加1是为了之后创建list
        days = len(slice) + 1
        # print(days)
        weight = np.arange(1, days, 1)
        weight = weight / weight.sum()
        return (slice * weight).sum()

    # 计算在时间上的最小值
    def ts_min(self, frame, days):
        return frame.rolling(days).min()

    # 计算在时间上的最大值
    def ts_max(frame, days):
        return frame.rolling(days).max()

    # 计算在时间上的排名（从小到大）
    def ts_argmin(self, frame, days):
        return frame.rolling(days).apply(np.argmin)

    # 计算在时间上的排名（从大到小）
    def ts_argmax(self, frame, days):
        return frame.rolling(days).apply(np.argmax)

    def ts_rank(self, frame, days):
        return frame.rolling(days).apply(self.ts_rank_apply)

    def ts_rank_apply(self, slice):
        return list(slice.argsort()).index(4)

    def sum(self, frame, days):
        return frame.rolling(days).sum()

    # 累乘
    def product(self, frame, days):
        return frame.rolling(days).apply(np.prod)

    # 标准差
    def stddev(self, frame, days):
        return frame.rolling(days).std()

    # 几日均值
    def sma(self, frame, days):
        return frame.rolling(days).mean()


    # 这里可以定义一个专门的实现具体策略的函数或者factor，然后创建新策略的时候就直接继承Stragey然后
    # 实现具体的因子函数就好
    def factor(self):
        pass


class simple_Strategy(Strategy):
    def factor(self):
        # pct_Chg = self.data.pct_chg
        # close = self.data.close
        volume = self.data.volume
        return self.rank(volume)

class BB_Data():
    def __init__(self, path):
        self.turn = pd.read_excel(path + "BullBear/换手率.xlsx", index_col=0)
        self.indexes = pd.read_excel(path+"BullBear/牛熊指标择时指数.xlsx", index_col=0)

data = BB_Data(path="F:/Python/BacktestSystem/")

class BB_Strategy(Strategy):
    def volatility(self, n):
        indexes_pct_change = self.data.indexes.pct_change()
        (indexes_pct_change.rolling(window=n).std()).to_csv("BullBear/" + str(n)+"日波动率.csv", encoding="utf_8_sig")
        return indexes_pct_change.rolling(window=n).std()

    def turnover_mean(self, n):
        (self.data.turn.rolling(window=n).mean()).to_csv("BullBear/" + str(n)+"日换手率.csv", encoding="utf_8_sig")
        return self.data.turn.rolling(window=n).mean()

    # 默认牛熊指标波动率和换手率都用250日
    def BullBear_indicator(self, n = 250):
        ((self.volatility(n).dropna()) / (self.turnover_mean(n).dropna())).to_csv("BullBear/"+str(n)+"日牛熊指标.csv", encoding="utf_8_sig")
        return (self.volatility(n).dropna())/(self.turnover_mean(n).dropna())

    def BullBear_factor(self, s=20, l=60):
        BB_indicator = self.BullBear_indicator()
        # 构建短均线
        short_avg = BB_indicator.rolling(s).mean()
        # 构建长均线
        long_avg = BB_indicator.rolling(l).mean()
        long_index = long_avg.index
        short_avg = short_avg.loc[long_index]
        # 之所以是小于号是因为牛熊指标越小越好
        return (short_avg < long_avg).astype("int")


def backtest():
    factor = BullBear.BullBear_factor()
    factor.to_csv("BullBear/" + "牛熊因子.csv", encoding="utf_8_sig")
    factor_index = factor.index

    pct_chg = (data.indexes.pct_change()).loc[factor_index]

    #
    for asset_name, asset_factor in factor.iteritems():
        asset_pct_chg = pct_chg[asset_name]
        # 指数的持仓每期收益向量
        asset_net_value_single = asset_factor.shift(1) * (1 + asset_pct_chg)
        asset_net_value_single.iloc[0] = 1
        # 现金的持仓每期收益向量
        cash_net_value_single = (1 - asset_factor).shift(1)
        cash_net_value_single.iloc[0] = 0
        total_net_value_single = asset_net_value_single + cash_net_value_single
        total_net_value = total_net_value_single.cumprod()
        total_net_value.to_csv("BullBear/" + asset_name + "test.csv", encoding="utf_8_sig")
        total_return = total_net_value.iloc[-1] - 1
        print(asset_name + "最终收益:" + str(total_return))

# 生成各参数的波动率和换手率
BullBear = BB_Strategy(data=data)
params = [60, 120, 200, 250]
for p in params:
    # BullBear.volatility(p)
    # BullBear.turnover_mean(p)
    pass

# print(BullBear.BullBear_factor())
backtest()








