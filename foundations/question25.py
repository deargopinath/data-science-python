#  2. Write a program to calculate the probability of one ace 
#     and then calculate 
#     the probability of second ace after drawing first ace from the deck of cards.
#     Finally, calculate the probability of both the aces together.

deck = {
    "size": 52, 
    "symbols": {"SPADE": 13, "CLUB": 13, "HEART": 13, "DIAMOND": 13},
    "values": {"A": 4, "2": 4, "3": 4, "4": 4, "5": 4, "6": 4, "7": 7, "8": 8, "9": 9, "10": 10, "J": 4, "Q": 4, "K": 4},
    "colours": {"RED": 26, "BLACK": 26}
}

firstAce = deck['values']['A'] / deck['size']
print("Probability of First ACE = ", round(firstAce, 4))

secondAce = (deck['values']['A'] -1) / (deck['size'] - 1)
print("Probability of Second ACE = ", round(secondAce, 4))

print("Probability of First ACE AND Second ACE = ", round((firstAce * secondAce), 4))
