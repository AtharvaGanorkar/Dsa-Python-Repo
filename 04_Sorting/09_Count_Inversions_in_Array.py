l = [2,4,1,3,5]

#l = [40,30,20,10]

def CountInversion(l): # l = [2,4,1,3,5]

    n = 0
    count = 0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i] > l[j]:
                count +=1
                
    return count

print(CountInversion(l))

arr = [2,4,1,3,5]



def merge_and_count(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    inv_count = 0

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            inv_count += (len(left_part) - i)  # Count inversions
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

    return inv_count


def count_inversions(arr, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += count_inversions(arr, left, mid)
        inv_count += count_inversions(arr, mid + 1, right)
        inv_count += merge_and_count(arr, left, mid, right)
    return inv_count


# Driver code
arr = [2, 4, 1, 3, 5]
inversion_total = count_inversions(arr, 0, len(arr) - 1)
print(inversion_total)  # Output: 3
