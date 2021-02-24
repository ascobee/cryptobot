#!/usr/bin/env python3
# create_int_data.py

import pandas as pd
from cryptobot.constant import INTERMEDIATE_DIR, INTERMEDIATE_PREFIX
from cryptobot.d01_data.listfiles import create_list_of_files
from cryptobot.d01_data.load_save_data import *


def remove_low_variance_features(historical_df):
    if not historical_df.empty:
        single_val_cols = historical_df.columns[historical_df.nunique() <= 2]
        historical_df.drop(single_val_cols, axis=1, inplace=True)
    else:
        print("Warning: DataFrame is empty.\n")

    return historical_df


def clean_all_raw_data_files(dir_name, file_name):
    files_list = load_txt_data(dir_name, file_name)

    for data_file in files_list:
        raw_data_df = load_csv_data(dir_name, data_file)
        clean_df = remove_low_variance_features(raw_data_df)
        save_csv_data(
            INTERMEDIATE_DIR,
            data_file,
            INTERMEDIATE_PREFIX,
            clean_df
        )
    create_list_of_files(INTERMEDIATE_DIR)

    print("Finished.")
    return
