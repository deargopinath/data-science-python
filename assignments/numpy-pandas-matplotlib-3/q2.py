# 2. The dataset given, records data of city temperatures over the years’ 2014 and 2015. 
#    Plot the histogram of the temperatures over this period for the cities of San Francisco and Moscow.

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('CityTemps.csv', delimiter=',')
plt.hist([df["San Francisco"],df["Moscow"]])
plt.show()
