import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

"""Contains visualization code, one that tracks only one stock if that is an option that
is desired and one that tracks all stocks."""
class LivePlotter:
    def __init__(self, symbol, feed, max_points=100):
        self.symbol = symbol
        self.feed = feed
        self.max_points = max_points
        self.prices = deque(maxlen=max_points)
        self.times = deque(maxlen=max_points)

        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot([], [], label=self.symbol)
        self.ax.set_title(f"Live Price for {self.symbol}")
        self.ax.set_xlabel("Points")
        self.ax.set_ylabel("Price")
        self.ax.legend()

    def update(self, frame):
        price = self.feed.get_latest_price(self.symbol)
        if price is not None:
            self.prices.append(price)
            self.times.append(len(self.times))  # just an index for x-axis

            self.line.set_data(self.times, self.prices)
            self.ax.relim()
            self.ax.autoscale_view()

        return self.line,

    def start(self):
        ani = animation.FuncAnimation(self.fig, self.update, interval=1000)
        plt.show()



class MultiStockPlotter:
    def __init__(self, symbols, feed, max_points=100):
        self.symbols = symbols
        self.feed = feed
        self.max_points = max_points
        self.data = {symbol: deque(maxlen=max_points) for symbol in symbols}
        self.timestamps = deque(maxlen=max_points)
        
        self.fig, self.ax = plt.subplots()
        self.lines = {symbol: self.ax.plot([], [], label=symbol)[0] for symbol in symbols}
        self.ax.set_title("Real-Time Stock Prices")
        self.ax.set_xlabel("Time (HH:MM:SS)")
        self.ax.set_ylabel("Price")
        self.ax.legend()

    def update(self, frame):
        import datetime

        now = datetime.datetime.now()
        self.timestamps.append(now)

        for symbol in self.symbols:
            price = self.feed.get_latest_price(symbol)
            if price is not None:
                self.data[symbol].append(price)
            else:
                # Keep last price or None if no data yet
                self.data[symbol].append(self.data[symbol][-1] if self.data[symbol] else None)

        for symbol in self.symbols:
            self.lines[symbol].set_data(list(self.timestamps), list(self.data[symbol]))

        self.ax.relim()
        self.ax.autoscale_view()
        self.ax.tick_params(axis='x', rotation=45)
        return self.lines.values()

    def start(self):
        ani = animation.FuncAnimation(self.fig, self.update, interval=1000, cache_frame_data=False)
        plt.show()