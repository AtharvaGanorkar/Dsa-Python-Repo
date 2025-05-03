# Hashing is very useful to keep track of the frequency of the elements in a list.

# You are given an array of integers. You need to print the non-repeated elements as they appear in the array.

# Example 1:

# Input:
# n = 10
# arr[] = {1,1,2,2,3,3,4,5,6,7}
# Output: 4 5 6 7
# Explanation: 4, 5, 6 and 7 are the only 
# elements which is having only 1 
# frequency and hence, Non-repeating.
# Example 2:

# Input:
# n = 5
# arr[] = {10,20,40,30,10}
# Output: 20 40 30
# Explanation: 20, 40, 30 are the only 
# elements which is having only 1 

def printNonRepeated(arr,n):
        
        frequency = {}
        
        for num in arr:
            if num in frequency:
                frequency[num]  +=1
            else:
                frequency[num]  = 1
                
        list2 = []
        for key in arr:
            if frequency[key] == 1:
                list2.append(key)
        return list2