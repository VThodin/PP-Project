import time
from data_feed import StockDataFeed
from indicators import moving_average, compute_rsi
from alerts import check_alerts
from data_logger import CSVLogger

API_KEY = "d0qm5shr01qg1llahlfgd0qm5shr01qg1llahlg0"
STOCKS = [
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
    loggers = {symbol: CSVLogger(symbol) for symbol in STOCKS}
    price_history = {symbol: [] for symbol in STOCKS}

    try:
        while True:
            for symbol in STOCKS:
                price = feed.get_latest_price(symbol)
                if price is None:
                    continue

                price_history[symbol].append(price)
                loggers[symbol].log_price(price)

                ma = moving_average(price_history[symbol])
                rsi = compute_rsi(price_history[symbol])
                alerts = check_alerts(symbol, price, ma, rsi)

                print(f"{symbol} - Price: {price:.2f}, MA: {ma}, RSI: {rsi}")
                for alert in alerts:
                    print(">>>", alert)

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting sequential stock tracker.")

if __name__ == "__main__":
    main()