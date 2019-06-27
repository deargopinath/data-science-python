# 13.
# Write a program which accepts a sequence of comma separated 4 digit binary 
# numbers as its input and then check whether they are divisible by 5 or not.
# The numbers that are divisible by 5 are to be printed in a comma separated sequence.

# Example: 0100,0011,1010,1001
# Then the output should be:
# 1010

value = []
items = [int(x, 2) for x in input("Enter comma separated binary numbers:\n").split(',')]
for p in items:
    if (p % 5 == 0):
        value.append(format(p, 'b'))

print (*value, sep=",")