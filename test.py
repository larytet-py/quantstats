# pip3 install virtualenv
# python3 -m venv myenv
# ~/.local/bin/virtualenv myenv
# source myenv/bin/activate
# pip3 install ipython
# pip3 install -r requirements.txt
# pip3 install notebook
# ~/.local/bin/jupyter-notebook
import pandas as pd
import quantstats as qs
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filename', type=str, help='The CSV file to be processed', default='BTCLV TRADES.csv')
args = parser.parse_args()

filename = args.filename
print(f'Processing file: {filename}')

# Extend pandas functionality with metrics, etc.
qs.extend_pandas()

# Read the CSV file into a DataFrame
trades = pd.read_csv(filename, parse_dates=['End Time', 'Next Start Time'])

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
qs.plots.snapshot(daily_returns, title='BTC Performance', show=True)
qs.reports.html(daily_returns, title='BTC Trading Performance Report', output='btc_trading_performance_report.html')