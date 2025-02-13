arr = [10,15,20,40,8,11,55]
low = 0
mid = 3
high = 6
def MergeSubArray(arr,low,mid,high):
    a = arr[low:mid+1]
    b = arr[mid+1:]
    res = []
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    while i < m and j < n:
            if a[i] > b[j]:
                res.append(b[j])
                j = j+1
            else:
                res.append(a[i])
                i = i+1
    while i < m:
        res.append(a[i])
        i +=1
    while j < n:
        res.append(b[j])
        j +=1
    return res
    
print(MergeSubArray(arr,low,mid,high))


def MergeSubArray(arr,low,mid,high):
    a = arr[low:mid+1]
    b = arr[mid+1:]
    m = len(a)
    n = len(b)
    i = 0
    j = 0
    k = low

    while i < m and j < n:
        if a[i] <= b[j]:
            arr[k] = a[i]
            k +=1
            i +=1
        else:
            arr[k] = b[j]
            k+=1
            j+=1
    
    while i < m:
        arr[k] = a[i]
        k +=1
        i +=1
    while j < n:
        arr[k] = b[j]
        k +=1
        j +=1
    
    return arr

         
print(MergeSubArray(arr,low,mid,high))

    