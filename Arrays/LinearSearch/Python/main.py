#1
def linearSearch(arr : list, n) -> int:
  if len(arr) == 0:
    return -1
  for i in range(len(arr)):
    if arr[i] == n:
      return i;
  return -1

arr = [1,2,3,4,5,6,7,8,9,8768,24,4345234,432]

print(linearSearch(arr, 7))
print(linearSearch(arr, 77))
