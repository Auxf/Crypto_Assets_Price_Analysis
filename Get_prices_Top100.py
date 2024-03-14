import requests
import csv
import time
from datetime import datetime

# Function to fetch the top 100 coin IDs
def fetch_top_100_coin_ids():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [coin["id"] for coin in data]
    else:
        print("Error fetching top 100 coin IDs:", response.status_code)
        return []

# Function to fetch price data for a single coin ID
def fetch_coin_data(coin_id):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart/range?vs_currency=usd&from=1615748443&to=1710446443&precision=full"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["prices"]
    else:
        print(f"Error fetching data for coin {coin_id}: {response.status_code}")
        return []

# Function to convert timestamp to date
def convert_timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d')

# Function to save data to CSV file
def save_to_csv(data, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date"] + list(data.keys()))
        dates = sorted(set(date for coin_data in data.values() for date in coin_data.keys()))
        for date in dates:
            row = [date] + [data[coin_id].get(date, None) for coin_id in data.keys()]
            writer.writerow(row)

def main():
    # Fetch top 100 coin IDs
    coin_ids = fetch_top_100_coin_ids()

    # Fetch price data for each coin ID
    data = {}
    for coin_id in coin_ids:
        coin_data = fetch_coin_data(coin_id)
        if coin_data:
            data[coin_id] = {convert_timestamp_to_date(timestamp): price for timestamp, price in coin_data}
        time.sleep(21)  # 21 seconds delay between API calls

    # Save data to CSV file
    if data:
        save_to_csv(data, "price_top.csv")
        print("Data saved to price_top.csv")

if __name__ == "__main__":
    main()
