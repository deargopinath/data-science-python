# 3. Use SalaryGender CSV file. Store the “Age” and “PhD” columns in one DataFrame and 
#   delete the data of all people who don’t have a PhD
import numpy as np
import pandas as pd
df = pd.read_csv('SalaryGender.csv', delimiter=',')
salary = np.array(df['Salary'])
gender = np.array(df['Gender'])
phd = np.array(df['PhD'])
age = np.array(df['Age'])
frame = pd.DataFrame()
frame["Age"] = age
frame["PhD"] = phd
for i in range(0, 100):
    if frame.loc[i]["PhD"] == 0:
        frame = frame.drop(i)

print(frame)
