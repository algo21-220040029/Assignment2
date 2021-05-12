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
First of all, we must first clarify the turnover rate and volatility corresponding to each market situation  
In a bull market, the volatility will rise, and the turnover rate will also rise;  
In a bear market, the volatility will increase and the turnover rate will decrease;  
When the volatility falls and the turnover rate rises, the market appears to be an upward trend;  
When the volatility decreases and the turnover rate decreases, it appears as a shocking market.  
Use volatility divided by turnover rate as a bull and bear indicator  
The advantage of this is that it can better characterize the above four situations, especially the bear market, which can be well captured by the bull and bear indicators to avoid risks.   
