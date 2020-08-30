#1 general answer
def reverseArray(arr: list) -> list:
  if len(arr) <= 1:
    return arr
  else:
    low = 0
    high = len(arr) - 1
    while low < high :
      arr[low], arr[high] = arr[high], arr[low]
      low += 1
      high -= 1
  return arr

print(reverseArray([1,2,3,4,5,6])) #even size
print(reverseArray([1,2,3,4,5,6,7])) #odd size

#2 python specific answer

def reverseArray(arr: list) -> list:
  return arr[::-1]

print(reverseArray([1,2,3,4,5,6])) #even size
print(reverseArray([1,2,3,4,5,6,7])) #odd size
