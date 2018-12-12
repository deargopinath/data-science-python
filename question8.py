""" 
8.  A website requires a user to input username and password to register. 
    Write a program to check the validity of password given by user. 
    Following are the criteria for checking password:
        1. At least 1 letter between [a-z]
        2. At least 1 number between [0-9]
        3. At least 1 letter between [A-Z]
        4. At least 1 character from [$#@]
        5. Minimum length of transaction password: 6
        6. Maximum length of transaction password: 12
    Hint: In case of input data being supplied to the question, it should be assumed to be a console input. 
"""
import getpass
import re

def isPasswordValid(password):
    if((len(password) < 6) or (len(password) > 12)):
        print("Failed validation: Password length must be between 6 and 12 characters")
        return False

    pattern = re.compile('[a-z]')
    if(not pattern.search(password)):
        print("Failed validation: Password must contain at least 1 letter between [a-z]")
        return False   

    pattern = re.compile('[A-z]')
    if(not pattern.search(password)):
        print("Failed validation: Password must contain at least one SMALL letter")
        return False   

    pattern = re.compile('[A-Z]')
    if(not pattern.search(password)):
        print("Failed validation: Password must contain at least one CAPITAL letter")
        return False   

    pattern = re.compile('[0-9]')
    if(not pattern.search(password)):
        print("Failed validation: Password must contain at least one DIGIT")
        return False   

    pattern = re.compile('[$#@]')
    if(not pattern.search(password)):
        print("Failed validation: Password must contain $ or # or @")
        return False

    print("Success: Password is valid")
    return True

password = getpass.getpass("Enter a password: ")
isPasswordValid(password)









