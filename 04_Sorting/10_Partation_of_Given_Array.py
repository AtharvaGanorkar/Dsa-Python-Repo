l = [5,13,6,9,12,8,11]
p = 5
a = []
b = []
def Partation(l,p):
    n = len(l)
    l[p],l[n-1] = l[n-1],l[p]
    c = l[n-1]
    for i in l:
        if i <= c :
            a.append(i)
        if i > c:
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


l = [10, 80, 30, 90, 40, 50, 70]
p = 1
Partition(l,p)
print(*l)