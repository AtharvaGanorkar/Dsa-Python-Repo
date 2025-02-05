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

# arr = [10,15,20,20,40,40]
arr = [5,8,8,10,10]
x = 10

print(LastOccurance(arr,x))



def LastOccurance(arr,low,high,x):
    if low > high:
        return -1
    mid = low + (high - low)//2
    if arr[mid] > x:
        return LastOccurance(arr,low,mid-1,x)
    elif arr[mid] < x:
        return LastOccurance(arr,mid+1,high,x)
    else:
        if mid == high or arr[mid +1] != arr[mid]:
            return mid
        else:
            return LastOccurance(arr,mid + 1,high,x)
        
LastOccurance(arr,0,len(arr)-1,x)
        
# ++++++++++++++++++++++++++++++++++++++++ ITERATIVE APPROACH ++++++++++++++++++++

def findFirstAndLast(arr, n, x):
	first = -1
	last = -1
	for i in range(0, n):
		if (x != arr[i]):
			continue
		if (first == -1):
			first = i
		last = i

	if (first != -1):
		print("First Occurrence = ", first,
			" \nLast Occurrence = ", last)
	else:
		print("Not Found")


# Driver code
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
n = len(arr)
x = 8
findFirstAndLast(arr, n, x)

