l = [20,30,40]
l.reverse()
print(l)

l = [10,30,20,50]
new_l = list(reversed(l))
print(new_l)

l  = [1,2,3,4,5]
new_l = l[::-1]
print(new_l)

l = [int(x) for x in input("Enter numbers: ").split(',')]
def Reverse(l):
    S = []
    for i in l:
        S.insert(0,i)
    return S
print(Reverse(l))

def reverseList(l):
    s=0
    e=len(l)-1
    while s<e:
        l[s],l[e]=l[e],l[s]
        s=s+1
        e=e-1

l = [1,2,3,4]
reverseList(l)
print(l)