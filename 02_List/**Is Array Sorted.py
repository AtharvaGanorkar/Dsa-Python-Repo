'''Given an array a[ ] of size N. The task is to check if array is sorted or not. 
A sorted array can either be increasingly sorted or decreasingly sorted. Also consider duplicate elements to be sorted.

Example 1:

Input:
N = 5
a[] = {1, 1, 2, 2, 3}
Output: 
1
Explanation: 
Here, Given array a is increasingly sorted.
Example 2:

Input:
N = 2
a[] = {4, 2}
Output: 
1
Explanation:
Here, Given array a is decreasingly sorted.'''


def isSorted(arr,n):
        increasing = True
        decreasing = True
        for i in range(1,n):
            if arr[i-1] > arr[i]: 
                increasing = False
            if arr[i-1] < arr[i]:
                decreasing = False
                
        if increasing or decreasing:
            return 1
        else:
            return 0