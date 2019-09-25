#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: David Burkett
# Date: 09/25/2019

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime

def df_builder():
    """
    Takes a CSV file and converts the data within to a Pandas DataFrame.

    Returns a Pandas DataFrame
    """

    temp_df = pd.read_csv('~/Dev/Python/heat-wave-tracker/Data/1893-2019_chas_tmp_data.csv', 
                            names=["DATE", "TAVG", "TMAX", "TMIN"],
                            header=None,
                            sep=',',
                            parse_dates= True,
                            infer_datetime_format=True,
                            index_col= 'DATE')

    return temp_df

def main():

    temp_data = df_builder()
    #print(temp_data.TMAX.resample('Y').mean())

    sns.set(style='darkgrid')
    sns.jointplot(data=temp_data,
                  x=temp_data.index, 
                  y=temp_data.TMAX.resample('Y').mean())
    plt.show()

if __name__ == "__main__":
    main()