# 13. With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], 
#     write a program to make a list whose elements are intersection of the above given lists.

list1 = [s for s in input("Enter list # 1: ").split()]
list2 = [s for s in input("Enter list # 2: ").split()]
print("Intersection of the two lists is: \n", (set(list1) & set(list2)))