import csv
from datetime import datetime
import threading

class CSVLogger:
    def __init__(self, symbol):
        self.symbol = symbol
        self.filename = f"data/{symbol}_prices.csv"
        self.lock = threading.Lock()
        # Write header once
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['timestamp', 'price', 'ma', 'rsi'])

    def log_price(self, price):
        timestamp = datetime.now().isoformat()
        with self.lock:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([timestamp, price])