# Crypto_Assets_Price_Analysis

This project is about getting the prices of the Top 100 tokens on CoinGecko for further analysis.

To perform test analysis, you can find the file "price_top_15032024.csv" from the 15th of March 2024.

To actualize this data set, download and run the file "Get_prices_Top100.py". It will take around 30 minutes because the script integrates breaks to avoid the rate limits.

Once you have a CSV file with all the actualized data, you can use the script "Correlation calculator.py" to perform correlation matrixes between the 100 assets. This correlation is customizable (method and number of data required).

Finally, the "Volatility Calculator.py" allows you to calculate each crypto asset's volatility and ranks the most volatile to the least volatile assets of the Top 100. You still need to redirect the script to the file with the data if you actualized it or even changed the name.
