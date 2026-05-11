import numpy as np

def max_drawdown(price):

    peak = price.expanding(min_periods=1).max()

    drawdown = (price - peak)/peak

    return drawdown.min()

def risk_level(volatility):

    if volatility > 0.05:
        return "HIGH"

    elif volatility > 0.02:
        return "MEDIUM"

    else:
        return "LOW"