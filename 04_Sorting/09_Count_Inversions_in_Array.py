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



def inversionCount(arr,l,m,r):
        res = 0
        l = 0
        r = len(arr)-1
        m = (l + r)//2
        if ( l < r):
            m = (l + r)//2
            
            res += inversionCount(arr,l,m)
            res += inversionCount(arr,m+1,r)
            res += mergecount(arr,l,m,r)
            
    
def mergecount(arr,l,mid,r):
        res = 0
        low = 0
        mid = (l + r)//2
        high = len(arr)-1
        i = 0
        j = 0
        k = 0
        left = arr[low:mid+1]
        right = arr[mid+1:high+1]
        count = 0
        while i < len(left) and j < len(left):
            if left[i] <= right[j]:
                i +=1
            else:
                arr[k] = left[i]
                k +=1
                j +=1
        while i < len(left):
            arr[k] = left[i]
            i +=1
            k +=1
        while j < len(right):
            arr[k] = left[j]
            j +=1
            k +=1
            
        return count

print(inversionCount(arr,l,m,r))