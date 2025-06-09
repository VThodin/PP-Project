import threading
from data_feed import StockDataFeed
from stock_worker import track_stock
from visualize import LivePlotter, MultiStockPlotter

API_KEY = "d0qm5shr01qg1llahlfgd0qm5shr01qg1llahlg0"
STOCKS = ['AAPL', 'GOOGL', 'TSLA', 'MSFT', ]

def main():
    feed = StockDataFeed(STOCKS, API_KEY)
    threads = []

    for symbol in STOCKS:
        # Enable plottiniklmg only for one stock to keep UI manageable
        #enable_plot = (symbol)
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