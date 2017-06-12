#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:22:18 2017

@author: davidrosenfeld
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "~/Documents/networks/ICIO_data/"

def prep_network_data(year):
    # Import data for a year
    input_output = pd.read_csv(path + "ICIO2016_" + str(year) + ".csv")   
    # Select only trade in intermediate inputs
    input_output = input_output.iloc[0:2414, 0:2415]
    # Make the index equal to the first column (which contains country name and sector)
    input_output.index = input_output.iloc[:,0]
    # Delete the first column
    del input_output["Unnamed: 0"]
    # Create 2 new variables: one for country, one for sector
    input_output["country"] = input_output.index.str[0:3]
    input_output["sector"] = input_output.index.str[4:]
    # Reset index
    input_output = input_output.reset_index(drop = True)
    # Replace all cells in country for China with "CHN", and all rows for Mexico with "MEX
    input_output.country = input_output.country.replace(["MX1", "MX2", "MX3"], ["MEX", "MEX", "MEX"])
    input_output.country = input_output.country.replace(["CN1", "CN2", "CN3", "CN4"], ["CHN", "CHN", "CHN", "CHN"])
    # Group by and sum for each country and sector pair
    input_output = input_output.groupby(["country", "sector"]).sum()
    # Transpose the matrix
    input_output = input_output.transpose()
    #Do the same operations all over again 
    input_output["country"] = input_output.index.str[0:3]
    input_output["sector"] = input_output.index.str[4:]
    input_output = input_output.reset_index(drop = True)
    input_output.country = input_output.country.replace(["MX1", "MX2", "MX3"], ["MEX", "MEX", "MEX"])
    input_output.country = input_output.country.replace(["CN1", "CN2", "CN3", "CN4"], ["CHN", "CHN", "CHN", "CHN"])
    input_output = input_output.groupby(["country", "sector"]).sum()
    # Transpose back again so we return to the original matrix shape
    input_output = input_output.transpose()
    # Save under the same name as before
    input_output.to_csv(path + "ICIO2016_" + str(year) + ".csv", index = True)

all_years = list(range(1995, 2012, 1))

for year in all_years:
    prep_network_data(year)


