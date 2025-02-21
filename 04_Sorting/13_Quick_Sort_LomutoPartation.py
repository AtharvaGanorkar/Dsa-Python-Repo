arr = [8, 4, 7, 9, 3, 10, 5]

def LumutoPartation(arr,l,h):
    pivot = arr[h]
    i = l-1

    for j in range(l,h):
        if arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[h] = arr[h],arr[i+1]

    return  i+1

def Qsort(arr,l,h):
    if l < h:
        p = LumutoPartation(arr,l,h)
        Qsort(arr,l,p-1)
        Qsort(arr,p+1,h)

Qsort(arr, 0, 6)

print(arr)