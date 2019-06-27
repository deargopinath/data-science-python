# 5.Design a code which will find the given number is Palindrome number or not.
# Hint: Use built-in functions of string.

userInput = input("Enter a non-negative integer: ")
if(userInput.isdigit()):
    if(userInput == str(userInput)[::-1]):
        print('Palindrome')
    else:
        print ('Not a palindrome')
else:
    print("Input must be a non-negative integer only")