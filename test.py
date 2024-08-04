%matplotlib inline
import pandas as pd
import quantstats as qs

# Extend pandas functionality with metrics, etc.
qs.extend_pandas()

# Read the CSV file into a DataFrame
trades = pd.read_csv('trades.csv', parse_dates=['End Time', 'Next Start Time'])

# Set the 'End Time' as the index
trades.set_index('End Time', inplace=True)

# Resample to daily frequency and forward-fill missing values
daily_equity = trades['Equity'].resample('D').ffill()

# Calculate daily returns
daily_returns = daily_equity.pct_change().dropna()

# Calculate the Sharpe ratio
sharpe_ratio = qs.stats.sharpe(daily_returns)

# Print the Sharpe ratio
print(f'Sharpe Ratio: {sharpe_ratio}')

# Alternatively, using the extend_pandas() functionality
print(daily_returns.sharpe())
