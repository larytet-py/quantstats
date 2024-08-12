import pandas as pd
from scipy import stats
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Outlier analysis on daily balance')
parser.add_argument('csv_file', type=str, help='Path to the CSV file')

# Parse command line arguments
args = parser.parse_args()

# Load the data from the CSV file specified in the command line
df = pd.read_csv(args.csv_file)

# Convert 'Balance' to numeric (in case it's read as a string)
df['Balance'] = pd.to_numeric(df['Balance'], errors='coerce')

# Calculate the Z-scores for the 'Balance' column
df['z_score'] = stats.zscore(df['Balance'])

# Identify outliers (Z-score > 3 or < -3 are commonly considered outliers)
df['is_outlier'] = df['z_score'].abs() > 2

# Print the DataFrame with the Z-scores and outlier identification
outliers_df = df[df['is_outlier'] == True]
print(outliers_df)
