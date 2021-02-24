#!/usr/bin/env python3
# load_save_data.py

import pandas as pd


def load_csv_data(dir_name, file_name):
    try:
        data_df = pd.read_csv(f"{dir_name}{file_name}", sep=" ", index_col=0)
        return data_df

    except FileNotFoundError as err:
        print(f"Failed to load \'{file_name}\'\n{err}\n")
        return pd.DataFrame()


def load_json_data(dir_name, file_name):
    try:
        data_df = pd.read_json(f"{dir_name}{file_name}")
        return data_df

    except FileNotFoundError as err:
        print(f"Failed to load \'{file_name}\'\n{err}\n")
        return pd.DataFrame()


def load_txt_data(dir_name, file_name):
    list_of_files = []
    try:
        with open(f"{dir_name}{file_name}", "r") as f:
            for line in f:
                list_of_files.append(line.strip("\n"))

        return list_of_files

    except FileNotFoundError as err:
        print(f"Failed to load \'{file_name}\'\n{err}\n")
        return list_of_files


def save_csv_data(dir_name, file_name, prefix, data_df):
    try:
        new_file_name = prefix + file_name[3:]
        data_df.to_csv(f"{dir_name}{new_file_name}", sep=" ")
        print(f"Saved data to \'{new_file_name}\'")
        return

    except FileNotFoundError as err:
        print(f"Failed to save data to \'{new_file_name}\'\n{err}\n")
        return
