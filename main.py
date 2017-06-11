import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
plt.interactive(False)


#data = pd.read_csv("/home/frank/Dropbox/school/Networks/ICIO2016_2011.csv")
#data2 = pd.read_csv("/home/frank/Dropbox/school/Networks/input_output.csv")

#del data2['country']
input_output = pd.read_csv("input_output.csv", index_col = [0,1], header = [0,1])
source = list(input_output.columns.values)
target = input_output.index

#filter for a subsample



input_output_matrix = input_output.as_matrix()


G = nx.from_numpy_matrix(input_output_matrix)


#G = nx.from_pandas_dataframe(input_output, source =source, target = target)

#G = nx.read_edgelist(path='input_output.csv')

#for row in data2:
#    G.add_nodes_from(row)

nx.draw(G)
plt.show()

print("The end")



