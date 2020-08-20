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
        
#2
#more efficient solution

from math import sqrt

def prime(x):
  print(x)
  if x == 1:
    return False
  if x == 2 or x==3:
    return True
  if x%2 ==0 or x%3==0:
    return False
  else:
    m = int(sqrt(x)) + 1
    res = True
    for i in range (5,m,6):
      if x%i == 0 or x%(i+2) == 0:
        res = False
    return res

print(prime(21))
print(prime(101))
print(prime(97))
print(prime(49))
print(prime(1031))
        
