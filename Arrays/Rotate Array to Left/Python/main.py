#1 
def rotateLeft(arr: list, n: int) -> list:
  if len(arr) <= 1:
    return arr
  else:
    while(n > 0):
      temp = arr[len(arr)-1]
      for i in range (len(arr)):
        arr[i-1] = arr[i]
      arr[len(arr)-2] = temp
      n -= 1
    return arr

print(rotateLeft([1,2,3,4,5,6],3))
