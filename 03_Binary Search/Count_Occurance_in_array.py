def CountOccurance(arr,x):
    count = 0
    for i in range(len(arr)):
        if arr[i] == x:
            count +=1
    return count
    

# arr = [10,20,20,20,30,30]
arr = [10,10,10,10]
x = 10

print(CountOccurance(arr,x))
# -----------------------------------------------------------------------------------------------------------
# Using Binary Search

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
            if mid == 0 or arr[mid-1] != arr[mid]:
                return mid
            else:
                high = mid-1
    return -1

def LastOccurance(arr,x):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            if mid == high or arr[mid+1] != arr[mid]:
                return mid
            else:
                low = mid + 1
    return -1

def CoutOcc(arr,x):
    first = FirstOccurance(arr,x)   # FirstOccurance() and LastOccurance()
                                  # is the function already derived , here we use that
    if first == -1:
         return 0
    else:
        return LastOccurance(arr,x) - first + 1  # this is the formula [lastoccurance - first + 1]

arr = [10,10,10,10]
x = 10
print(CoutOcc(arr,x))