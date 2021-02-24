#!/usr/bin/env python3
# tradecrypto.py

import pandas as pd
import robin_stocks.robinhood as rh
from conf.secrets import EMAIL, PASSWORD
from cryptobot.constant import REF_DIR
from cryptobot.ordercrypto import OrderCrypto


def place_crypto_order(oc=OrderCrypto):
    login = rh.login(EMAIL, PASSWORD)

    order_dict = rh.order_crypto(
        symbol=oc.symbol,
        side=oc.side,
        quantityOrPrice=oc.quantity_or_price,
        amountIn=oc.amount_in,
        limitPrice=oc.limit_price,
        timeInForce=oc.time_in_force,
        jsonify=oc.jsonify
    )

    return order_dict


# NOT FINISHED
def view_all_crypto_orders():
    login = rh.login(EMAIL, PASSWORD)

    orders_list = rh.get_all_crypto_orders()

    orders_df = pd.DataFrame(orders_list)
    orders_df.to_json(f"{REF_DIR}all-crypto-orders.json")
    return


# NOT FINISHED
def view_all_open_crypto_orders():
    login = rh.login(EMAIL, PASSWORD)

    orders_list = rh.get_all_open_crypto_orders()

    orders_df = pd.DataFrame(orders_list)
    orders_df.to_json(f"{REF_DIR}open-orders.json")
    return


# NOT FINISHED
def view_crypto_order_info(order_id):
    login = rh.login(EMAIL, PASSWORD)

    order_info = rh.get_crypto_order_info(order_id)
    return


# NOT FINISHED
def cancel_all_orders():
    login = rh.login(EMAIL, PASSWORD)

    cancelled_orders_list = rh.cancel_all_crypto_orders()

    cancelled_df = pd.DataFrame(cancelled_orders_list)
    cancelled_df.to_json(f"{REF_DIR}cancelled-orders.json")
    return
