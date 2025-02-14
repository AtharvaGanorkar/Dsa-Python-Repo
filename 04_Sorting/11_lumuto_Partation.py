arr = [10,80,30,90,50,70]

def LomutoPartation(arr):
    l = 0
    h = len(arr)-1
    pivot = arr[h]
    i = l-1
    
    for j in range(l,h):
        if arr[j] < pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1]
    
    return 

LomutoPartation(arr)
print(arr)

