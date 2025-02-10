# Floor in a Sorted Array
'''Given a sorted array arr[] (with unique elements) and an integer k, 
find the index (0-based) of the largest element in arr[] that is less than or equal to k. 
This element is called the "floor" of k. If such an element does not exist, return -1.

Examples

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 0
Output: -1
Explanation: No element less than 0 is found. So output is -1.

Input: arr[] = [1, 2, 8, 10, 11, 12, 19], k = 5
Output: 1
Explanation: Largest Number less than 5 is 2 , whose index is 1.

Input: arr[] = [1, 2, 8], k = 1
Output: 0
Explanation: Largest Number less than or equal to  1 is 1 , whose index is 0.'''


def findFloor(self,arr,k):
        low = 0
        high = len(arr)-1
        floor = -1
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == k:
                return mid
            
            if arr[mid] > k:
                high = mid - 1
            else:
                floor = mid
                low = mid + 1
        
        return floor
        

def findFloor(self,arr,k):
        res = -1
        for i in range(0,len(arr)):
            if arr[i] <= k:
                res = i
        return res
