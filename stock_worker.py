from indicators import moving_average, compute_rsi
from alerts import check_alerts
import time
from data_logger import CSVLogger
import threading
import ctypes

def track_stock(symbol, feed, enable_plot=False):
    prices = []
    logger = CSVLogger(symbol)

    while True:
        price = feed.get_latest_price(symbol)
        if price is None:
            time.sleep(0.5)
            continue

        prices.append(price)
        logger.log_price(price)
        
        ma = moving_average(prices, period=5)
        rsi = compute_rsi(prices, period=14)
        alerts = check_alerts(symbol, price, ma, rsi)

        print(f"{symbol} - Price: {price}, MA: {ma}, RSI: {rsi}")
        for alert in alerts:
            print(">>>", alert)
            ctypes.windll.user32.MessageBoxW(0, alert, "RSI ALERT", 0)
        time.sleep(1)