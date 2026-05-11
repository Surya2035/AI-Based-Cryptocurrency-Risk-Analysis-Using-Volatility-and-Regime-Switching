from arch import arch_model
import pandas as pd

def compute_garch_volatility(df, coin):

    # select specific coin
    coin_df = df[df["Coin"] == coin].copy()

    # remove missing values
    coin_df = coin_df.dropna()

    # returns for GARCH
    returns = coin_df["Return"] * 100

    # fit GARCH model
    model = arch_model(returns, vol="Garch", p=1, q=1)

    results = model.fit(disp="off")

    # add conditional volatility
    coin_df["GARCH_volatility"] = results.conditional_volatility

    return coin_df