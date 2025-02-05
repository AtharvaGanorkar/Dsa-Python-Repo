l = [int(x) for x in input("Enter numbers Seprated by commas: ").split(',')]
def LargestElement(l):
    l.sort()
    return l[-1]


print(LargestElement(l))

def getMax(l):
    for x in l:
        for y in l:
            if y > x:
                break
            else:
                return x
        return None
    

def getmax(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i] > res:
                res = l[i]
        return res
    