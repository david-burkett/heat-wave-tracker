#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: David Burkett
# Date: 09/25/2019

import pandas as pd
import numpy as np
from datetime import datetime

def df_builder():
    """
    Takes a CSV file and converts the data within to a Pandas DataFrame.

    Returns a Pandas DataFrame
    """

    temp_df = pd.read_csv(path, 
                            names=["DATE", "TMAX", "TMAX_ATTRIBUTES", "TMIN", "TMIN_ATTRIBUTES", "TOBS", "TOBS_ATTRIBUTES"],
                            header=None,
                            sep=',',
                            parse_dates= True,
                            infer_datetime_format=True,
                            index_col= 'DATE')

    return temp_df

def main():

    temperature_data = df_builder()

    print(temperature_data.resample('Y').mean())

if __name__ == "__main__":
    main()