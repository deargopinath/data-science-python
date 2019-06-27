# Business challenge/requirement
# Fyntra is the largest online clothing company in USA. It sells clothing online, but they 
# also have in-store style and clothing advice sessions. 
# Customers come into the store, have sessions/meetings with a personal stylist, 
# then can go home and order either on a mobile app or website for the clothes they want.
# Company wants to decide whether to focus the effort on mobile app experience or its website. 
# As a drastic measure it is also evaluating to shut down the website. 
# You as a ML expert in the team will help the company make the right decision 
#
# 1. Compute -- Use seaborn to create a jointplot to compare the Time on Website 
#    and Yearly Amount Spent columns.  Is there a correlation?
# 2. Compute – Do the same as above but now with Time on App and Yearly Amount Spent. 
#    Is this correlation stronger than 1st One?
# 3. Compute -- Explore types of relationships across the entire data set using pairplot.
#    Based off this plot what looks to be the most correlated feature with Yearly Amount Spent?
# 4. Compute – Create linear model plot of Length of Membership and Yearly Amount Spent. 
#    Does the data fits well in linear plot?
# 5. Compute – Train and Test the data and answer multiple questions --
#    What is the use of random_state=85?
# 6. Compute – Predict the data and do a scatter plot. Check if actual and predicted data match?
# 7. What is the value of Root Mean Squared Error?

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

customers = pd.read_csv("FyntraCustomerData.csv")

sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
sns.jointplot(x='Time_on_Website',y='Yearly_Amount_Spent',data=customers)
plt.show()

sns.jointplot(x='Time_on_App',y='Yearly_Amount_Spent',data=customers)
sns.pairplot(customers)
plt.show()

# Length of Membership 
sns.lmplot(x='Length_of_Membership',y='Yearly_Amount_Spent',data=customers)
plt.show()

# Split data into training and testing subsets
y = customers['Yearly_Amount_Spent']
X = customers[['Avg_Session_Length', 'Time_on_App','Time_on_Website', 'Length_of_Membership']]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)


# Training with Linear Regression Model
lm = LinearRegression()
lm.fit(X_train,y_train)
plt.show()
print('Coefficients: \n', lm.coef_)


# Predictions on test data
predictions = lm.predict( X_test)
plt.scatter(y_test,predictions)
plt.xlabel('Y Test')
plt.ylabel('Predicted Y')
plt.show()

# Check if prediction matches the actual data 
# Find the  Root Mean Squared Error**

print('Root Mean Squared Error = ', round( np.sqrt(metrics.mean_squared_error(y_test, predictions)),2) )

sns.distplot((y_test-predictions),bins=50)
plt.show()
coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
coeffecients
print("More engagement on mobile app leads to more revenue!")
