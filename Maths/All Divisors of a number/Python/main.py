#1
# num = x*y such that x < y
# there fore  * x <=n

def printDivisors(n):
  i = 1
  res = []
  while(i*i <=n):
    if (n % i == 0):
      if i:
        res.append(i)
      if int(n/i) != i:
        if int(n/i):
          res.append(int(n/i))
    i += 1
  return sorted(res)

print(printDivisors(21321522312))

