#1
# initialise an array of size n+1 

def sieve(n):
  if n <= 1:
    return;
  isPrime = [True for i in range(n+1)]
  i = 2
  while(i*i <= n) :
    if isPrime[i]:
      j = i*i
      while(j <= n):
        isPrime[j] = False
        j += i
    i += 1
  for i in range (2, n+1):
    if isPrime[i] :
      print(i)
      
  
sieve(100)
