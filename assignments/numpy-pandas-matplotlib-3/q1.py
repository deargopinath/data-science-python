# 1. You are given a dataset, which is present in the LMS, containing the number of hurricanes occurring 
#    in the United States along the coast of the Atlantic. 
#    Load the data from the dataset into your program and plot a Bar Graph of the data, 
#    taking the Year as the x-axis and the number of hurricanes occurring as the Y-axis.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('Hurricanes.csv', delimiter=',')
print(df)
plt.bar(df["Year"], df["Hurricanes"])
plt.show()
