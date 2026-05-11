import statsmodels.api as sm

def compute_regime_switching(df, coin):

    coin_df = df[df["Coin"] == coin]

    returns = coin_df["Return"].dropna()

    model = sm.tsa.MarkovRegression(
        returns,
        k_regimes=2,
        trend='c',
        switching_variance=True
    )

    results = model.fit()

    regimes = results.smoothed_marginal_probabilities[1]

    coin_df = coin_df.iloc[-len(regimes):]

    coin_df["Regime"] = regimes.values

    return coin_df