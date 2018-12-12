#  18. Please write a program to randomly generate a list with 5 numbers, which are
#      divisible by 5 and 7 , between 1 and 1000 inclusive.

import random
print(random.sample([x for x in range(1,1001) if ((x % 5 == 0) and (x % 7 == 0))], 5))