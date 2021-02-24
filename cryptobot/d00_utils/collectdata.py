#!/usr/bin/env python3
# collectdata.py

import pandas as pd
import robin_stocks.robinhood as rh
from conf.secrets import EMAIL, PASSWORD
from cryptobot.constant import RAW_DIR, REF_DIR, TRADABLE_CRYPTOS
from cryptobot.d01_data.load_save_data import load_json_data


def collect_historical_data(ticker, interval='hour', span='week', bounds='24_7'):
    login = rh.login(EMAIL, PASSWORD)
    crypto_df = load_json_data(REF_DIR, TRADABLE_CRYPTOS)

    if ticker not in crypto_df.values:
        return pd.DataFrame()

    hist = rh.get_crypto_historicals(
        ticker,
        interval=interval,
        span=span,
        bounds=bounds
    )
    hist_df = pd.DataFrame()

    for i in range(len(hist)):
        df = pd.DataFrame(hist[i], index=[i])
        hist_df = pd.concat([hist_df, df])

    hist_df.to_csv(f"{RAW_DIR}d01-{ticker}-historical.csv", sep=" ")

    print(
        f"Raw historical data over the time frame {span} for {ticker} has been saved.")

    return hist_df


def collect_crypto_tickers():
    crypto_info_dicts = rh.get_crypto_currency_pairs()
    crypto_df = pd.DataFrame()

    i = 0
    for currency in crypto_info_dicts:
        if currency['tradability'] == "tradable":
            curr_dict = {}
            curr_dict['code'] = currency['asset_currency']['code']
            curr_dict['name'] = currency['asset_currency']['name']
            df = pd.DataFrame(curr_dict, index=[i])
            crypto_df = pd.concat([crypto_df, df])
            i += 1

    crypto_df.to_json(f"{REF_DIR}{TRADABLE_CRYPTOS}")

    print("The list of tradable cryptocurrencies has been updated.")
    return
