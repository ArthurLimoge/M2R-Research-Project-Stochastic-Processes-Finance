# M2R-Project

Project done under the supervision of [Dr. Andreas Sojmark](https://www.imperial.ac.uk/people/a.sojmark). It aims to use physical models such as particle diffusion and geometric Brownian motion to understand stochastic processes such as stock markets. It then delves into part of the theory for stochastic calculus to explain the intuition behind it.

:large_blue_diamond: 0_M2R_Report.pdf: final report of the project

### Contributions:


• Arthur Limoge: implementation of the variance ratio test in R (3.1.3), theoretical motivation and intuition for Itô Calculus (section 3.2)

• Munazza Sarwar: derivation of the Black-Scholes equation from a binomial model (section 2.1)

• Timothy Minn Kang: solving of the Black-Scholes and study of the heat equation (section 3.2), and solution curves and error analysis simulations in Python (3.1.1, 3.1.2)

• Yongda Zhu: construction of models to understand discrete random walks (section 1.1)

• Zhuohan Yang: generalization of the latter models to continuous cases (section 1.2)


## Programs: 

:large_blue_diamond: Market_study.py: 

:large_blue_diamond: Variance_Ratio_test.Rmd: program testing weak-form market efficiency by using the Lo & MacKinley variance ratio test

## Datasets:

#### :large_orange_diamond: Daily data sets

• Dataset1.csv -> Apple stock shares from 03/06/2019 to 02/06/2020 - source: https://yhoo.it/2Br0rQh

• Dataset2.csv -> Activision-Blizzard stocks from 08/02/2013 to 07/02/2018 - source: https://bit.ly/3gRZFfl

• Dataset3.csv ->  General motors stocks from 04/06/2019 to 03/06/2020 - source: https://finance.yahoo.com/quote/gm/history?ltr=1

• Dataset4.csv -> McDonald's stocks from 08/02/2013 to 07/02/2018 source - https://bit.ly/3gRZFfl

• Dataset5.csv -> Netflix stocks from 08/02/2013 to 07/02/2018 source - https://bit.ly/3gRZFfl

• Dataset7.csv -> Goldman Sachs stocks from 04/06/2019 to 04/06/2020 source https://finance.yahoo.com/quote/GS/history


#### :large_orange_diamond: High frequency datasets

• Dataset6.csv -> S&P500 high frequency stock prices (1/min) from 17/11/2015 - source: https://www.quandl.com/databases/AS500/data


#### Code/Files used in Subsections 3.1.1 and 3.1.2
• DB.csv ->  Deutsche Bank stock prices (per day) from 12/06/2019 to 12/06/2020 -source:
https://finance.yahoo.com/quote/DB/history?p=DB

• Final_DB_results.csv ->  Deutsche Bank stock prices (at close of trading), times between 26/05/2020 and 12/06/2020 inclusive, call option prices - source:
https://bigcharts.marketwatch.com/quickchart/quickchart.asp?symb=DB%23F1920E950000&insttype=&freq=1&show=&time=4 (call option prices)
(time and stock prices obtained from DB.csv)

• Black-Scholes Difference Plotter Deutsche Bank

• Code for Figures 1 and 2

