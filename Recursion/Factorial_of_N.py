def FactN(n,a):
    if n == 0:
        return a
    return FactN(n-1,n*a)

print(FactN(4,1))