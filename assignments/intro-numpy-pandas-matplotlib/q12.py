# 12. Create a four dimensions array get sum over the last two axis at once. 13.
import numpy as np
import pandas as pd
A = np.random.randint(0,10,(3,4,3,4))
sum = A.reshape(A.shape[:-2] + (-1,)).sum(axis=-1)
print(sum)
