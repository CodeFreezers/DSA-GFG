#1

#x * y = gcd(x,y) * lcm(x,y)
# lcm(x,y) = (x * y) / gcd(x,y)

def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,int(a%b))

def lcm(x,y):
  return int((x*y)/gcd(x,y))

print(lcm(3,4))
  
