# 1. Write a program to find out the ranks of the students like, first, second and third 
#    if the percentage list of all students is given.
#    Percentage of all students= [87, 76, 88, 95, 94]
#    Hint: Use for loop with if-else statements

scores = sorted([int(x) for x in input("Enter the scores of students: ").split()], reverse=True)
rank = 1
score = scores[0]
for i in range(len(scores)):
    if(not scores[i] == score):
        rank = (i+1)
    score = scores[i]
    print("Score: ", score, ", Rank: ", rank)
