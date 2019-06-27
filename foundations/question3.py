# 3.Write a program, which will find all the numbers between 1000 and 3000 (both included) 
# such that each digit of a number is an even number. 
# The numbers obtained should be printed in a comma separated sequence on a single line.
# Hint: 
# In case of input data being supplied to the question, it should be assumed to be a console input.
# Divide each digit with 2 and verify is it even or not.

evenDigitNumbers = list()

for n in range(1000, 3001):
    thousands = int(n/1000)%10
    hundreds = int(n/100)%10
    tens = int(n/10)%10
    units = n%10
    if((thousands % 2) != 0):
        n += 1000
        continue
    if((hundreds % 2) != 0):
        n += 100
        continue
    if((tens % 2) != 0):
        n += 10
        continue
    if((units % 2) != 0):
        continue
    evenDigitNumbers.append(n)
print (evenDigitNumbers)
