#1
def CheckIfArrayIsSorted(arr : list) -> bool:
  if len(arr) <= 1 :
    return True
  for i in range(1,len(arr)):
    if arr[i] < arr[i-1]:
      return False
  return True

print(CheckIfArrayIsSorted([1,3,4,9,6,878]))

print(CheckIfArrayIsSorted([1,3,4,6,8,9,3123,99]))

print(CheckIfArrayIsSorted([1,3,4,6,8,9,99]))
