l = [5,13,6,9,12,8,11]
p = 5
a = []
b = []
def Partation(l,p):
    c = l[p]
    for i in l:
        if i <= l[p] :
            a.append(i)
        if i > l[p]:
            b.append(i)

    return a + b

print(Partation(l,p))


def Partition(l,p):
    n = len(l)
    l[p],l[n-1] = l[n-1],l[p]
    temp = []

    for i in l:
        if i <= l[n-1]:
            temp.append(i)
    for i in l:
        if i > l[n-1]:
            temp.append(i)
    
    for i in range(len(l)):
        l[i] = temp[i]

    return l

print(Partition(l,p))