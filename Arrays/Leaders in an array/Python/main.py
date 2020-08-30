#1
def LeadersInArray(arr: list) -> None:
  if len(arr) == 0:
    return
  if len(arr) == 1:
    print(arr[0])
    return
  else:
    currentLeader = arr[len(arr)-1]
    print(currentLeader)
    i = len(arr)-2
    while(i>0):
      if arr[i] > currentLeader:
        print(arr[i])
        currentLeader = arr[i]
      i -= 1

print(LeadersInArray([12,20013,214,465,5643,34,87,78,65]))
