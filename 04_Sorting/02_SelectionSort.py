def SelectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[min_index],arr[i]= arr[i],arr[min_index]

arr = [10,5,8,20,2,18]

SelectionSort(arr)
print(arr)


# Selection sort is not a stable sorting algorithm.


def SelectionSort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1,len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]

arr = [10,5,8,20,2,18]

SelectionSort(arr)
print(arr)

