import requests
import pandas as pd
from datetime import datetime
import os
import time

DATA_PATH = "data/crypto_data.csv"

# Top crypto trading pairs
COINS = {
    "BTCUSDT": "Bitcoin",
    "ETHUSDT": "Ethereum",
    "BNBUSDT": "BNB",
    "XRPUSDT": "XRP",
    "SOLUSDT": "Solana",
    "ADAUSDT": "Cardano",
    "DOGEUSDT": "Dogecoin",
    "TRXUSDT": "TRON",
    "AVAXUSDT": "Avalanche",
    "DOTUSDT": "Polkadot"
}

def download_coin(symbol, name):

    print("Downloading:", name)

    url = "https://api.binance.com/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": "1d",   # daily data
        "limit": 365        # last 365 days
    }

    response = requests.get(url, params=params)

    data = response.json()

    rows = []

    for kline in data:

        rows.append({
            "Date": datetime.fromtimestamp(kline[0] / 1000),
            "Coin": name,
            "Open": float(kline[1]),
            "High": float(kline[2]),
            "Low": float(kline[3]),
            "Close": float(kline[4]),
            "Volume": float(kline[5]),
            "Price": float(kline[4])
        })

    return rows


def scrape_top10():

    all_rows = []

    for symbol, name in COINS.items():

        rows = download_coin(symbol, name)

        all_rows.extend(rows)

        time.sleep(1)

    df = pd.DataFrame(all_rows)

    os.makedirs("data", exist_ok=True)

    df.to_csv(DATA_PATH, index=False)

    print("Dataset saved successfully")

    return df


if __name__ == "__main__":
    scrape_top10()