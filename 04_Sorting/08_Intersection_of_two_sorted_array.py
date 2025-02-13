a = [3,5,10,10,10,15,15,20,30]
b = [5,10,10,15,30]


def Intersection(a,b):
    for i in range(len(a)):
        if i > 0 and a[i-1] == a[i]:
            continue
        for j in range(len(b)):
            if a[i] == b[j]:
                print(a[i], end = " ")
                break

Intersection(a,b)



a = [3,5,10,10,10,15,15,20,30]
b = [5,10,10,15,30]

def Intersection(a,b):
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while i < m and j < m:
        if i > 0 and a[i] == a[i-1]:
            i +=1
            continue
        if a[i] < b[j]:
            i +=1
        elif a[i] > b[j]:
            j +=1
        else:
            print(a[i],end = " ")
            i +=1
            j +=1





