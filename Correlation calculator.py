import pandas as pd

# Replace by the name of the file you have with all the prices
df = pd.read_csv("price_top_15032024.csv")

# Set the 'Date' column as the index
df.set_index('Date', inplace=True)

# Calculate the correlation matrix
correlation_matrix = df.corr('pearson', 700)

# Export the correlation matrix to a CSV file
correlation_matrix.to_csv("correlation_matrix.csv")

print("Correlation Matrix:")
print(correlation_matrix)
print("Correlation matrix exported to correlation_matrix.csv")
