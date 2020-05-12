# 3. Print the names of the top five movies with the costliest budgets.

import pandas
frame = pandas.read_csv('HollywoodMovies.csv', delimiter=',')
sorted_frame = frame.sort_values(by='Budget', ascending=False)
print(sorted_frame.loc[:, "Budget"])
