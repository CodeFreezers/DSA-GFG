#1

def gcd(a,b):
  while a!=b:
    if a>b:
      a -= b
    else:
      b -= a
  return a

print(gcd(12,36))

#2

def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,int(a%b))

print(gcd(12,36))
  
  
