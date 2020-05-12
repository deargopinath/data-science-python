# Learn to fit a decision tree and compare its accuracy with random forest classifier. 
# Questions:
# 1. Let’s attempt to predict the survival of a horse based on various observed 
#   medical conditions. Load the data from ‘horses.csv’ and observe whether it
#   contains missing values.
#   [Hint: Pandas dataframe has a method isnull]
# 2. This dataset contains many categorical features, replace them with label encoding.
#   [Hint: Refer to get_dummies methods in pandas dataframe or Label encoder in scikit-learn]
# 3. Replace the missing values by the most frequent value in each column.
#   [Hint: Refer to Imputer class in Scikit learn preprocessing module]
# 4. Fit a decision tree classifier and observe the accuracy.
# 5. Fit a random forest classifier and observe the accuracy.

import pandas as pd
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import Imputer
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
import warnings
warnings.filterwarnings(action='ignore', category=DeprecationWarning)

animals = pd.read_csv("horse.csv")
target = animals['outcome']
target.unique()
animals =animals.drop(['outcome'],axis=1)
category_variables = ['surgery', 'age', 'temp_of_extremities','peripheral_pulse',
       'mucous_membrane', 'capillary_refill_time', 'pain', 'peristalsis',
       'abdominal_distention', 'nasogastric_tube', 'nasogastric_reflux', 'rectal_exam_feces', 'abdomen',
      'abdomo_appearance', 'surgical_lesion','cp_data']

for category in category_variables:
    animals[category] = pd.get_dummies(animals[category])
    
X, y = animals.values,target.values
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
imp = Imputer(missing_values="NaN",strategy="most_frequent",axis =0)
X_train = imp.fit_transform(X_train)
X_test = imp.fit_transform(X_test)
classifier = DecisionTreeClassifier()
classifier.fit(X_train,y_train)
y_predict = classifier.predict(X_test)
accuracy = accuracy_score(y_predict,y_test)
print("Accuracy of Decision Tree Classifier = ", accuracy)
classifier = RandomForestClassifier(n_estimators=100)
classifier.fit(X_train,y_train)
y_predict = classifier.predict(X_test)
accuracy = accuracy_score(y_predict,y_test)
print("Accuracy of Random Forest Classifier = ", accuracy)