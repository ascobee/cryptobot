#!/usr/bin/env python3
# ordercrypto.py

from cryptobot.constant import REF_DIR, TRADABLE_CRYPTOS
from cryptobot.d01_data.load_save_data import load_json_data


class _TradeCrypto:

    def __init__(self, side='buy', amount_in='quantity', limit_price=None) -> None:
        self.side = side   # "buy" or "sell"
        self.amount_in = amount_in  # "quantity" or "price"
        self.limit_price = limit_price
        self.time_in_force = "gtc"
        self.jsonify = True


class OrderCrypto(_TradeCrypto):

    def __init__(self, **kwargs) -> None:
        super(OrderCrypto, self).__init__(**kwargs)
        self.symbol = str
        self.quantity_or_price = float
        self._order_type = "Market"
        self._amount_type = str
        self._exp_date = "Good until cancelled"

    def order_summary(self):
        print(
            "****** Order Summary ******",
            f"Crypto: {self.symbol}",
            f"Order Type: {self._order_type} {self.side}",
            f"Amount in {self._amount_type}: {self.quantity_or_price}",
            f"Limit price in USD: {self.limit_price}",
            f"Order Expires: {self._exp_date}",
            sep="\n",
            end="\n\n"
        )

    def confirm_order(self):
        while True:
            try:
                confirmed = input("Continue? (Y/N): ")[0]

                if confirmed.isalpha():
                    confirmed = confirmed.upper()

                    if confirmed == "Y":
                        return True

                    if confirmed == "N":
                        print("Order cancelled.")
                        return False

                print("Invalid value! Try again.")

            except IndexError:
                print("Invalid selection! Try again.")

            except EOFError:
                print("Order cancelled.")
                return False

    def set_order_attr(self):
        crypto_df = load_json_data(REF_DIR, TRADABLE_CRYPTOS)

        while True:
            try:
                ticker = input("Crypto to trade: ")

                if ticker.isalpha():
                    ticker = ticker.upper()

                    if ticker in crypto_df.values:
                        self.symbol = ticker
                        break

                print("Invalid value! Try again.")

            except EOFError:
                print("Order cancelled.")
                return False

        if self.amount_in == 'price':
            self._amount_type = "USD"
        else:
            self._amount_type = self.symbol

        while True:
            try:
                amount = input(
                    f"Amount in {self._amount_type} to {self.side}: ")
                self.quantity_or_price = round(float(amount), 8)
                break

            except ValueError:
                print("Invalid value! Try again.")

            except EOFError:
                print("Order cancelled.")
                return False

        if self.limit_price == float:
            self._order_type = "Limit"

        while self._order_type == "Limit":
            try:
                limit_amount = input("Limit price in USD: ")
                self.limit_price = round(float(limit_amount), 8)
                break

            except ValueError:
                print("Invalid value! Try again.")

            except EOFError:
                print("Order cancelled.")
                return False

        return True
