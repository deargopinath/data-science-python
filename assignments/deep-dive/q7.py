# 7.
# Write a program which can compute the factorial of a given numbers. Use recursion to find it. 
# Hint: Suppose the following input is supplied to the program: 8
# Then, the output should be: 40320

def factorial(n):
    if (n == 1):
        return 1
    if (n == 0):
        return 0
    if (n < 0):
        return None
    return n * factorial(n - 1)

n = int(input("Enter a positive integer: "))
print ("Factorial of ", n, " = ", factorial(n))
