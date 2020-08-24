#1
def josp(n, k):
  a=[0]*n
  for i in range(n):
    a[i]=i
  helperFunc(n, k, a, 0)
  return a[0]

def helperFunc(n, k, a, idx):
  if idx >= len(a):
    idx = idx - len(a) 
  if n==1:
    return a
  temp = idx + k - 1
  if temp >= len(a):
    temp -= len(a)
  a.pop(temp)
  # print(a) un comment this line to see the solution as visualisation
  helperFunc(n-1, k, a, temp)

print(josp(7, 3))
print(josp(5, 3))

#2 simple solution
def josp(n, k):
  if n == 1:
    return 0
  else:
    return (josp(n-1, k) + k) % n

print(josp(7,3))
print(josp(5,2))
