#1
def printSubSets(s, current="", i=0):
  if i == len(s):
    print(current)
    return
  printSubSets(s, current, i+1)
  printSubSets(s, str(current + s[i]), i+1) 

printSubSets("ABC")
