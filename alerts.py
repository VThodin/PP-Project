def check_alerts(symbol, price, ma, rsi):
    alerts = []
    if rsi is not None:
        if rsi < 30:
            alerts.append(f"[{symbol}] RSI LOW ALERT: {rsi:.2f}")
        elif rsi > 70:
            alerts.append(f"[{symbol}] RSI HIGH ALERT: {rsi:.2f}")

    if ma is not None and price > ma * 1.05:
        alerts.append(f"[{symbol}] PRICE ABOVE MA: {price} > {ma:.2f}")
    return alerts