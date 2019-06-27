#  9. Write a for loop that prints all elements of a list and their position in the list.
#     a = [4,7,3,2,5,9]
#     Hint: Use Loop to iterate through list elements.

inputList = [s for s in input("Enter a list of words:\n").split()]
position = 1
for element in inputList:
    print ("Element : ", element, " , Position : ", position)
    position += 1
