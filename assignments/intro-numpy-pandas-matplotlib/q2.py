
# 2. Find: 
#    (i)  The number of men with a PhD
#    (ii) The number of women with a PhD

import numpy as np
import pandas as pd
df = pd.read_csv('SalaryGender.csv', delimiter=',')
salary = np.array(df['Salary'])
gender = np.array(df['Gender'])
phd = np.array(df['PhD'])
age = np.array(df['Age'])
men_count = 0
women_count = 0
for i in range(0, 100):
    if gender[i] == 1 and phd[i] == 1:
        men_count +=1
    if gender[i] == 0 and phd[i] == 1:
        women_count +=1

print(men_count)
print(women_count)
