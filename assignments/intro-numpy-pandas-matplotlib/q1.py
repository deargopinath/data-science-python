# 1. Extract data from the given SalaryGender CSV file and 
#   store the data from each column in a separate NumPy array
import numpy as np
import pandas as pd
df = pd.read_csv('SalaryGender.csv', delimiter=',')
salary = np.array(df['Salary'])
gender = np.array(df['Gender'])
phd = np.array(df['PhD'])
age = np.array(df['Age'])
print(df)
