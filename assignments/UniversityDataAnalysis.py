# Domain – Education focus – Data analysis
#
# Key issues:   Ensure students identify is not revealed shared
# Data volume:  In thousands, but only around 1800 records are shared in files 
#               MathScoreTerm1.csv, DSScoreTerm1.csv, PhysicsScoreTerm1.csv
#
# Approach to Solve
# You have to use fundamentals of Numpy and Pandas covered in module 4.
# 1. Read the three csv files which contains the score of same students in term1 for each Subject
# 2. Remove the name and ethnicity column (to ensure confidentiality)
# 3. Fill missing score data with zero
# 4. Merge the three files
# 5. Change Sex(M/F) Column to 1/2 for further analysis
# 6. Store the data in new file – ScoreFinal.csv
#
# Enhancements for code
# You can try these enhancements in code
# 1. Convert ethnicity to numerical value
# 2. Fill the missing score for a student to the average of the class

import pandas as pd
import numpy as np

# Read 3 input files, without considering name and ethnicity
mathematics = pd.read_csv("MathScoreTerm1.csv", usecols = ["ID", "Age", "Sex", "Score"], index_col = "ID")
dataStructures = pd.read_csv("DSScoreTerm1.csv", usecols = ["ID", "Score"], index_col = "ID")
physics = pd.read_csv("PhysicsScoreTerm1.csv", usecols = ["ID", "Score"], index_col = "ID")

# Prepare aggregate score sheet
allSubjects = pd.merge(pd.merge(mathematics, physics, how = "inner", on="ID"),
                       dataStructures, how = "inner", on="ID")
allSubjects.columns = ["Mathematics", "Age", "Sex", "Physics", "Data Structures"]
allSubjects = allSubjects[["Age", "Sex", "Mathematics", "Physics", "Data Structures"]]

# Fill Missing Scores with 0
allSubjects['Mathematics'] = allSubjects['Mathematics'].fillna(0)
allSubjects['Physics'] = allSubjects['Physics'].fillna(0)
allSubjects['Data Structures'] = allSubjects['Data Structures'].fillna(0)

# Map gender to numeric values M = 1, F = 2
allSubjects['Sex'] = allSubjects['Sex'].map({'M': 1, 'F': 2}).astype(int)

# Export final score sheet to file
allSubjects.to_csv("ScoreFinal.csv", header=True)
print (allSubjects.to_string())
