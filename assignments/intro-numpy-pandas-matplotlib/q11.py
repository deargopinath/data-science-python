# 11. Create a random array of 3 rows and 3 columns and sort it according to 1st column, 2nd column or 3rd column.
import numpy as np
import pandas as pd
x = np.random.randint(0,10,(3,3))
print(x)
print(x[x[:,1].argsort()])
