# 15. By using list comprehension, please write a program to 
#     print the list after removing the value 24 in [12,24,35,24,88,120,155].

inputList = [12,24,35,24,88,120,155]
print([element for element in inputList if not element == 24])