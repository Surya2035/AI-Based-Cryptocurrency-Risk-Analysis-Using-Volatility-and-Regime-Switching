def detect_volatility_spikes(df):

    threshold = df["Volatility"].mean() + 2 * df["Volatility"].std()

    df["Volatility_Explosion"] = df["Volatility"] > threshold

    return df