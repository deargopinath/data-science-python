# 3. Create csv file from the data file available in LMS which goes by the name ‘M4_assign_dataset’ 
#    and read this file into a pandas data frame
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sales=pd.read_csv("sample-salesv2.csv",parse_dates=['date'])
print(sales.head())
print(sales['unit price'].describe())
customers = sales[['name','net_price','date']]
customer_group = customers.groupby('name')
print(customer_group.size())
sales_totals = customer_group.sum()
my_plot = sales_totals.plot(kind='bar')
plt.show()
