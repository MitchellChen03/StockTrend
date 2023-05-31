import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Retrieve stock data from Yahoo Finance
ticker = "AAPL"
start_date = "2023-04-01"
end_date = "2023-05-22"
data = yf.download(ticker, start=start_date, end=end_date)

# Compute the rolling mean and standard deviation
#rolling mean is the moving 21 day average: We used 21 days because why not. rolling_std is the root of the stock.
window_size = 21
rolling_mean = data['Close'].rolling(window_size).mean()
rolling_std = data['Close'].rolling(window_size).std()


# Compute the upper and lower bands
# We use the upper and lower bands as a indicator for the trend to see where the stock is going.
# Upper band: 30 day moving average subtract 2 times of the 30 day root of the price
# lower band: 30 day moving average subtract 2 times of the 30 day root of the price

upper_band = rolling_mean + (2 * rolling_std)
lower_band = rolling_mean - (2 * rolling_std)

# Plot the stock prices, rolling mean, and Bollinger Bands
#This basically just plots everything so far...
plt.plot(data['Close'], label='Close')
plt.plot(rolling_mean, label='Rolling Mean')
plt.plot(upper_band, label='Upper Band')
plt.plot(lower_band, label='Lower Band')
plt.legend()

# Predict the trend line
x = np.array(range(len(data)))
y = data['Close'].values
z = np.polyfit(x, y, 1)
print(z)
trend_line = z[0]*x + z[1]
print(trend_line)

# Plot the trend line
plt.plot(data.index, trend_line, label='Trend Line')
plt.legend()

# Show the plot
plt.show()
