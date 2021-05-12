# Assignment2
In this assignment, i recurrent the research papar 《Volatility and turnover rate construct bull and bear indicators 》 of Huatai Securities。  
The reason I chose this article to reproduce is that in the stock market, judging the type of market is especially important.   
Different types of factors have huge differences in performance in different market styles.   
For example, in a bull market, the entire market is pulling up, and each stock rotates upwards, and the effects of reversal factors and momentum factors will be better;  
while in a bear market, the effects of reversal factors will be unsatisfactory ,and at the meantime, stocks with high dividends and low volatility may have good defensive  
functions. 
And of course, this is not absolute.   
The basis of the whole article is based on the use of volatility and turnover rate as the basis for constructing bull and bear market indicators.  
The first step is the selection of data, which is different from the original text. I selected the closing price and turnover rate of each broad-based index from 2010-01 to 2020-11-13. During the period, there were several bull and bear markets, including 14 15 The big bull market and the big bear market of the year, at the same time, this data will be closer to the current than the article.  
In the second step, first analyze the volatility and turnover rate directly.  
The definition of volatility is the standard deviation of the rate of return of the past n trading days.  
The rate of return can be calculated using the closing price, and then rolling is used to calculate the standard deviation to get the volatility.  
First compare the volatility of different rolling times and we can get the following figure:  
![image](https://user-images.githubusercontent.com/78793744/117833079-9e004600-b2a8-11eb-8148-64698d26fc5d.png)
Next is an image of the 250-day volatility and the Shanghai Composite Index 
![image](https://user-images.githubusercontent.com/78793744/117836149-05b79080-b2ab-11eb-9257-10b75adafad8.png)
Combining experience with the above figure, it can be found that in a rapidly rising or falling bull and bear market, the volatility starts when the bull market starts, and will continue to rise at the beginning of the bear market until the end of the bear market.   
This is because the change of the price rising in the bull market, and when the stock market reaches the top, the willing of selling stocks will be more intense, which will increase the changing speed of and the price of stock market.    
This rule gives a potential method to judge the transition or end of a bull market and a bear market.   
In a slow down bear market, volatility does not follow the above-mentioned law. 
Now let’s look at the turnover rate  
The figure below shows the turnover rate of different parameters  
![image](https://user-images.githubusercontent.com/78793744/117977010-f72cb000-b362-11eb-9c88-c7af13563064.png)  
Next is the 250-day turnover rate and the Shanghai Composite Index  
![image](https://user-images.githubusercontent.com/78793744/117977025-fdbb2780-b362-11eb-9e07-0c68bd1398ed.png)  
It can be found that the turnover rate and the Shanghai Composite Index are positively correlated, which has the potential to judge the bull and bear market   
Now let's build the bull and bear indicator  
First of all, we must first clarify the turnover rate and volatility corresponding to each market situation.  
In a bull market, the volatility will rise, and the turnover rate will also rise;  
In a bear market, the volatility will increase and the turnover rate will decrease;  
When the volatility falls and the turnover rate rises, the market appears to be an upward trend;  
When the volatility decreases and the turnover rate decreases, it appears as a shocking market.   
Use volatility divided by turnover rate as a bull and bear indicator   
The advantage of this is that it can better characterize the above four situations, especially the bear market, which can be well captured by the bull and bear indicators to avoid risks.    
Found that the bull and bear market indicators have an inverse relationship with stock indexes.   
上证指数	上证50	沪深300	中证500	万得全A
-0.446322393	-0.303634254	-0.418759558	-0.432993728	-0.405640939
However, in this backtest period, the correlation between the bull and bear indicators and the stock index is not as good as the -0.6 in the article, so the backtest results later are not as good as the article.   
The final return of 上证指数、上证50、沪深300、中证500、万得全A is   
上证指数最终收益:0.7838098381243166  
上证50最终收益:0.7534795112057018  
沪深300最终收益:1.0818006998845  
中证500最终收益:1.4935436172486223  
万得全A最终收益:1.9018456135226227  
according to the Backtest() function in Strategy_BullBear.py   
The net value curve is:   
![image](https://user-images.githubusercontent.com/78793744/117985904-b7b69180-b36b-11eb-894d-1ce16d3af80e.png)   
![image](https://user-images.githubusercontent.com/78793744/117987052-be91d400-b36c-11eb-9be4-c24e12cfb670.png)  
![image](https://user-images.githubusercontent.com/78793744/117987455-129cb880-b36d-11eb-9ca4-803dee81270f.png)  
![image](https://user-images.githubusercontent.com/78793744/117987625-3c55df80-b36d-11eb-9575-120e31b654ec.png)  
![image](https://user-images.githubusercontent.com/78793744/117987793-67d8ca00-b36d-11eb-8e0c-410f140e4ffa.png)  
It can be found that the advantage of this factor is that when the stock index falls sharply, the strategy can play the effect of stopping the loss one step ahead of the index.    
The disadvantage is that it cannot stop the loss when the sharp fall occurs.    
This may be because of the use of the 250-day bull and bear Indicators, leading to a certain degree of lag.   

The pictures are plot by excel, which name is 画图.xlsx
The main python program is StrategyBullBear.py  









