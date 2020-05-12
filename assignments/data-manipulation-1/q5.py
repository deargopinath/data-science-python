# 5. Perform Operations on Files
#    5.1: From the raw data below create a data frame 'first_name': 
#               ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
#               'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
#               'age': [42, 52, 36, 24, 73],
#               'preTestScore': [4, 24, 31, ".", "."],
#               'postTestScore': ["25,000", "94,000", 57, 62, 70]
#    5.2: Save the dataframe into a csv file as example.csv
#    5.3: Read the example.csv and print the data frame
#    5.4: Read the example.csv without column heading
#    5.5: Read the example.csv and make the index columns as 'First Name’ and 'Last Name'
#    5.6: Print the data frame in a Boolean form as True or False.
#         True for Null/ NaN values and false for non-null values
#    5.7: Read the dataframe by skipping first 3 rows and print the data frame
#    5.8: Load a csv file while interpreting "," in strings around numbers as thousands seperators. 
#               Check the raw data 'postTestScore' column has, as thousands separator.
#               Comma should be ignored while reading the data.
#               It is default behaviour, but you need to give argument to read_csv function which makes sure commas are ignored.

import pandas as pd
# 5.1
raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
print(df)

# 5.2
df.to_csv('example.csv')

# 5.3
df = pd.read_csv('example.csv')
print(df)

# 5.4
df = pd.read_csv('example.csv', header=None)
print(df)

# 5.5
df = pd.read_csv('example.csv', index_col=['First Name', 'Last Name'], 
                 names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
print(df)

# 5.6
df = pd.read_csv('example.csv', na_values=['.'])
print(pd.isnull(df))

# 5.7
df = pd.read_csv('example.csv', skiprows=3)
print(df)

# 5.8
df = pd.read_csv('example.csv',  thousands=',')
print(df)
