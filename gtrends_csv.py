# Install necessary libraries (for Google Colab or local machine)
!pip install yfinance pandas

import yfinance as yf
import pandas as pd

# Define stock tickers
textile_tickers = ["VFC", "NKE", "HNNMY", "ADDYY", "GPS"]
related_tickers = ["TJX", "ROST", "BURL", "ZGN", "LVMUY"]

# Function to fetch stock data and handle missing columns
def get_stock_data(tickers):
    try:
        # Fetch 5 years of monthly data
        data = yf.download(tickers, period="5y", interval="1mo")

        # Check available columns
        print(f"Available columns: {data.columns.levels[0] if isinstance(data.columns, pd.MultiIndex) else data.columns}")

        # Prioritize 'Adj Close' but use 'Close' if missing
        if "Adj Close" in data.columns:
            data = data["Adj Close"]
        elif "Close" in data.columns:
            data = data["Close"]
        else:
            print("⚠ No 'Adj Close' or 'Close' column found!")
            return pd.DataFrame()  # Return empty DataFrame if no price data is available

        return data

    except Exception as e:
        print(f"❌ Error fetching data: {e}")
        return pd.DataFrame()

# Fetch data for textiles industry
print("Fetching Yahoo Finance data for Textile Industry...")
textile_stock_data = get_stock_data(textile_tickers)

# Fetch data for related industry
print("Fetching Yahoo Finance data for Related Industry (Apparel & Retail)...")
related_stock_data = get_stock_data(related_tickers)

# Save to CSV files only if data exists
if not textile_stock_data.empty:
    textile_csv_path = "textile_stock_data.csv"
    textile_stock_data.to_csv(textile_csv_path)
    print(f"✅ Textile industry data saved to {textile_csv_path}")

if not related_stock_data.empty:
    related_csv_path = "related_stock_data.csv"
    related_stock_data.to_csv(related_csv_path)
    print(f"✅ Related industry data saved to {related_csv_path}")

print("✅ Data retrieval complete!")
