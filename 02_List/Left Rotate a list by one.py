'''def LRotate(l):
    arr=[]
    for i in l:
        arr.insert(-1,i)
    return arr

l = [10,20,30,40]
print(LRotate(l))

l = [10,20,30,40]
l = l[1:]+l[0:1]
print(l)

l=[10,20,30,40]
a=l.pop(0)
l.append(a)  # l.append(l.pop(a))
print(l)


def Rl(l):
    n = len(l)
    e = l[0]
    for i in range(1,n):
     l[i-1]=l[i]
    l[n-1]=e

l = [10,20,30,40]
Rl(l)
print(l)

arr = [1,2,3,4,5]
d = 2
def rotatearr(arr,d):
    a = -1
    for i in arr:
       for j in range(0,d):
          arr.insert(-a,j)
          a+=1
    return arr 

rotatearr(arr,d)
print(arr)'''

arr = [1,2,3,4,5]
n = 5
d = 2

d = d%n

print(d)