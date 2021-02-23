#!/usr/bin/env python3
# login.py

import robin_stocks as r
from ..conf.secrets import EMAIL, PASSWORD
# import pathlib


login = r.login(EMAIL, PASSWORD)

# test_path = pathlib.Path(__file__).parent.absolute()

# print(test_path)
