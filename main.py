import threading
from data_feed import StockDataFeed
from stock_worker import track_stock
from visualize import MultiStockPlotter
from datetime import datetime

"""This file is used to start the project and different threads.
Stocks that we want to track are given as a list.
This file aslso starts a plot tracking the development of all the stocks, altough
it is not very useful if you don't run the program for a long time or only track one stock
or two with similar starting prices."""

API_KEY = "d0qm5shr01qg1llahlfgd0qm5shr01qg1llahlg0"
STOCKS = [
    'AAPL','MSFT','GOOGL','AMZN','TSLA','NVDA']

STOCKS2 = [
    'AAPL','MSFT','GOOGL','AMZN','META','TSLA','NVDA',
    'JPM','BAC','WFC','C',
    'PFE','JNJ','MRK','ABBV',
    'KO','PG','DIS','NFLX','MCD',
    'XOM','CVX','BA','CAT','GE',
    'DUK','SO','NEE',
    'T','VZ',
    'UPS','UAL'
]

def main():
    feed = StockDataFeed(STOCKS, API_KEY)
    threads = []

    for symbol in STOCKS:
        # Enable plottiniklmg only for one stock to keep UI manageable
        #enable_plot = (symbol)
        print(f"[{symbol}] Starting thread at {datetime.now()}")
        t = threading.Thread(target=track_stock, args=(symbol, feed))
        t.start()
        threads.append(t)
        #vissualize = LivePlotter(symbol, feed)
        #vissualize.start()
    

    visualize = MultiStockPlotter(STOCKS, feed)
    visualize.start()
    for t in threads:
        t.join()

if __name__ == "__main__":
    main()