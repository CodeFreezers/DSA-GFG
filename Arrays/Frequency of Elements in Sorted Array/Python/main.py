#1
def freqInSortedArray(arr: list) -> None:
  freq, i = 1, 1
  n = len(arr)
  while i < n:
    while i < n and arr[i] == arr[i-1]:
      freq += 1
      i += 1
    print(arr[i-1], " -- ",freq)
    freq = 1
    i += 1
  
print(freqInSortedArray([1,1,1,4,4,4,4,4,6,6,7,8,9,12,12,12,12]))
