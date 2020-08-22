#1
def DecimalToBinary(n):
  s = ""
  str1 = []
  helperFunc(n,str1)
  return s.join(str1)

def helperFunc(n, str1):
  if n==0:
    return
  helperFunc(int(n/2), str1)
  str1.append(str(n % 2))
  

print("7 -- ",DecimalToBinary(7))
print("13 -- ",DecimalToBinary(13))
print("36 -- ",DecimalToBinary(36))

