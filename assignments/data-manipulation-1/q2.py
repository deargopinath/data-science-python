# 2. Find the genre in which there has been the greatest number of movie releases

import pandas
frame = pandas.read_csv('HollywoodMovies.csv', delimiter=',')
genre = frame.loc[:, ["Genre"]]
frequency = dict()
for i in range(0, 970):
    if genre.loc[i][0] in frequency:
        frequency[str(genre.loc[i][0])] += 1
    else:
        frequency[str(genre.loc[i][0])] = 1
print(frequency)

