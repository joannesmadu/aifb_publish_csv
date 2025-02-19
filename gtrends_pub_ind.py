# Re-import necessary libraries after execution state reset
import pandas as pd
import datetime

# Define dummy data to simulate Google Trends data retrieval
dates = pd.date_range(start="2019-01-01", periods=60, freq='M')

# Publishing industry keywords
publishing_data = pd.DataFrame({
    "Date": dates,
    "E-Books": [abs(hash("ebooks"+str(d))) % 100 for d in dates],
    "Audiobooks": [abs(hash("audiobooks"+str(d))) % 100 for d in dates],
    "Print Books": [abs(hash("print_books"+str(d))) % 100 for d in dates],
    "Self-Publishing": [abs(hash("self_publishing"+str(d))) % 100 for d in dates],
    "Digital Magazines": [abs(hash("digital_magazines"+str(d))) % 100 for d in dates]
})

# Related industry: Media and journalism keywords
journalism_data = pd.DataFrame({
    "Date": dates,
    "Online News": [abs(hash("online_news"+str(d))) % 100 for d in dates],
    "Print Newspapers": [abs(hash("print_newspapers"+str(d))) % 100 for d in dates],
    "Broadcast Journalism": [abs(hash("broadcast_journalism"+str(d))) % 100 for d in dates],
    "Investigative Reporting": [abs(hash("investigative_reporting"+str(d))) % 100 for d in dates],
    "Podcasting": [abs(hash("podcasting"+str(d))) % 100 for d in dates]
})

# Save data to CSV files
publishing_csv_path = "/mnt/data/publishing_industry_trends.csv"
journalism_csv_path = "/mnt/data/journalism_industry_trends.csv"

publishing_data.to_csv(publishing_csv_path, index=False)
journalism_data.to_csv(journalism_csv_path, index=False)

# Provide file paths for download
publishing_csv_path, journalism_csv_path
