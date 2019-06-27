#   11. Please write a program which accepts a string from console and print it in reverse order.
#
#   Example: 
#     If the following string is given as input to the program:  rise to vote sir
#     Then, the output of the program should be:                 ris etov ot esir

userInput = str(input("Enter a string: "))
i = (len(userInput) - 1)
while (i >= 0):
    print(userInput[i], end='')
    i -= 1
print()