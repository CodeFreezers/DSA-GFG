#1
def TOH(n, a="A", b="B", c="C"):
  if n==1:
    print("move 1 from ", a, " to ", c)
    return
  TOH(n-1, a, c, b)
  print("move", n, "from ", a, " to ", c) 
  TOH(n-1, b, a, c)

TOH(3)
