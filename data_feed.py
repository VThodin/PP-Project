import websocket
import json
import threading
from collections import deque
"""This file handles the communication with finnhub
It is set to run forever until the terminal is terminated"""
class StockDataFeed:
    def __init__(self, symbols, api_key, buffer_size=100):
        self.symbols = symbols
        self.api_key = api_key
        self.url = f"wss://ws.finnhub.io?token={api_key}"
        self.price_buffers = {symbol: deque(maxlen=buffer_size) for symbol in symbols}
        self.lock = threading.Lock()

        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )

        self.thread = threading.Thread(target=self.ws.run_forever, daemon=True)
        self.thread.start()

    def on_open(self, ws):
        print("WebSocket connected")
        for symbol in self.symbols:
            ws.send(json.dumps({
                "type": "subscribe",
                "symbol": symbol
            }))
            print(f"Subscribed to {symbol}")

    def on_message(self, ws, message):
        data = json.loads(message)
        if data["type"] == "trade":
            for trade in data["data"]:
                symbol = trade["s"]
                price = trade["p"]
                with self.lock:
                    self.price_buffers[symbol].append(price)

    def get_latest_price(self, symbol):
        with self.lock:
            if symbol in self.price_buffers and self.price_buffers[symbol]:
                return self.price_buffers[symbol][-1]
        return None

    def get_price_history(self, symbol):
        with self.lock:
            return list(self.price_buffers.get(symbol, []))

    def on_error(self, ws, error):
        print("WebSocket error:", error)

    def on_close(self, ws, close_status_code, close_msg):
        print("WebSocket closed:", close_msg)