import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv("price_top_15032024.csv")

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Calculate daily returns for each token
returns_df = df.pct_change().dropna()

# Calculate standard deviation of daily returns for each token
volatility_series = returns_df.std()

# Sort tokens by volatility (from most volatile to least volatile)
ranked_volatility = volatility_series.sort_values(ascending=False)

# Print the ranked volatility
print("Ranking of tokens by volatility:")
print(ranked_volatility)

# Save the ranked volatility to a CSV file
ranked_volatility.to_csv("crypto_volatility.csv")

print("Volatility ranking saved to crypto_volatility.csv")
