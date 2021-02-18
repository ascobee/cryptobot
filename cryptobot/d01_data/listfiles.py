#!/usr/bin/env python3
# listfiles.py


import os


def create_list_of_files(dir_name):
    try:
        new_file_name = "list_of_files.txt"
        full_path = dir_name + new_file_name
        files_list = os.listdir(dir_name)
        files_list = [x for x in files_list if ".csv" in x]

        f = open(full_path, "w")
        f.writelines("\n".join(files_list))
        f.close()
        return print(f"Created a list of all data files \'{new_file_name}\'.\n")
    except FileNotFoundError as err:
        return print("Failed to create a list of all data files.\n")
