import numpy as np
import pandas as pd
import os
import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew, kurtosis

# Load historical prices data
stock_symbols = ['QCOM', 'AMD', 'AAPL', 'NVDA', 'MSFT', 'F', 'KO', 'WMT', 'WELL', 'XOM', 'CVX', 'IMO']

for symbol in stock_symbols:
    print(symbol)

stock_data = yf.download(stock_symbols, start='2003-01-01', end='2023-01-01')['Adj Close']
spx_data = yf.download('^GSPC', start='2003-01-01', end='2023-01-01')['Adj Close']

# Plot daily prices
fig, ax1 = plt.subplots(figsize=(14, 8))

color = 'tab:blue'
ax1.set_xlabel('Date')
ax1.set_ylabel('Stock Prices', color=color)
ax1.plot(stock_data, alpha=0.6)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
color = 'tab:red'
ax2.set_ylabel('S&P 500 Index', color=color)
ax2.plot(spx_data, color=color, alpha=0.6)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Daily Prices of 12 Stocks and S&P 500 Index')
output_dir = './figures'
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'stock_prices.png'))
plt.show()

print(stock_data)
