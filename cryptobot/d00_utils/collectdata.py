#!/usr/bin/env python3
# collectdata.py

from .. import constant as const
from ...conf.secrets import EMAIL, PASSWORD

import pandas as pd
import robin_stocks as r


def collect_historical_data(ticker, interval='hour', span='week', bounds='24_7'):
    login = r.login(EMAIL, PASSWORD)
    all_crypto_tickers = load_crypto_list()

    if ticker not in all_crypto_tickers:
        return pd.DataFrame()

    hist = r.get_crypto_historicals(
        ticker,
        interval=interval,
        span=span,
        bounds=bounds
    )
    hist_df = pd.DataFrame()

    for i in range(len(hist)):
        df = pd.DataFrame(hist[i], index=[i])
        hist_df = pd.concat([hist_df, df])

    hist_df.to_csv(f"../../data/crypto/01_raw/d01-{ticker}-historical.csv", " ")

    print(
        f"Raw historical data over the time frame {span} for {ticker} has been saved.")

    return hist_df


def collect_crypto_tickers():
    crypto_info_dicts = r.get_crypto_currency_pairs(info='asset_currency')
    crypto_list = []

    for currency in crypto_info_dicts:
        if 'code' in currency.keys():
            crypto_list.append(currency['code'])

    return crypto_list


def save_crypto_list(crypto_list):
    try:
        f = open("../../data/crypto/03_processed/available-crypto-tickers.txt", "w")
        f.writelines("\n".join(crypto_list))
        f.close()
        return print("The list of available cryptocurrencies has been updated.")
    except FileNotFoundError as err:
        return print("Failed to update list of available cryptocurrencies.\n", err)


def load_crypto_list():
    try:
        full_crypto_list = []
        with open("../../data/crypto/03_processed/available-crypto-tickers.txt", "r") as f:
            for line in f:
                full_crypto_list.append(line.strip("\n"))
        return full_crypto_list
    except FileNotFoundError as err:
        print("Failed to load list of available cryptocurrencies.\n")
        print("Attempting to generate list...\n")

        full_crypto_list = collect_crypto_tickers()
        if len(full_crypto_list) != 0:
            save_crypto_list(full_crypto_list)
        else:
            print("Error: Unabled to retrieve list of available cryptocurrencies.\n")
        return full_crypto_list


# full_list = collect_crypto_tickers()

# save_crypto_list(full_list)

# for tick in full_list:
#     collect_historical_data(tick, 'day', '5year', '24_7')

# collect_historical_data("BCH", 'day', 'year', '24_7')
