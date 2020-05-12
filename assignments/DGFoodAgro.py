# New DG Food Agro are a multinational exporter of various grains from India since nearly 130 years. 
# But their main product of exporting since early 1980s has been Wheat. 
# They export wheat to countries like America, Afghanistan, Australia etc. 
# They started seeing varying exports of sales year on year for various countries. 
# The reason that was theorized by them had a lot of natural causes like floods, country growth, population explosion etc. 
# Now they need to decide which countries fall in the same range of export and which don’t. 
# They also need to know which countries export is low and can be improved and which countries are performing very well across the years.
# The data provided right now is across 18 years. 
# What they need is a repeatable solution which won’t get affected no matter how much data is added across time and that they should 
# be able to explain the data across years in less number of variables. 

# Objective: Our objective is to cluster the countries based on various sales data provided to us across years. 
# We have to apply an unsupervised learning technique like K means or Hierarchical clustering so as to get the final solution. 
# But before that we have to bring the exports (in tons) of all countries down to same scale across years. Plus, as this solution needs 
# to be repeatable we will have to do PCA so as to get the principal components which explain max variance. 
# Implementation:
# 1) Read the data file and check for any missing values
# 2) Change the headers to country and year accordingly.
# 3) Cleanse the data if required and remove null or blank values
# 4) After the EDA part is done, try to think which algorithm should be applied here.
# 5) As we need to make this across years we need to apply PCA first.
# 6) Apply PCA on the dataset and find the number of principal components which explain nearly all the variance.
# 7) Plot elbow chart or scree plot to find out optimal number of clusters. 
# 8) Then try to apply K means, Hierarchical clustering and showcase the results.  
# 9) You can either choose to group the countries based on years of data or using the principal components.
# 10) Then see which countries are consistent and which are largest importers of the good based on scale and position of cluster.

import os
import pandas as pd

# FMCG  Dimensionality Reduction and Clustering for Exploratory Data Analysis
# Getting and preparing data

inputDataFile = 'Project_Data_1.csv'
# Read the CSV file as a data frame.  

existing_df = pd.read_csv(inputDataFile, index_col = 0, thousands  = ',')
existing_df.index.names = ['country']
existing_df.columns.names = ['year']

# Specified `index_col` to be 0 since we want the country names to be the row labels. 
# Specified the `thousands` separator to be ',' so Pandas automatically parses cells as numbers. 
# We can use `head()` to check the first few lines.  

existing_df.head()

# Dimensionality reduction with PCA
from sklearn.decomposition import PCA
pca = PCA(n_components=2)
pca.fit(existing_df)
existing_2d = pca.transform(existing_df)
existing_df_2d = pd.DataFrame(existing_2d)
existing_df_2d.index = existing_df.index
existing_df_2d.columns = ['PC1','PC2']
existing_df_2d.head()

# See the explained variance ratio as follows.
print(pca.explained_variance_ratio_) 

# First PC explains almost 92% of the variance, while the second one accounts for 6%.
# Now we are ready to plot the lower dimensionality version of our dataset. 
# We just need to call plot on the data frame


ax = existing_df_2d.plot(kind='scatter', x='PC2', y='PC1', figsize=(16,8))
for i, country in enumerate(existing_df.index):
    ax.annotate(country, (existing_df_2d.iloc[i].PC2, existing_df_2d.iloc[i].PC1))

# Create a bubble chart, by setting the point size to a value proportional to the mean value for all the years in that particular country. 
# First we need to add a new column containing the re-scaled mean per country across all the years.       


from sklearn.preprocessing import normalize
existing_df_2d['country_mean'] = pd.Series(existing_df.mean(axis=1), index=existing_df_2d.index)
country_mean_max = existing_df_2d['country_mean'].max()
country_mean_min = existing_df_2d['country_mean'].min()
country_mean_scaled = (existing_df_2d.country_mean-country_mean_min) / country_mean_max
existing_df_2d['country_mean_scaled'] = pd.Series(
    country_mean_scaled, 
    index=existing_df_2d.index)
existing_df_2d.head()

# Now we are ready to plot using this variable size (we will ommit the country names this time since we are not so interested in them).  
existing_df_2d.plot(kind='scatter', x='PC2', y='PC1', s=existing_df_2d['country_mean_scaled']*100, figsize=(16,8))

# Let's do the same with the sum instead of the mean. 
existing_df_2d['country_sum'] = pd.Series(existing_df.sum(axis=1), index=existing_df_2d.index)
country_sum_max = existing_df_2d['country_sum'].max()
country_sum_min = existing_df_2d['country_sum'].min()
country_sum_scaled = (existing_df_2d.country_sum-country_sum_min) / country_sum_max
existing_df_2d['country_sum_scaled'] = pd.Series(
    country_sum_scaled, 
    index=existing_df_2d.index)
existing_df_2d.plot(kind='scatter', x='PC2', y='PC1', s=existing_df_2d['country_sum_scaled']*100, figsize=(16,8))

# And finally let's associate the size with the change between 1990 and 2007. 
# Note that in the scaled version, those values close to zero 
# will make reference to those with negative values in the original non-scaled version, since we are scaling to a [0,1] range.  
existing_df_2d['country_change'] = pd.Series(existing_df['2007']-existing_df['1990'], index=existing_df_2d.index)
country_change_max = existing_df_2d['country_change'].max()
country_change_min = existing_df_2d['country_change'].min()
country_change_scaled = (existing_df_2d.country_change - country_change_min) / country_change_max
existing_df_2d['country_change_scaled'] = pd.Series(
    country_change_scaled, 
    index=existing_df_2d.index)
existing_df_2d[['country_change','country_change_scaled']].head()
existing_df_2d.plot(kind='scatter', x='PC2', y='PC1', s=existing_df_2d['country_change_scaled']*100, figsize=(16,8))

# K-means clustering to group countries based on how similar their situation has been year-by-year. 
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5)
clusters = kmeans.fit(existing_df)

# Store the cluster assignments together with each country in our data frame. The cluster labels are returned in `clusters.labels_`.  
existing_df_2d['cluster'] = pd.Series(clusters.labels_, index=existing_df_2d.index)

# And now we are ready to plot, using the cluster column as color.
import numpy as np
existing_df_2d.plot(
    kind='scatter',
    x='PC2',y='PC1',
    c=existing_df_2d.cluster.astype(np.float), 
    figsize=(16,8))