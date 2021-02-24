#!/usr/bin/env python3
# listfiles.py

from os import listdir
from cryptobot.constant import LIST_OF_FILES


def create_list_of_files(dir_name):
    try:
        files_list = listdir(dir_name)
        files_list = [x for x in files_list if ".csv" in x]

        f = open(f"{dir_name}{LIST_OF_FILES}", "w")
        f.writelines("\n".join(files_list))
        f.close()

        print(f"List of all data files saved in \'{LIST_OF_FILES}\'.\n")
        return

    except FileNotFoundError as err:
        print("Failed to create list of all data files.\n")
        return
