# 14.
# Write a program that accepts a sentence and calculate the  and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9

sentence = input("Enter the sentence:\n")
upperCase = 0
lowerCase = 0
for word in sentence:
    if word.isupper():
        upperCase += 1
    elif word.islower():
        lowerCase += 1

print ("UPPER CASE", upperCase)
print ("LOWER CASE", lowerCase)