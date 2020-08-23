#1
def CheckPalindrome(s):
  return helperCheck(s, 0, len(s) - 1)

def helperCheck(s, start, end):
  if start >= end:
    return True;
  
  return (s[start] == s[end]) and helperCheck(s, start + 1, end - 1)

print(CheckPalindrome("abbcdba"))
print(CheckPalindrome("abbcbba"))
