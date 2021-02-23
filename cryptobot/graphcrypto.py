#!/usr/bin/env python3
# graphcrypto.py

from ..conf.secrets import EMAIL, PASSWORD
from .d00_utils.collectdata import collect_historical_data

import matplotlib.pyplot as plt
import pandas as pd
import robin_stocks.robinhood as rh

# ticker_list = ['DOGE']
ticker_list = ['PENN', 'DOGE']


def graph_crypto(ticker_list, interval='hour', span='week', bounds='24_7'):
    login = rh.login(EMAIL, PASSWORD)

    for ticker in ticker_list:
        hist_df = collect_historical_data(ticker, interval, span, bounds)

        if hist_df.empty:
            print(f"Warning: Unable to process request for {ticker}.")
            continue

        name = rh.get_crypto_info(ticker, info='name')

        hist_df['begins_at'] = pd.to_datetime(
            hist_df['begins_at'], infer_datetime_format=True)
        hist_df['open_price'] = hist_df['open_price'].astype('float32')
        hist_df['close_price'] = hist_df['close_price'].astype('float32')
        hist_df['high_price'] = hist_df['high_price'].astype('float32')
        hist_df['low_price'] = hist_df['low_price'].astype('float32')

        plt.close("all")

        ax = hist_df.plot(x='begins_at', y='open_price', figsize=(16, 8))
        ax.set_xlabel('Date')
        ax.set_ylabel('Price (USD)')
        ax.legend([ticker])
        ax.set_title(name)

        plt.show()

    return


# graph_crypto(ticker_list, 'day', '5year', '24_7')
