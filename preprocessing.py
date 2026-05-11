import pandas as pd
import numpy as np

def preprocess():

    df = pd.read_csv("data/crypto_data.csv")

    df["Date"] = pd.to_datetime(df["Date"])

    df = df.sort_values(["Coin", "Date"])

    # log returns
    df["Return"] = df.groupby("Coin")["Price"].transform(
        lambda x: np.log(x / x.shift(1))
    )

    # rolling volatility
    df["Volatility"] = df.groupby("Coin")["Return"].transform(
        lambda x: x.rolling(5).std()
    )

    return df