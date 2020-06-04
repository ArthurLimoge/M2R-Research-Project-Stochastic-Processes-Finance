"""
Website used as reference for the code
https://towardsdatascience.com/simulating-stock-prices-in-python-using-geometric-brownian-motion-8dfd6e8c6b18
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# open the file in read mode
# file = pd.read_csv('Dataset1.csv')  # Data used: apple shares (03/06/2019 to 02/06/2020) - https://yhoo.it/2Br0rQh
file = pd.read_csv('Dataset2.csv')  # Data used: S&P 500 stocks (08/02/2013 to 07/02/2018) - https://bit.ly/3gRZFfl

# number of days of predictions
days = 100

# create an empty list for the data
dataset = []

year = 0  # split the data-sets into one-year windows. Can here change the indexing year.
for i in file.close[365*year:365*(year+1)]:  # study the stock prices at the market closing time
    if i == float(i):
        dataset.append(i)

# remove the last few days so that the simulated predictions "extend" the data
restricted_data = dataset[0:len(dataset) - days]


def market_predictions(data):
        dataset = data
        dt = 1
        T = days
        N = T / dt
        t = np.arange(1, int(N) + 1)

        # Calculate mean following the method from the article (line 2)
        returns = []
        r = 0
        for i in range(len(restricted_data)):
            t = (restricted_data[i] - restricted_data[i - 1]) / restricted_data[i - 1]
            returns.append(t)
            r = r + t

        mu = r / len(restricted_data)
        # mu = 0.5*(dt**2)

        # Calculate variance
        sigma = np.std(returns)
        # sigma = dt


        # number of predictions we want
        scenario_size = 10
        # generate some numbers from a normal distribution
        b = {str(scenario): np.random.normal(0, 1, int(N)) for scenario in range(1, scenario_size + 1)}
        # print(b)
        # cumulative addition to the previous value
        W = {str(scenario): b[str(scenario)].cumsum() for scenario in range(1, scenario_size + 1)}
        # print(W)

        drift = (mu - 0.5 * sigma ** 2) * t
        diffusion = {str(scenario): sigma * W[str(scenario)] for scenario in range(1, scenario_size + 1)}

        # initial price
        S_init = restricted_data[-1]

        S = np.array([S_init * np.exp(drift + diffusion[str(scenario)]) for scenario in range(1, scenario_size + 1)])
        S = np.hstack((np.array([[S_init] for scenario in range(scenario_size)]), S))

        index = [i for i in range(len(restricted_data), len(dataset) + 1)]

        # plot the predictions
        for i in range(scenario_size):
            plt.plot(index, S[i, :])

        # f = dataset[len(dataset)-days-1:len(dataset)]


        # plot the actual data
        plt.plot(dataset, 'r')
        plt.xlabel('Time (days)')
        plt.ylabel('Closing price ($)')
        plt.show()
        return "Graph plotted."


a = market_predictions(dataset)


''' VARIANCE ROOT TEST (NOT RELEVANT)

def delta(j, T, var_1, log_prices):
    res = 0
    rets = np.diff(log_prices)
    for t in range(j+1, T):  # NOT SURE ABOUT THE RANGE
        t -= 1  # array index is t-1 for t-th element
        res += np.square((rets[t]-np.mean(rets))*(rets[t-j]-np.mean(rets)))
    return res / ((T-1) * var_1)**2


def variance_ratio_test(data):
    price_series = data
    log_return_series = []
    for i in range(len(price_series)-1):
        x = np.log(price_series[i+1]/price_series[i])
        log_return_series.append(x)
    var_1 = np.var(log_return_series, ddof=1)  # one-period return sample variance
    vr_list = []
    T = len(log_return_series)  # number of log-data points
    for k in range(1, T):
        m = k*(T - k + 1)*(1 - k/T)  # this accounts for the bias of the var_k estimator defined below
        sum_term = []
        for i in range(k, len(price_series)):
            y = (np.log(price_series[i] / price_series[i - k]) - k*np.mean(log_return_series))**2
            sum_term.append(y)
        var_k = (1/m)*np.sum(sum_term)  # k-period return variance (as described by Lo & MacKinlay)
        vr_k = var_k/var_1
        vr_list.append(vr_k)
    # now, want to check that this variance ratio satisfies an RWH (Random Walk Hypothesis)
    asymptotic_var_vec = []
    for k in range(1, T):
        # asymptotic_var = 2*(2*k - 1)*(k - 1)/(3*k*T)  # variance assuming homoscedasticity
        # the following three lines are the variance assuming heteroscedasticity
        # asymptotic_var = 0
        # for j in range(1, k):
        #     asymptotic_var += (2 * (k - j) / k) ** 2 * delta(j, T, var_1, log_return_series)
        asymptotic_var_vec.append(asymptotic_var)
    centered_sample = vr_list - np.ones(len(vr_list))
    standardized_sample = np.divide(centered_sample, np.sqrt(asymptotic_var_vec))
    # now check the p-value of this sample, under the null hypothesis (Lo & MacKinley) that it is standard normal
    p_value_vector = np.ones(len(standardized_sample)) - norm.cdf(standardized_sample)
    return p_value_vector
'''



'''
NOT RELEVANT - still working on it


want to compare this with just a randomised geometric brownian motion 
that we get from a random walk, the brownian motion is X~N(0,dt)
hence the geometric brownian motion is  Y=e^X, where logY~N(0,dt)

when calculating random walk ---> brownian motion we get X
then we take 


def brown1(x0,t,N):
    dt=t/N
    x=[x0]
    dx=[np.sqrt(dt) * np.random.randn()]

    for i in range(1,N+1):
        dx.append(np.sqrt(dt) * np.random.randn())
        #print(np.sqrt(dt) * np.random.randn())
        x.append(x[i-1]+dx[i])
    print(x)
    y=[np.exp(i) for i in x]
    print(y)
    #print(dx,x)
    return(x)


for i in range(2):
    y=brown1(S_init,dt,days)
    h=[k for k in y]
    print(y,h)
    plt.plot(index,h)

plt.plot(dataset,'r')


print(S_init,dt,days)
'''










