# 19. Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).
#     
#     Example:
#     If the following n is given as input to the program:  5
#     Then, the output of the program should be:  3.55

userInput = input("Enter a positive integer: ")
if(userInput.isdigit() and (int(userInput) > 0)):
    n = int(userInput)
    result = 0.5
    resultBanner = str("1/2")
    for i in range(2, n + 1):
        result += (i/(i+1))
        resultBanner += (" + " + str(i) + "/" + str(i+1))
    print(resultBanner, " = ", result)
else:
    print("Input must be a positive integer only")

