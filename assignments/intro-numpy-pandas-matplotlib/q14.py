# 14. Create a random matrix and Compute a matrix rank.
import numpy as np
import pandas as pd
A = np.random.uniform(0,1,(10,10))
X, Y, Z = np.linalg.svd(A)
rank = np.sum(Z > 1e-10)
print(rank)
