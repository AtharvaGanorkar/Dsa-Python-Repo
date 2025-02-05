# +++++++++++Recursive Binary Search +++++++++++++++++

def Bsearch(l,x,low,high):
    if low > high:
        return -1
    mid = low + (high - low)//2
    if l[mid] == x:
        return mid
    elif l[mid] > x:
        return Bsearch(l,x,low,mid-1)
    else:
        return Bsearch(l,x,mid+1,high)

def BsearchMain(l,x):
    return Bsearch(l,x,0,len(l)-1)

l =[10,20,30,40,50,60]  
x = 20

print(BsearchMain(l,x))