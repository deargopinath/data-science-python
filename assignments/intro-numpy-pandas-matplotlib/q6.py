# 6. Create a numpy array [[0, 1, 2], [ 3, 4, 5], [ 6, 7, 8],[ 9, 10, 11]]) and 
#    filter the elements greater than 5.

import numpy as np
import pandas as pd
x = np.array([[ 0,  1,  2],[ 3,  4,  5],[ 6,  7,  8],[ 9, 10, 11]])
print('Our array is:' )
print(x)
print('\n')
print('The items greater than 5 are:')
print(x[x > 5])
