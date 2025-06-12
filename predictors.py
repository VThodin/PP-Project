import numpy as np
from sklearn.linear_model import LinearRegression

def predict_next(prices, past_window=10 ,offset=5):
    if len(prices) < past_window: return None
    x = np.array(past_window).reshape(-1, 1)
    y = np.array(prices[-past_window:])
    model = LinearRegression(x, y)
    return model.predict([[past_window + offset - 1]])[0]