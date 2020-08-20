#1

from math import sqrt

def prime(x):
  print(x)
  if x == 1:
    return False
  else:
    m = int(sqrt(x)) + 1
    res = True
    for i in range (2,m):
      if x%i == 0:
        res = False
    return res

print(prime(21))
print(prime(101))
print(prime(97))
print(prime(49))
        
