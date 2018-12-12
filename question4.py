# 4.Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose if the entered string is: Python0325
# Then the output will be:
# LETTERS: 6
# DIGITS:4
# Hint: Use built-in functions of string.

userInput = str(input("Enter a Sentence: \n"))
letters = 0
digits = 0

for character in userInput:
    if (character.isdigit()):
        digits += 1
        continue
    if(character.isalpha()):
        letters += 1
        continue
print ("LETTERS: ", letters, "\nDIGITS: ", digits)
