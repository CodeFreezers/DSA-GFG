#1
#The number of digits in a number say N can be easily obtained by using the formula:
#number of digits in N = log10(N) + 1.

import math
def NumberOfDigitsInNumber(N):
  print(round(math.log(N,10)))

NumberOfDigitsInNumber(7665768657657)

NumberOfDigitsInNumber(96535343)

