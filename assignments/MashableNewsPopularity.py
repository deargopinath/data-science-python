from mpl_toolkits.mplot3d import Axes3D
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.exceptions import ConvergenceWarning
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, fbeta_score, roc_curve, auc, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn.svm import SVC
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeClassifier
from time import time
import matplotlib.pyplot as pl
import matplotlib.patches as mpatches
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings(action='ignore', category=ConvergenceWarning)

# Define benchmark (1400) for number of shares required to consider an article as popular
shareBenchmark = 1400

# Load data on Mashable News Articles
data = pd.read_csv("OnlineNewsPopularity_small.csv")

# Read the target attribute
popularity_raw = data[data.keys()[-1]]
popularity_raw.describe()
label_encoder = preprocessing.LabelEncoder()
popular_label = pd.Series(label_encoder.fit_transform(popularity_raw>=1500))
features_raw = data.drop(['url', data.keys()[1], data.keys()[-1]], axis=1)

# Set benchmark for popularity
unpop=data[data[' shares'] < shareBenchmark]
pop=data[data[' shares'] >= shareBenchmark]

# See popularity spread across the days of the week
print("Finding popularity by day of release...")
columns_day = features_raw.columns.values[29:36]
unpop_day = unpop[columns_day].sum().values
pop_day = pop[columns_day].sum().values
fig = pl.figure("Popularity by Release Day", figsize = (13, 5))
pl.title("Popularity by Release Day", fontsize = 16)
pl.bar(np.arange(len(columns_day)), pop_day, width = 0.3, align="center", color = 'yellowgreen', label = "Most shared articles")
pl.bar(np.arange(len(columns_day)) - 0.3, unpop_day, width = 0.3, align = "center", color = 'grey', label = "Least shared articles")
pl.xticks(np.arange(len(columns_day)), columns_day)
pl.ylabel("News Articles", fontsize = 14)
pl.xlabel("Days of week", fontsize = 14)
pl.legend(loc = 'upper right')
pl.tight_layout()
pl.savefig("popularity-by-release-day.png")
print("Graph saved to popularity-by-release-day.png")
pl.show()

# See popularity by genre
print("Finding popularity by genre...")
columns_chan = features_raw.columns.values[11:17]
unpop_chan = unpop[columns_chan].sum().values
pop_chan = pop[columns_chan].sum().values
fig = pl.figure("Popularity by Genre", figsize = (13, 5))
pl.title("Popularity by Genre", fontsize = 16)
pl.bar(np.arange(len(columns_chan)), pop_chan, width = 0.3, align="center", color = 'yellowgreen', label = "Most shared articles")
pl.bar(np.arange(len(columns_chan)) - 0.3, unpop_chan, width = 0.3, align = "center", color = 'grey', label = "Least shared articles")
pl.xticks(np.arange(len(columns_chan)), columns_chan)
pl.ylabel("News Articles", fontsize = 14)
pl.xlabel("Genres", fontsize = 14)  
pl.legend(loc = 'upper center')
pl.tight_layout()
pl.savefig("popularity-by-genre.png")
print("Graph saved to popularity-by-genre.png")
pl.show()

# Normalize the numerical features
scaler = MinMaxScaler()
numerical = [' n_tokens_title', ' n_tokens_content', ' num_hrefs', ' num_self_hrefs', 
             ' num_imgs', ' num_videos', ' average_token_length', ' num_keywords', 
             ' self_reference_min_shares', ' self_reference_max_shares', ' self_reference_avg_sharess']
features_raw[numerical] = scaler.fit_transform(data[numerical])

learningModel = RandomForestClassifier(n_estimators=100)
selector = RFECV(learningModel, step=1, cv=5)
selector = selector.fit(features_raw, popular_label)
selector.ranking_

pl.figure("Recursive Feature Elimination - Random Forest")
pl.title("Recursive Feature Elimination - Random Forest", fontsize = 16)
pl.xlabel("# Features selected")
pl.ylabel("# Correct classifications")
pl.plot(range(1, len(selector.grid_scores_) + 1), selector.grid_scores_)
pl.savefig('recursive-feature-elimination.png')
pl.show()

print(features_raw.columns.values[selector.ranking_!=1].shape[0])
print(features_raw.columns.values[selector.ranking_!=1])
randomForestFeatures = features_raw[features_raw.columns.values[selector.ranking_==1]]

# Split data into training and testing sets

xTrain, xTest, yTrain, yTest = train_test_split(randomForestFeatures, popular_label, test_size = 0.1, random_state = 0)
trainingSampleSize = xTrain.shape[0]
testingSampleSize = xTest.shape[0]
print("Samples in Training set = ", trainingSampleSize)
print("Samples in Testing set = ", testingSampleSize)

# Learn from training sample
learningModelName = learningModel.__class__.__name__
start = time()
learningModel.fit(xTrain[:trainingSampleSize], yTrain[:trainingSampleSize])
end = time()
learningTime = end-start

# Make predictions on some samples
# (First 50 articles from given input are considered for testing)
predictionSampleSize = 50
predictions = learningModel.predict(xTrain[:predictionSampleSize])
end = time()
predictionTime = end-start
accuracy = accuracy_score(yTrain[:predictionSampleSize], predictions)
fScore = fbeta_score(yTrain[:predictionSampleSize], predictions, beta=1)
areaUnderCurve = roc_auc_score(yTrain[:predictionSampleSize], predictions)
print(learningModelName, " trained on ", trainingSampleSize, " samples.")
print("Predictions made on ", predictionSampleSize, " samples.")
print("Accuracy = ", accuracy, "\nF-score = ", fScore, "\nAUC = ", areaUnderCurve)
print("Learning time = ", learningTime, "\nPrediction time = ", predictionTime)
print("Predictions on popularity of news articles\n")
print("Atricle #\tWill it become popular?")
print("---------\t-----------------------\n")
count = 1
for p in predictions:
    if (p == 1):
        print(count, "\t\t Yes")
    else:
        print(count, "\t\t No")
    count += 1
