
import requests
import os
from dotenv import load_dotenv
import pandas as pd
import datetime

date_time = datetime.datetime.now()

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")


symbol = input("Please enter a stock symbol: ")

train = pd.read_table("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv")
train.head()

request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={symbol}&apikey={ALPHAVANTAGE_API_KEY}&datatype=csv"

response = requests.get(request_url)
print("------------------------------")
print("You selected:",symbol)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", date_time)
# print(type(response))
# print(response.text)