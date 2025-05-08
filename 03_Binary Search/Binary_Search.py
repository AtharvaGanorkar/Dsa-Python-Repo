l = [10,20,30,40,50,60]
l2 = [5,15,25]

# +++++++++++++++++++++++++++++ LINEAR SEARCH +++++++++++++++++


def Search(arr,num):
    n = len(arr)-1
    if num < arr[0] or num > arr[n]:
        return -1
    
    for i in range(0,n+1):
        if arr[i] == num:
            return i
    return -1

# arr = [5,10,15,25,35]
# num = 25
arr = [10,10]
num = 10
print(Search(arr,num))

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


