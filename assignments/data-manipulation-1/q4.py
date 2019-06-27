# 4. Is there any correspondence between the critics’ evaluation of a movie and its acceptance by the public? 

import matplotlib.pyplot as plt, pandas
frame = pandas.read_csv('HollywoodMovies.csv', delimiter=',')
selected = frame.loc[:, ["Profitability", "RottenTomatoes"]]
plt.scatter(selected["Profitability"], selected["RottenTomatoes"])
plt.xlim(0, 200)
plt.show()
