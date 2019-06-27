# 2.Write a code which accepts a sequence of words as input and 
# prints the words in a sequence after sorting them alphabetically.
# Hint: 
# In case of input data being supplied to the question, it should be assumed to be a console input.

inputList = [s for s in input("Enter a list of words:\n").split()]
print("Sorted list is:\n", sorted(inputList))