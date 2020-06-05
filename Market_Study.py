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
# file = pd.read_csv('Dataset1.csv')  
file = pd.read_csv('Dataset2.csv')  # sources for the datasets: https://github.com/ArthurLimoge/M2R-Project
# file = pd.read_csv('Dataset3.csv')

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










