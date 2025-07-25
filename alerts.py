"""This file is for checking and givin alerts for when it could be a
good oppurtinity to buy or sell.
The alerts for RSI should probaby be changed or be something completely different
since it currently spams you with message windows."""
def check_alerts(symbol, price, ma, rsi):
    alerts = []
    if rsi is not None:
        if rsi < 30:
            alerts.append(f"[{symbol}] RSI LOW ALERT, BUY NOW!: {rsi:.2f}")
        elif rsi > 70:
            alerts.append(f"[{symbol}] RSI HIGH ALERT, SELL NOW!: {rsi:.2f}")

    if ma is not None and price > ma * 1.05:
        alerts.append(f"[{symbol}] PRICE ABOVE MA: {price} > {ma:.2f}")
    return alerts