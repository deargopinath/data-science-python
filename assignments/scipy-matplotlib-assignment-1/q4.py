# 4. Let the x axis data points and y axis data points are
#    X = [1,2,3,4]
#    y = [20, 21, 20.5, 20.8]
#
#    4.1: Draw a Simple plot
#    4.2: Configure the line and markers in simple plot
#    4.3: configure the axes
#    4.4: Give title of Graph & labels of x axis and y axis
#    4.5: Give error bar if y_error = [0.12, 0.13, 0.2, 0.1]
#    4.6: define width, height as figsize=(4,5) DPI and adjust plot dpi=100 
#    4.7: Give a font size of 14
#    4.8: Draw a scatter graph of any 50 random values of x and y axis 
#    4.9: Create a dataframe from following data
#         'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
#         'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'], 
#         'female': [0, 1, 1, 0, 1],
#         'age': [42, 52, 36, 24, 73],
#         'preTestScore': [4, 24, 31, 2, 3], 'postTestScore': [25, 94, 57, 62, 70]
#         Draw a Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
#    4.10: Draw a Scatterplot from the data in question 9 of preTestScore and postTestScore with the size = 300 
#          and the color determined by sex

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# 4.1
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
plt.plot(x, y)
plt.show()

# 4.2
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
plt.plot(x, y, linestyle="dashed", marker="o", color="green")
plt.show()

# 4.3
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
plt.plot(x, y, linestyle="dashed", marker="o", color="green")
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])
plt.show()

# 4.4
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
plt.plot(x, y, linestyle="dashed", marker="o", color="green")
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])
plt.xlabel("this is X")
plt.ylabel("this is Y")
plt.title("Simple plot")
plt.show()

# 4.5
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
y_error = [0.12, 0.13, 0.2, 0.1]
plt.plot(x, y, linestyle="dashed", marker="o", color="green")
plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="green")
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])
plt.xlabel("this is X")
plt.ylabel("this is Y")
plt.title("Simple plot")
plt.show()

# 4.6
fig = plt.figure(figsize=(4, 5), dpi=100)
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
y_error = [0.12, 0.13, 0.2, 0.1]
plt.plot(x, y, linestyle="dashed", marker="o", color="green")
plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="green")
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])
plt.xlabel("this is X")
plt.ylabel("this is Y")
plt.title("Simple plot")
plt.subplots_adjust(left=0.18)
plt.show()

# 4.7
fig = plt.figure(figsize=(4, 5), dpi=100)
plt.rc("font", size=14)
x = [1,2,3,4]
y = [20, 21, 20.5, 20.8]
y_error = [0.12, 0.13, 0.2, 0.1]
plt.plot(x, y, linestyle="dashed", marker="o", color="green")
plt.errorbar(x, y, yerr=y_error, linestyle="None", marker="None", color="green")
plt.xlim(0.5,4.5)
plt.xticks([1,2,3,4])
plt.ylim(19.8,21.2)
plt.yticks([20, 21, 20.5, 20.8])
plt.xlabel("this is X")
plt.ylabel("this is Y")
plt.title("Simple plot")
plt.subplots_adjust(left=0.19)
plt.show()

# 4.8
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = np.pi * (15 * np.random.rand(N))**2  # 0 to 15 point radii
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.show()

# 4.9
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])
print(df.head(3))
plt.scatter(df.preTestScore, df.postTestScore, s=df.age)

# 4.10
plt.scatter(df.preTestScore, df.postTestScore, s=300, c=df.female)
