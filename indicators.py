import numpy as np

#This file does the calculations for moving average and rsi.
def moving_average(data, period=5):
    if len(data) < period:
        return None
    return np.mean(data[-period:])

def compute_rsi(data, period=14):
    if len(data) < period + 1:
        return None
    deltas = np.diff(data[-(period+1):])
    gain = np.mean([d for d in deltas if d > 0])
    loss = np.mean([-d for d in deltas if d < 0])
    if loss == 0: return 100
    rs = gain / loss
    return 100 - (100 / (1 + rs))