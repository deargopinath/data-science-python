# 11.
# Write a program that accepts sequence of lines as input and prints the lines after 
# making all characters in the sentence capitalized. 
# Suppose the following input is supplied to the program:
# Hello world 
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD 
# PRACTICE MAKES PERFECT

output = []
print("Enter input sequence of lines: \n")
while True:
    s = input()
    if not s:
        break
    output.append(s.upper())
print (*output, sep="\n")