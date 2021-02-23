#!/usr/bin/env python3
# __main__.py

from . import constant as const
from .d01_data.listfiles import create_list_of_files
from .d01_data.load_save_data import (load_csv_data,
                                      load_txt_data,
                                      save_csv_data)
from .d02_intermediate.create_int_data import (clean_all_raw_data_files,
                                               remove_low_variance_features)


if __name__ == "__main__":
    # test_file = "d01-BCH-historical.csv"

    # test_df = load_csv_data(RAW_DIR, test_file)

    # slim_df = remove_low_variance_features(test_df)

    # save_csv_data(INTERMEDIATE_DIR, test_file, INTERMEDIATE_PREFIX, slim_df)

    # create_list_of_files(RAW_DIR)

    test_file = "list_of_files.txt"

    clean_all_raw_data_files(const.RAW_DIR, test_file)
