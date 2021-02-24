#!/usr/bin/env python3
# cli.py

from os import name, system

import robin_stocks.robinhood as rh

from cryptobot.constant import PROCESSED_DIR, TRADABLE_CRYPTOS
from cryptobot.d00_utils.tradecrypto import *
from cryptobot.d01_data.load_save_data import load_json_data
from cryptobot.ordercrypto import OrderCrypto


def fill_out_order(oc):
    if oc.set_order_attr():
        oc.order_summary()

        if oc.confirm_order():
            order_confirmation = place_crypto_order(oc)
            print(order_confirmation)
        else:
            print("Failed to place order.\n")

    return menu_crypto_trading()


def validate_menu_selection(msg, menu_items=0):
    while True:
        try:
            command = input(msg)[0]

            if command.isdigit():
                command = int(command)

                if command <= menu_items:
                    return command

            print("Invalid selection! Try again.")

        except IndexError:
            print("Invalid selection! Try again.")

        except EOFError:
            return 0


def menu_crypto_trading():
    print(
        "****** Crypto Trading Menu ******",
        "0 - QUIT",
        "1 - LIST ALL TRADABLE CRYPTO",
        "2 - BUY CRYPTO",
        "3 - SELL CRYPTO",
        "4 - VIEW ORDERS",
        "5 - CANCEL ORDERS",
        sep="\n",
        end="\n\n"
    )

    switcher = {
        0: quit_cryptobot,
        1: list_tradable_crypto,
        2: menu_buy_crypto,
        3: menu_sell_crypto,
        4: menu_view_crypto_orders,
        5: menu_cancel_crypto_orders
    }

    command = validate_menu_selection("Selection: ", menu_items=5)

    return switcher[command]()


# DO I NEED THIS?
def list_tradable_crypto():
    print("****** Tradable Cryptos ******",
          load_json_data(PROCESSED_DIR, TRADABLE_CRYPTOS),
          "\n0 - RETURN TO MAIN MENU",
          sep="\n",
          end="\n\n"
          )

    return menu_crypto_trading()


def menu_buy_crypto():
    print(
        "****** Buy Crypto Menu ******",
        "0 - RETURN TO MAIN MENU",
        "1 - MARKET ORDER: SPECIFY AMOUNT IN DOLLARS",
        "2 - MARKET ORDER: SPECIFY AMOUNT IN SHARES",
        "3 - LIMIT ORDER: SPECIFY AMOUNT IN DOLLARS",
        "4 - LIMIT ORDER: SPECIFY AMOUNT IN SHARES",
        sep="\n",
        end="\n\n"
    )

    switcher = {
        0: menu_crypto_trading,
        1: {
            "side": "buy",
            "amount_in": "price",
            "limit_price": None,
        },
        2: {
            "side": "buy",
            "amount_in": "quantity",
            "limit_price": None,
        },
        3: {
            "side": "buy",
            "amount_in": "price",
            "limit_price": float,
        },
        4: {
            "side": "buy",
            "amount_in": "quantity",
            "limit_price": float,
        },
    }

    command = validate_menu_selection("Selection: ", menu_items=4)
    menu_item = switcher[command]

    if command == 0:
        return menu_item()
    else:
        oc = OrderCrypto(**menu_item)
        return fill_out_order(oc)


def menu_sell_crypto():
    print(
        "****** Sell Crypto Menu ******",
        "0 - RETURN TO MAIN MENU",
        "1 - MARKET ORDER: SPECIFY AMOUNT IN DOLLARS",
        "2 - MARKET ORDER: SPECIFY AMOUNT IN SHARES",
        "3 - LIMIT ORDER: SPECIFY AMOUNT IN DOLLARS",
        "4 - LIMIT ORDER: SPECIFY AMOUNT IN SHARES",
        sep="\n",
        end="\n\n"
    )

    switcher = {
        0: menu_crypto_trading,
        1: {
            "side": "sell",
            "amount_in": "price",
            "limit_price": None,
        },
        2: {
            "side": "sell",
            "amount_in": "quantity",
            "limit_price": None,
        },
        3: {
            "side": "sell",
            "amount_in": "price",
            "limit_price": float,
        },
        4: {
            "side": "sell",
            "amount_in": "quantity",
            "limit_price": float,
        },
    }

    command = validate_menu_selection("Selection: ", menu_items=4)
    menu_item = switcher[command]

    if command == 0:
        return menu_item()
    else:
        oc = OrderCrypto(**menu_item)
        return fill_out_order(oc)


def menu_view_crypto_orders():
    print(
        "****** View Crypto Orders Menu ******",
        "0 - RETURN TO MAIN MENU",
        "1 - VIEW ALL CRYPTO ORDERS",
        "2 - VIEW ALL OPEN CRYPTO ORDERS",
        "3 - VIEW ALL ORDERS FOR A SPECIFIC CRYPTO",
        "4 - VIEW ALL OPEN ORDERS FOR A SPECIFIC CRYPTO",
        "5 - VIEW DETAILS FOR A SPECIFIC CRYPTO ORDER",
        sep="\n",
        end="\n\n"
    )

    # NEED TO UPDATE
    switcher = {
        0: menu_crypto_trading,
        1: view_all_crypto_orders,
        2: view_all_open_crypto_orders,
        3: view_all_crypto_orders,
        4: view_all_open_crypto_orders,
        5: view_crypto_order_info
    }

    command = validate_menu_selection("Selection: ", menu_items=4)

    return switcher[command]()


def menu_cancel_crypto_orders():
    print(
        "****** Cancel Crypto Orders Menu ******",
        "0 - RETURN TO MAIN MENU",
        "1 - CANCEL ALL CRYPTO ORDERS",
        "2 - CANCEL A SPECIFIC CRYPTO ORDER",
        sep="\n",
        end="\n\n"
    )

    # NEED TO UPDATE
    switcher = {
        0: menu_crypto_trading,
        1: cancel_all_orders,
        2: rh.cancel_crypto_order
    }

    command = validate_menu_selection("Selection: ", menu_items=4)

    return switcher[command]()


def quit_cryptobot():
    print("\nQuitting program...\n")
    return


def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


if __name__ == "__main__":
    menu_crypto_trading()
