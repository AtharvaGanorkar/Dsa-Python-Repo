'''a=[1,2,4,5,6]
b=[2,4,4,6,8]

1,2,4,5,6,8


def Union(a,b):
    c = a+b
    c.sort()
    for i in range(0,len(c)):
        if i == 0 or c[i] != c[i-1]:
            print(c[i],end = " ")
Union(a,b)'''




a=[1,2,4,5,6]
b=[2,4,4,6,8]

1,2,4,5,6,8



def Union(a,b):
    m = len(a)
    n = len(b)
    i = j = 0
    # k = 0
    while i < m and j < n:
        if i > 0 and a[i] == a[i-1]:
            i = i+1
        elif j > 0 and b[j] == b[j-1]:
            j = j + 1
        elif a[i] < b[j]:
            print(a[i],end = " ")
            i = i+1
        elif a[i] > b[j]:
            print(b[j],end = " ")
            j = j+1
        else:
            print(a[i],end= " ")
            i +=1
            j +=1

    while i < m:
        if i > 0 and a[i] != a[i-1]:
            print(a[i], end  = " ")
        i +=1
    while j < n:
        if j > 0 and a[j] != a[j-1]:
            print(b[j], end  = " ")
        j +=1
    

         
Union(a,b)        








