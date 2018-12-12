# 1. Write a program to find out the probability for:
#     • Drawing a heart or drawing a club
#     • Drawing an ace, a king or a queen

deck = {
    "size": 52, 
    "symbols": {"SPADE": 13, "CLUB": 13, "HEART": 13, "DIAMOND": 13},
    "values": {"A": 4, "2": 4, "3": 4, "4": 4, "5": 4, "6": 4, "7": 7, "8": 8, "9": 9, "10": 10, "J": 4, "Q": 4, "K": 4},
    "colours": {"RED": 26, "BLACK": 26}
}

heart = deck['symbols']['HEART'] / deck['size']
print("Probability of HEART = ", heart)

club = deck['symbols']['CLUB'] / deck['size']
print("Probability of CLUB = ", club)

print("Probability of HEART OR CLUB = ", (heart + club))

ace = deck['values']['A'] / deck['size']
print("Probability of ACE = ", round(ace, 2))

king = deck['values']['K'] / deck['size']
print("Probability of KING = ", round(king, 2))

queen = deck['values']['Q'] / deck['size']
print("Probability of QUEEN = ", round(queen, 2))

print("Probability of ACE OR KING OR QUEEN = ", round((ace + king + queen), 2))
