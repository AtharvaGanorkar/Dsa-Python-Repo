def SmallerElement(l,x):
    S=[]
    for y in l:
        if y<x:
            S.append(y)
    return S

l = [8,100,20,40,3,7,10]
x = 10

print("Smallest elements than",x,"in the given list are",SmallerElement(l,x))


