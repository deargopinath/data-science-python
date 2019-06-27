# From the data provided on Hollywood movies:
# 1. Find the highest rated movie in the “Quest” story type.

import pandas
frame = pandas.read_csv('HollywoodMovies.csv', delimiter=',')
selected_columns = frame.loc[:, ["Movie", "RottenTomatoes", "Story"]]
highest_rated = ""
rating = 0
for i in range(0, 970):
    if selected_columns.loc[i]["Story"] == "Quest" and selected_columns.loc[i]["RottenTomatoes"] > rating:
        rating = selected_columns.loc[i]["RottenTomatoes"]
        highest_rated = selected_columns.loc[i]["Movie"]
print(highest_rated, rating)
