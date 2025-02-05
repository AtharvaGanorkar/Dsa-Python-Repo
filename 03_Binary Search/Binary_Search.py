l = [10,20,30,40,50,60]
l2 = [5,15,25]

# +++++++++++++++++++++++++++++ LINEAR SEARCH +++++++++++++++++


def IndexOf(n):
    count = 0
    for i in l:
        count +=1
        if l[count] == n:
            return count
        else:
            return -1

print(IndexOf(80))

# ++++++++++++++++++++++ BINARY SEARCH +++++++++++++++++++++++++

def IndexOf(l,x):
    low = 0
    high = len(l)-1
    while low <= high:
        mid = (low+high)//2
        if l[mid] == x:
            return mid
        elif l[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1

print(IndexOf(l,20))


