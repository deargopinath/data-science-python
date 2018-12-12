#  Business challenge/requirement
#  LifeTel Telecom is the latest entrant in the highly competitive Telecom market ...
#
#  Key issues
#  Build a system where when user enters Reference ID it is encrypted, so that hackers 
#  cannot view the mapping of Reference ID and finger print
#
#  Approach to Solve
#  You have to use fundamentals of Python taught in module
#     1. Read the input from command line - Reference ID
#     2. Check for validity – it should be 12 digits and allows on number and alphabet
#     3. Encrypt the Reference ID and print it for reference
#
#  Enhancements for code
#  You can try these enhancements in code
#     1. Allow some special characters in ReferenceID
#     2. Give the option for decryption to user

from cryptography.fernet import Fernet
import re

referenceID = input("Enter ReferenceID: ")
pattern = re.compile('^[a-zA-Z0-9]{12}$')
if(pattern.search(referenceID)):
    secretKey = Fernet.generate_key()
    cipher = Fernet(secretKey)
    encryptedID = cipher.encrypt(str.encode(referenceID))
    print("Encrypted Reference ID = ", encryptedID.decode())
    decryptedText = cipher.decrypt(encryptedID)
    print("Decrypted ID = ", decryptedText.decode())
else:
    print("Failed validation: Reference ID must have exactly 12 characters only")