# 6. Perform Operations on Files
#    6.1: From the raw data below create a Pandas Series 'Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'
#       a) Print all elements in lower case
#       b) Print all the elements in upper case c) Print the length of all the elements
#    6.2: From the raw data below create a Pandas Series
#       ' Atul', 'John ', ' jack ', 'Sam'
#       a) Print all elements after stripping spaces from the left and right 
#       b) Print all the elements after removing spaces from the left only 
#       c) Print all the elements after removing spaces from the right only
#    6.3: Create a series from the raw data below
#       'India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'
#       a) split the individual strings wherever ‘_’ comes and create a list out of it.
#       b) Access the individual element of a list
#       c) Expand the elements so that all individual elements get splitted by ‘_’ 
#          and insted of list returns individual elements
#    6.4: Create a series and replace either X or dog with XX-XX 
#         'A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'
#    6.5: Create a series and remove dollar from the numeric values '12', '-$10', '$10,000'
#    6.6: Create a series and reverse all lower case words 'india 1998', 'big country', np.nan
#    6.7: Create pandas series and print true if value is alphanumeric in series 
#         or false if value is not alpha numeric in series.
#         '1', '2', '1a', '2b', '2003c'
#    6.8: Create pandas series and print true if value is containing 
#         ‘A’ '1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c'
#    6.9: Create pandas series and print in three columns 
#         value 0 or 1 is a or b or c exists in values 'a', 'a|b', np.nan, 'a|c'
#    6.10: Create pandas dataframe having keys and ltable and rtable as below -
#          'key': ['One', 'Two'], 'ltable': [1, 2] 'key': ['One', 'Two'], 'rtable': [4, 5]
#          Merge both the tables based of key

import pandas as pd
import numpy as np


# 6.1
s = pd.Series(['Amit', 'Bob', 'Kate', 'A', 'b', np.nan, 'Car', 'dog', 'cat'])
print(s.str.lower())
print(s.str.upper())
print(s.str.len())

# 6.2
s = pd.Index([' Atul', 'John ', ' jack ', 'Sam'])
print(s.str.strip())
print(s.str.lstrip())
print(s.str.rstrip())

# 6.3
s = pd.Series(['India_is_big', 'Population_is_huge', np.nan, 'Has_diverse_culture'])
print(s.str.split('_'))
print(s.str.split('_').str.get(1))
print(s.str.split('_', expand=True))

# 6.4
s = pd.Series(['A', 'B', 'C', 'AabX', 'BacX','', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.replace('^.a|dog', 'XX-XX ', case=False))

# 6.5:
d = pd.Series(['12', '-$10', '$10,000'])
print(d.str.replace('$', ''))

# 6.6
pattern = r'[a-z]+'
replacement = lambda m: m.group(0)[::-1]
s=pd.Series(['india 1998', 'big country', np.nan]).str.replace(pattern, replacement)
print(s)

# 6.7
pattern = r'[0-9][a-z]'
print(pd.Series(['1', '2', '1a', '2b', '2003c']).str.contains(pattern))

# 6.8
pattern = r'[0-9][a-z]'
print(pd.Series(['1', '2', '1a', '2b', 'America', 'VietnAm','vietnam', '2003c']).str.contains('A', na=False))

# 6.9
s = pd.Series(['a', 'a|b', np.nan, 'a|c'])
print(s.str.get_dummies(sep='|'))

# 6.10
left = pd.DataFrame({'key': ['One', 'Two'], 'ltable': [1, 2]})
right = pd.DataFrame({'key': ['One', 'Two'], 'rtable': [4, 5]})
new=pd.merge(left, right, on='key')
print(new)
