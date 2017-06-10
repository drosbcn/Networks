#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:22:18 2017

@author: davidrosenfeld
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

path = "~/Documents/networks/"

input_output = pd.read_csv(path + "ICIO2016_2011.csv")

input_output.tail(5)

input_output = input_output.iloc[0:2414, 0:2415]

sum(input_output.iloc[:,0] != input_output.columns[1:2415])

input_output.index = input_output.iloc[:,0]

input_output["country"] = input_output.index.str[0:3]
input_output["sector"] = input_output.index.str[4:]
input_output = input_output.reset_index(drop = True)
input_output.country[2278:] = "CHN"
input_output.country[2176:2278] = "MEX"

del input_output["Unnamed: 0"]
input_output = input_output.groupby(["country", "sector"]).sum()

input_output = input_output.transpose()
input_output["country"] = input_output.index.str[0:3]
input_output["sector"] = input_output.index.str[4:]
input_output = input_output.reset_index(drop = True)
input_output.country = input_output.country.replace(["MX1", "MX2", "MX3"],
                                                    ["MEX", "MEX", "MEX"])
input_output.country = input_output.country.replace(["CN1", "CN2", "CN3", "CN4"],
                                                    ["CHN", "CHN", "CHN", "CHN"])

input_output = input_output.groupby(["country", "sector"]).sum()

input_output = input_output.transpose()
input_output.to_csv(path + "input_output.csv", index = True)

imported_table = pd.read_csv(path + "input_output.csv", index_col = [0,1],
                             header = [0,1])
