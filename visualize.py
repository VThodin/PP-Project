import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

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