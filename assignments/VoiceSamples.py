# Objectives:
#     * Fit a model using binary classification using logistic regression.
#     * Identify correlated variables and form a less complex model.
#
# Questions:
# 1.  We will use acoustic features to distinguish a male voice from female. 
#     Load the dataset from “voice.csv”, identify the target variable and 
#     do a one-hot encoding for the same. 
#     Split the dataset in train-test with 20% of the data kept aside for testing.
#     [Hint: Refer to LabelEncoder documentation in scikit-learn]
#    
# 2.  Fit a logistic regression model and measure the accuracy on the test set.
#     [Hint: Refer to Linear Models section in scikit-learn]
#
# 3.  Compute the correlation matrix that describes the dependence between all 
#     predictors and identify the predictors that are highly correlated.  
#     Plot the correlation matrix using seaborn heatmap.
#     [Hint: Explore dataframe methods to identify appropriate method]
#
# 4.  Based on correlation remove those predictors that are correlated and fit a 
#     logistic regression model again and compare the accuracy with that of previous model.
#     [Hint: Identify correlated variable pairs and remove one among them]

import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

voice = pd.read_csv("voice.csv")
voice.columns
X,y = voice.iloc[:,:-1].values, voice.iloc[:,-1].values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
lr = LogisticRegression(solver="lbfgs", max_iter=500)
lr.fit(X_train,y_train)
y_predict = lr.predict(X_test)
print("Accuracy = ", accuracy_score(y_predict,y_test))
corr_matrix = voice.corr()
print("Correlation Matrix:\n", corr_matrix)
sns.heatmap(corr_matrix, square=True, cmap=plot.cm.RdYlGn)
plot.yticks(rotation=0)
plot.xticks(rotation=90)
plot.title("Heat Map")
plot.show()
print("Removing the most correlated predictors ...")
corr_treshold = 0.9
iters = range(len(corr_matrix.columns) - 1)
drop_cols = []
for i in iters:
    for j in range(i):
        item = corr_matrix.iloc[j:(j+1), (i+1):(i+2)]
        col = item.columns
        row = item.index
        val = item.values
        if abs(val) >= corr_treshold:
            # Prints the correlated feature set and the corr val
            print(col.values[0], "|", row.values[0], "|", round(val[0][0], 2))
            drop_cols.append(i)
drops = sorted(set(drop_cols))[::-1]
# Drop the correlated columns
for i in drops:
    col = voice.iloc[:, (i+1):(i+2)].columns.values
    voice = voice.drop(col, axis=1)
corr_matrix_new = voice.corr()
print("After deleting correlated predictors:\n")
print("New Correlation Matrix:\n", corr_matrix_new)
sns.heatmap(corr_matrix_new, square=True, cmap=plot.cm.RdYlGn)
plot.yticks(rotation=0)
plot.xticks(rotation=90)
plot.title("Heat Map - After removing correlated predictors")
plot.show()
