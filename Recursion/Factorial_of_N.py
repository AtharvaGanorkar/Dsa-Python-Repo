def FactN(n,a):
    if n <= 0:
        return a
    return FactN(n-1,n*a)

print(FactN(5,1))

def FactN(n):
    if n<= 0:
        return 1
    return n * FactN(n-1)