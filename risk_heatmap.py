import pandas as pd

def compute_risk_heatmap(df):

    risk_table = df.groupby("Coin").agg({
        "Volatility":"mean",
        "Return":"mean"
    }).reset_index()

    risk_table["RiskScore"] = risk_table["Volatility"] * 100

    return risk_table