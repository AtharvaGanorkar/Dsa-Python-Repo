def SOD(n):
   s = 0
   while n > 0:
    i = n%10
    s += i
    n = n//10
   print(s)

SOD(253)

# +++++ USING RECURSION +++++++++

def dSum(n):
  if n < 10:
    return n
  return dSum(n//10) + n%10

dSum(253)