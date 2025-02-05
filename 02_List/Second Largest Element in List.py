'''Second Largest Element in a List'''

'''Example:
Input: arr[] = {12, 35, 1, 10, 34, 1}
Output: The second largest element is 34.
Explanation: The largest element of the 
array is 35 and the second 
largest element is 34

Input: arr[] = {10, 5, 10}
Output: The second largest element is 5.
Explanation: The largest element of 
the array is 10 and the second 
largest element is 5

Input: arr[] = {10, 10, 10}
Output: The second largest does not exist.
Explanation: Largest element of the array 
is 10 there is no second largest element
Approach: The approach is to traverse the array twice. 

In the first traversal find the maximum element. 

In the second traversal find the greatest element in the remaining excluding the previous greatest.'''


def getMax(l):
    if not l:
        return None
    else:

        res = l[0]                  # assume l[0] is the max
        for i in range(1, len(l)):  # iterate through index 1 to last
            if l[i] > res:           # check whether current element is greater than res
                res = l[i]          # if current element is greater than res ,update res to current
        return res
    
def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = getMax(l)
    slar = None

    for x in l:

        if x != lar:
            if slar == None:
                slar = x
            else:
                slar = max(x, slar)
    return slar

l = [int(x) for x in input().split()]

print(getSecMax(l))


'''Efficient Solution:
Approach: Find the second largest element in a single traversal. 
Below is the complete algorithm for doing this:  

1) Initialize the first as 0(i.e, index of arr[0] element
2) Start traversing the array from array[1],
   a) If the current element in array say arr[i] is greater
      than first. Then update first and second as,
      second = first
      first = arr[i]
   b) If the current element is in between first and second,
      then update second to store the value of current variable as
      second = arr[i]
3) Return the value stored in second.'''

def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]; slar = None

    for x in l[1:]:
        if x > lar:         # if current element is greater than lar(largest element)
            slar = lar          # update slar to largest
            lar = x         # update lar to current element(largest)

        elif x != lar:      # if x is less then largest and not equal to lar(largest element)
            if slar == None or slar < x:    # if x is greater then second largest
                slar = x                    # assign current element is second largest
    return slar

l = [int(x) for x in input().split()]
print(getSecMax(l))