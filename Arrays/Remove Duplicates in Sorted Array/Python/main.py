#1
def RemoveDuplicates(arr: list) -> list:
  if len(arr) <= 1:
    return arr
  else:
    i = 1
    n = len(arr)
    while i < n :
      if arr[i] == arr[i-1]:
        arr.pop(i)
        n -= 1
        continue
      i += 1
  return arr

print(RemoveDuplicates([1,1,1,1,1,1,1,1,1,2,3,4,5,5,5,6,6,7,8]))
