#1
def power (x, n):
  res = 1
  for i in range(n):
    res = res * x
  return res

#2
def power(x, n):
  if n == 0:
    return 1
  temp = power (x, int(n/2))
  temp = temp * temp
  if n % 2 == 0:
    return temp
  else:
    return temp * x


print(power(5, 3))
