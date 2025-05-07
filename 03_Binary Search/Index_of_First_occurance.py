# ++++++++++++++++++++ RECURSIVE APPROACH ++++++++++++++++++++++++++

def Firstoccurance(arr,low,high,x):
    if low > high:
        return -1
    mid = low + (high - low)//2
    if arr[mid] > x:
        return Firstoccurance(arr,low,mid-1,x)
    elif arr[mid] < x:
        return Firstoccurance(arr,mid+1,high,x)
    else:
        if mid == 0 or arr[mid-1] != arr[mid]:
            return mid
        else:
            return Firstoccurance(arr,low,mid-1,x)
        

        


# +++++++++++++++++++++ ITTERATIVE APPROACH +++++++++++++++++++++++++++++++
arr = [10,20,20,30,30,30,40]
x =  30
def FirstOccurance(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == 0 or arr[mid] != arr[mid-1] :
                return mid
            else:
                high = mid-1
    return -1

print(FirstOccurance(arr,x))
print(Firstoccurance(arr,0,5,x))