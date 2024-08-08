# pip3 install virtualenv
# python3 -m venv myenv
# ~/.local/bin/virtualenv myenv
# source myenv/bin/activate
# pip3 install ipython
# pip3 install -r requirements.txt
# pip3 install notebook
# ~/.local/bin/jupyter-notebook

# Required imports
import pandas as pd
import quantstats as qs
import argparse

# Argument parser setup
parser = argparse.ArgumentParser(description='Process equity data.')
parser.add_argument('filename', type=str, help='The CSV file to be processed')
parser.add_argument('--mode', type=str, choices=['backtest', 'bot'], default='backtest', help='Mode of operation: "backtest" or "bot"')
args = parser.parse_args()

columns_names = {"time":"End Time", "balance": "Balance", "format": '%Y-%m-%d %H:%M:%S'}
if args.mode == 'bot':
    columns_names = {"time":"Time", "balance": "daily balance", "format": '%Y-%m-%d %H:%M:%S'}

# Get filename from arguments
filename = args.filename
print(f'Processing file: {filename}')

# Extend pandas functionality with metrics, etc.
qs.extend_pandas()

# Read the CSV file into a DataFrame
trades = pd.read_csv(filename)

# Parse the 'Time' column with the specified date format
trades[columns_names['time']] = pd.to_datetime(trades[columns_names['time']], format=columns_names['format'], errors='coerce')

# Check if there are any parsing issues
if trades[columns_names['time']].isnull().any():
    print("Warning: There are parsing issues with the 'Time' column. Some dates might be NaT.")

# Drop rows with NaT in 'Time' column
# trades.dropna(subset=['Time'], inplace=True)

# Set the 'Time' column as the index
trades.set_index(columns_names['time'], inplace=True)

# Ensure the index is sorted
trades.sort_index(inplace=True)

# Use raw equity data for plotting and reporting
equity_data = trades[columns_names['balance']]

# Plot the equity performance
qs.plots.snapshot(equity_data, title='Equity Performance', show=True)

# Generate an equity performance report
qs.reports.html(equity_data, title='Trading Performance Report for '+filename, output=filename+'.html')


