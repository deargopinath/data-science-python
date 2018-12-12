# 12. Please write a program which count and print the numbers of each character in a string input by console.
# Example: 
#     If the following string is given as input to the program:    abcdefgabc
#     Then, the output of the program should be:
#       a,2
#       c,2
#       b,2
#       e,1
#       d,1
#       g,1
#       f,1

userInput = (input("Enter a string: "))
characterCounter = {}
for character in userInput:
    if(character.isalpha()):
        if(not character in characterCounter):
            characterCounter[character] = 1
        else:
            count = int(characterCounter[character])
            count += 1
            characterCounter[character] = count

for character, count in characterCounter.items():
  print(character, ',', count)
