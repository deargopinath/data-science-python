# 1. Write a program which will find factors of given number and find whether the factor is even or odd.
# Hint: Use Loop with if-else statements

userInput = input("Enter a positive integer: ")
if(userInput.isdigit() and (int(userInput) > 0)):
    n = int(userInput)
    print("The factors of",n,"are:")
    for i in range(1, n + 1):
        if (n % i == 0):
            print(i, {True : 'Even', False : 'Odd'} [i%2 == 0])
else:
    print("Input must be a positive integer only")

