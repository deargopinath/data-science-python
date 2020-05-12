# 13. Create a random array and swap two rows of an array.
import numpy as np
import pandas as pd
A = np.arange(25).reshape(5,5)
A[[0,1]] = A[[1,0]]
print(A)
