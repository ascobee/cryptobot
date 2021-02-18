#!/usr/bin/env python3
# load_save_data.py

import pandas as pd


def load_csv_data(dir_name, file_name):
    try:
        full_path = dir_name + file_name
        data_df = pd.read_csv(full_path, sep=" ", index_col=0)

        return data_df
    except FileNotFoundError as err:
        print(f"ERROR: Failed to load \'{file_name}\'\n{err}\n")

        return pd.DataFrame()


# def load_txt_data(dir_name, file_name):
#     try:
#         full_path = dir_name + file_name
#         data_df = pd.read_table(full_path, sep=" ", header=0, names=['file_names'])

#         return data_df
#     except FileNotFoundError as err:
#         print(f"ERROR: Failed to load \'{file_name}\'\n{err}\n")

#         return pd.DataFrame()


def load_txt_data(dir_name, file_name):
    list_of_files = []
    try:
        full_path = dir_name + file_name
        with open(full_path, "r") as f:
            for line in f:
                list_of_files.append(line.strip("\n"))

        return list_of_files
    except FileNotFoundError as err:
        print(f"ERROR: Failed to load \'{file_name}\'\n{err}\n")

        return list_of_files


def save_csv_data(dir_name, file_name, prefix, data_df):
    try:
        new_file_name = prefix + file_name[3:]
        full_path = dir_name + new_file_name

        data_df.to_csv(full_path, sep=" ")

        return print(f"Saved data to \'{new_file_name}\'")
    except FileNotFoundError as err:
        return print(f"ERROR: Failed to save data to \'{new_file_name}\'\n{err}\n")
