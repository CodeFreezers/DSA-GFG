#1
def SumofDigits(n):
  if n < 10:
    return n
  return SumofDigits(int(n/10)) + n % 10

print(SumofDigits(123))
print(SumofDigits(9994441))
