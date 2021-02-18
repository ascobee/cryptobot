#!/usr/bin/env python3
# create_int_data.py

import pandas as pd

from ..d01_data.listfiles import create_list_of_files
from ..d01_data.load_save_data import load_csv_data, load_txt_data, save_csv_data
# from sklearn.feature_selection import VarianceThreshold
from .. import constant as const

# INTERMEDIATE_DIR = "./data/crypto/02_intermediate/"
# INTERMEDIATE_PREFIX = "d02"


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
            const.INTERMEDIATE_DIR,
            data_file,
            const.INTERMEDIATE_PREFIX,
            clean_df
        )
    create_list_of_files(const.INTERMEDIATE_DIR)

    return print("Finished.")
