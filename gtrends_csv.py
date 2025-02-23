# Install necessary libraries
!pip install yfinance pandas

import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# Define stock tickers for the Music Industry and Related Industry
music_industry_tickers = ["SIRI", "WMG", "SONO"]  # Example: SiriusXM, Warner Music Group, Sonos
related_industry_tickers = ["SPOT", "NFLX", "DIS"]  # Example: Spotify, Netflix, Disney (streaming/entertainment)

# Define date range
end_date = datetime.today().strftime('%Y-%m-%d')
start_date = (datetime.today() - timedelta(days=365)).strftime('%Y-%m-%d')

def fetch_stock_data(tickers, start, end):
    """Fetch historical stock data for the given tickers and save as a DataFrame."""
    stock_data = yf.download(tickers, start=start, end=end)

    # Print columns to check if 'Adj Close' exists
    print("Available columns:", stock_data.keys())

    # Use 'Close' if 'Adj Close' is missing
    if 'Adj Close' in stock_data:
        return stock_data['Adj Close']
    else:
        print("Warning: 'Adj Close' missing, using 'Close' instead.")
        return stock_data['Close'] if 'Close' in stock_data else stock_data

# Fetch data for both industries
music_industry_data = fetch_stock_data(music_industry_tickers, start_date, end_date)
related_industry_data = fetch_stock_data(related_industry_tickers, start_date, end_date)

# Save to CSV
music_csv_path = "/content/Music_Industry_Stocks.csv"
related_csv_path = "/content/Related_Industry_Stocks.csv"

music_industry_data.to_csv(music_csv_path)
related_industry_data.to_csv(related_csv_path)

# Provide download links
from google.colab import files
files.download(music_csv_path)
files.download(related_csv_path)

print("Download the CSV files for Music and Related Industries.")
