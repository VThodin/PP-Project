from indicators import moving_average, compute_rsi
from alerts import check_alerts
import time
from data_logger import CSVLogger
import threading
import ctypes
from predictors import predict_next
from datetime import datetime, timedelta
"""This file does the main work for every stock, it uses the other files to get prices, give alerts, predictions and prints to terminal all info"""
def track_stock(symbol, feed, enable_plot=False):
    prices = []
    logger = CSVLogger(symbol)
    minute_prices = []  # Store 1 price per minute

    last_minute = datetime.now().minute
    

    while True:
        price = feed.get_latest_price(symbol)
        if price is None:
            time.sleep(0.5)
            continue

        prices.append(price)
        logger.log_price(price)

        current_minute = datetime.now().minute
        if current_minute != last_minute:
            minute_prices.append(price)
            last_minute = current_minute
        
        ma = moving_average(prices, period=5)
        rsi = compute_rsi(prices, period=14)
        prediction = predict_next(minute_prices, past_window=10, offset=5)
        if prediction:
            print(f"[{symbol}] 5-min Prediction: {prediction:.2f}")

        alerts = check_alerts(symbol, price, ma, rsi)

        print(f"{symbol} - Price: {price}, MA: {ma}, RSI: {rsi}")
        for alert in alerts:
            print(">>>", alert)
            ctypes.windll.user32.MessageBoxW(0, alert, "RSI ALERT", 0)
        time.sleep(1)