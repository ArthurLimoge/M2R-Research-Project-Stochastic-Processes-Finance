---
title: "Variance ratio test for market efficiency"
Arthur Limoge, Munazza Sarwar, Timothy Kang
date: "21/10/2019"
---

# Don't forget to download the datasets to the working directory, and import them to RStudio before running the code.


First import the stock data from the S&P500 dataset ("Dataset6.csv" on: https://github.com/ArthurLimoge/M2R-Project); create a prices_vector for each ticker 

```{r}

data <- split(Dataset6$close, Dataset6$ticker) # splits the stock prices based on the ticker. We will treat each sample independently. 
number_tickers = length(data)
list_log_series <- list()
for(i in 1:number_tickers){
  price_series = unlist(data[i])
  log_return_series <- c()
  sample_size <- length(price_series)
  log_return_series <- log(price_series[2:sample_size]) - log(price_series[1:sample_size-1])
  list_log_series[[i]] <- log_return_series
}



```

We can now, on each one these log return series, apply the Variance Ratio Test for Market Efficiency (as described by Lo & MacKinley in 1988), by using the function Auto.VR from the 'vrtest' package.

```{r}

vr_vec <- c()
for(i in 1:number_tickers){
  log_return_series = unlist(list_log_series[i])
  var_ratio = unlist(Auto.VR(log_return_series)[1])
  vr_vec <- c(vr_vec, var_ratio)
}

```


According to the theory by Lo and MacKinley, each of those variance ratios should follow a standard normal distribution. So vr_vec should look like a standard normal sample. An easy way to (not formally) check it could be to visualize how the values look when plotted against a standard Gaussian:

```{r}

lower.x <- -1.96
upper.x <- 1.96
step <- (upper.x - lower.x) / 100
sigma <- 1
mu <- 0
bounds <- c(mu-3*sigma, mu+3*sigma)
cord.x <- c(lower.x,seq(lower.x,upper.x,step),upper.x)
cord.y <- c(0,dnorm(seq(lower.x,upper.x,step),mu,sigma),0)
curve(dnorm(x,mu,sigma),xlim=bounds) 
polygon(cord.x,cord.y,col='skyblue')
y_points = integer(27)
points(vr_vec, y_points, pch = 19, col = 'firebrick')
title(main="95% confidence interval and Variance ratios",
   xlab="x", ylab="y")

```

In blue, a 95% confidence interval for the standard normal. 

Now, a more rigorous way to check if our sample can indeed be approximated by a standard normal is to draw a quantile-quantile (QQ) plot.

```{r}

qqnorm(vr_vec, pch = 1, col = "deeppink", frame = FALSE)
qqline(vr_vec, col = "darkslategray", lwd = 2)

```

