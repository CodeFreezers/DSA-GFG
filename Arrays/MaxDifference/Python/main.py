#1 efficient solution with O(n)
def maxDifference(arr: list) -> int:
  minVal = arr[0]
  res = arr[1] - arr[0]
  for i in range(1, len(arr)):
    res = max(res, arr[i] - minVal)
    minVal = min(minVal, arr[i])
  return res

print(maxDifference([2, 3, 10, 6, 4, 8, 1]))
print(maxDifference([11, 10 , 40 , 123, 4, 41, 2, 34]))
