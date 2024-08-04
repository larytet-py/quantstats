# %matplotlib inline
import pandas as pd
import quantstats as qs
import argparse

parser = argparse.ArgumentParser(description='Calculate Sharpe Ratio from trades CSV file.')
parser.add_argument('filename', type=str, help='The path to the trades CSV file')

# Parse the arguments
args = parser.parse_args()


# Extend pandas functionality with metrics, etc.
qs.extend_pandas()


# Read the CSV file into a DataFrame
trades = pd.read_csv(args.filename, parse_dates=['End Time', 'Next Start Time'])

# Set the 'End Time' as the index
trades.set_index('End Time', inplace=True)

# Resample to daily frequency and forward-fill missing values
daily_equity = trades['Balance'].resample('D').ffill()

# Calculate daily returns
daily_returns = daily_equity.pct_change().dropna()

# Calculate the Sharpe ratio
sharpe_ratio = qs.stats.sharpe(daily_returns)

# Print the Sharpe ratio
print(f'Sharpe Ratio: {sharpe_ratio}')

# Alternatively, using the extend_pandas() functionality
print(daily_returns.sharpe())
