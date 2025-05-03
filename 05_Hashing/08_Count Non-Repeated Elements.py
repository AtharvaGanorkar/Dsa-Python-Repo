# You are given an array of integers arr[]. You need to print the count of non-repeated elements in the array.

# Example 1:

# Input: arr[] = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7]
# Output: 4
# Explanation: 4, 5, 6 and 7 are the elements with frequency 1 and rest elements are repeated so the number of non-repeated elements are 4.
# Input: arr[] = [10, 20, 30, 40, 10]
# Output: 3
# Explanation: 20, 30, 40 are the elements with the frequency 1 and 10 is the repeated element to number of non-repeated elements are 3.


def countNonRepeated(arr):
    frequency = {}

    for i in range(len(arr)):
        if arr[i] in frequency:
            frequency[arr[i]] +=1
        else:
            frequency[arr[i]] = 1

    count_Non_Repeated = 0

    for i in frequency:
        if frequency[i] == 1:
            count_Non_Repeated +=1
    return count_Non_Repeated

arr = [1, 1, 2, 2, 3, 3, 4, 5, 6, 7]
print(countNonRepeated(arr))
