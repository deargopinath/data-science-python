# 1.Provide the learner some more practice for exploratory data analysis. 2.Equip the learner to fit and evaluate a linear regression model.
# Questions:
#   1.Load the data from “cereal.csv” and plot histograms of sugar and vitamin content across different cereals.
#     [Hint: Extract values of a specific column using their labels and use hist method of pyplot]
#
#   2. The names of the manufactures are coded using alphabets, 
#      create a new column with their full name using the below mapping.
#       'N': 'Nabisco',
#       'Q': 'Quaker Oats',
#       'K': 'Kelloggs',
#       'R': 'Raslston Purina',
#       'G': 'General Mills' ,
#       'P' :'Post' ,
#       'A':'American Home Foods Products'
#     Create a bar plot where each manufacturer is on the y axis and 
#     the height of the bars depict the number of cereals manufactured by them.
#     [Hint: Try using countplot this time or bar method of pyplot]
#
#   3. Extract the rating as your target variable ‘y’ and all numerical parameters as your predictors ‘x’. 
#      Separate 25% of your data as test set.
#
#   4. Fit a linear regression module and measure the mean squared error on test dataset.
#     [Hint: Explore linear models and metrics section of sklearn documentation]

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# read in the data set
cereals = pd.read_csv("cereal.csv")

# 1
sugar = cereals["sugars"]
plt.hist(sugar)
plt.title("Sugar in Breakfast Cereal products")
plt.xlabel("Breakfast Cereal Products")
plt.ylabel("Sugar content")
plt.show()

vitamins = cereals["vitamins"]
plt.hist(vitamins)
plt.title("Vitamins in Breakfast Cereal products")
plt.xlabel("Breakfast Cereal Products")
plt.ylabel("Vitamin content")
plt.show()

# 2
values_dict = {'N': 'Nabisco', 'Q': 'Quaker Oats', 'K': 'Kelloggs', 'R': 'Raslston Purina', 'G': 'General Mills' , 'P' :'Post' , 'A':'American Home Foods Products'}
cereals['mfr_name'] = cereals['mfr'].map(values_dict)
sns.countplot(y = 'mfr_name' , hue = 'type' , data=cereals , palette ='cool')
plt.title("Breakfast Cereal Products")
plt.xlabel("Number of products")
plt.show()

# 3
df = cereals.iloc[:,3:-1]
dataset = df.to_numpy()
dataset.shape
x= dataset[:,:-1]
y= dataset[:,-1]
x.shape
y.shape
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25,random_state=10)
print ("Training set: ", X_train.shape)
print ("Testing set: ", X_test.shape)

# 4
lr = LinearRegression()
lr.fit(X_train,y_train)
lr.score(X_test,y_test)
y_predict = lr.predict(X_test)
y_predict - y_test
print ("Mean Squared Error (MSE) = ", mean_squared_error(y_test,y_predict))
