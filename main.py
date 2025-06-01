import threading
from data_feed import StockDataFeed
from stock_worker import track_stock
from visualize import LivePlotter

API_KEY = "d0qm5shr01qg1llahlfgd0qm5shr01qg1llahlg0"
STOCKS = ['AAPL', 'GOOGL', 'TSLA']

def main():
    feed = StockDataFeed(STOCKS, API_KEY)
    threads = []

    for symbol in STOCKS:
        # Enable plotting only for one stock to keep UI manageable
        enable_plot = (symbol == STOCKS[0])
        t = threading.Thread(target=track_stock, args=(symbol, feed, enable_plot))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

if __name__ == "__main__":
    main()