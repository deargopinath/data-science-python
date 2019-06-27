# 15.
# Give example of fsum and sum function of math library.
#
#  math.fsum(iterable) - Return an accurate floating point sum of values in the iterable.
#
#  Example: 
#  sum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
#  0.9999999999999999
#
#  fsum([.1, .1, .1, .1, .1, .1, .1, .1, .1, .1])
#  1.0

from math import fsum
data = [float(x) for x in input("Enter comma separated values:\n").split(',')]
print("sum = ", sum(data))
print("fsum = ", fsum(data))
