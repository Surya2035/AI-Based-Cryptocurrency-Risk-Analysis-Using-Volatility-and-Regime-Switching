def generate_risk_insight(volatility, regime):

    # High regime probability
    if regime > 0.6:
        return (
            "⚠ High Risk Market Regime Detected.\n\n"
            "The Markov model indicates the market is in a high-volatility state. "
            "Price swings are likely to be large and unpredictable."
        )

    # Volatility spike
    elif volatility > 0.05:
        return (
            "⚡ Volatility Spike Detected.\n\n"
            "Market volatility is currently elevated compared to its historical average. "
            "Risk management strategies are recommended."
        )

    # Normal conditions
    else:
        return (
            "✅ Market Conditions Stable.\n\n"
            "The market is currently in a relatively calm volatility regime. "
            "Risk levels appear moderate."
        )