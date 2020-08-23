#1
def Solution(n, a, b, c):
  if n == 0:
    return 0
  if n < 0:
    return -1
  res =  max(Solution(n-a, a, b, c), Solution(n-b, a, b, c), Solution(n-c, a, b, c))
  if res == -1:
    return -1
  return res + 1

print(Solution(5, 1, 5, 2))

#Time complexity O(3^n) // by using DP we can improve it
