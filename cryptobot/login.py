#!/usr/bin/env python3
# login.py

import robin_stocks.robinhood as rh
from ..conf.secrets import EMAIL, PASSWORD
# import pathlib


login = rh.login(EMAIL, PASSWORD)

# test_path = pathlib.Path(__file__).parent.absolute()

# print(test_path)
