# 10. Create numpy array having elements 0 to 10 And negate all the elements between 3 and 9
import numpy as np
import pandas as pd
x = np.arange(11)
x[(3 < x) & (x <= 8)] *= -1
print(x)
