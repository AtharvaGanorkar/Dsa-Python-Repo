l = [10,20,30,40,50,60]

l.append(30)
print(l)

l.insert(1,15)
print(l)

print(15 in l)

print(l.count(30))

print(l.index(30))

print(l.index(30,4,8))

l.remove(20)
print(l)

print(l.pop())
print(l)

print(l.pop(2))
print(l)

del l[1]
print(l)

del l[0:2]
print(l)

l2 = [10,40,20,50]
print(max(l2))

print(min(l2))

print(sum(l2))

l2.reverse()
print(l2)

l2.sort()
print(l2)


# Python program to demonstrate
# Creation of List

# Creating a List
List = []
print("Blank List: ")
print(List)

# Creating a List of numbers
List = [10, 20, 14]
print("\nList of numbers: ")
print(List)

# Creating a List of strings and accessing
# using index
List = ["Geeks", "For", "Geeks"]
print("\nList Items: ")
print(List[0])
print(List[2])


# Creating a list with multiple distinct or duplicate elements

# Creating a List with
# the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print("\nList with the use of Numbers: ")
print(List)

# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print("\nList with the use of Mixed Values: ")
print(List)

# Accessing elements from the List
l = [10, 20, 30, 40, 50]
print(l)
print(l[3])
print(l[1])
print(l[-1])
print(l[-2])

# Accessing elements from a multi-dimensional list

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [['Geeks', 'For'], ['Geeks']]

# accessing an element from the
# Multi-Dimensional List using
# index number
print("Accessing a element from a Multi-Dimensional list")
print(List[0][1])
print(List[1][0])

# Negative indexing

'''In Python, negative sequence indexes represent positions from the end of the array. 
Instead of having to compute the offset as in List[len(List)-3], it is enough to 
just write List[-3]. Negative indexing means beginning from the end, -1 refers to 
the last item, -2 refers to the second-last item, etc.'''

List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']

# accessing an element using
# negative indexing
print("Accessing element using negative indexing")

# print the last element of list
print(List[-1])

# print the third last element of list
print(List[-3])


# Getting the size of Python list
'''Python len() is used to get the length of the list.'''

# Creating a List
List1 = []
print(len(List1))

# Creating a List of numbers
List2 = [10, 20, 14]
print(len(List2))

# Taking Input of a Python List
'''We can take the input of a list of elements as string, 
integer, float, etc. But the default one is a string'''

# Python program to take space
# separated input as a string
# split and store it to a list
# and print the string list

# input the list as string
string = input("Enter elements (Space-Separated): ")

# split the strings and store it to a list
lst = string.split()  
print('The list is:', lst)   # printing the list

# Example 2:
# input size of the list
n = int(input("Enter the size of list : "))
# store integrs in a list using map,
# split and strip functions
lst = list(map(int, input("Enter the integer\
elements:").strip().split()))[:n]

# printing the list
print('The list is:', lst)


# Adding Elements to a Python List
# Method 1: Using append() method
'''Elements can be added to the List by using the built-in append() function.
 Only one element at a time can be added to the list by using the append() method, 
 for the addition of multiple elements with the append() method, loops are used. 
 Tuples can also be added to the list with the use of the append method because tuples are immutable. 
 Unlike Sets, Lists can also be added to the existing list with the use of the append() method.'''

# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print("Initial blank List: ")
print(List)

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print("\nList after Addition of a List: ")
print(List)

# Method 2: Using insert() method
'''append() method only works for the addition of elements at the end of the List, 
for the addition of elements at the desired position, insert() method is used. 
Unlike append() which takes only one argument, the insert() method requires two arguments(position, value). '''

l = [10, 20, 30, 40, 50]
l.append(30)
print(l)
l.insert(1, 15)
print(l)
print(15 in l)
print(l.count(30))
print(l.index(30))

# Method 3: Using extend() method
'''Other than append() and insert() methods, there's one more method 
for the Addition of elements, extend(), this method is used to add 
multiple elements at the same time at the end of the list.

Note: append() and extend() methods can only add elements at the end
'''
# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = [1, 2, 3, 4]
print("Initial List: ")
print(List)

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print("\nList after performing Extend Operation: ")
print(List)

# Reversing a List
'''A list can be reversed by using the reverse() method in Python.'''

l=[10,40,20,50]
print(max(l))
print(min(l))
print(sum(l))
l.reverse()
print(l)
l.sort()
print(l)


# Removing Elements from the List
# Method 1: Using remove() method
'''Elements can be removed from the List by using the built-in remove() function
 but an Error arises if the element doesn't exist in the list. Remove() method only 
 removes one element at a time, to remove a range of elements, the iterator is used. 
 The remove() method removes the specified item.

Note: Remove method in List will only remove the first occurrence of the searched element.'''

# Python program to demonstrate
# Removal of elements in a List

# Creating a List
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
print("Initial List: ")
print(List)

# Removing elements from List
# using Remove() method
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)

# Example 2:
# Creating a List
List = [1, 2, 3, 4, 5, 6,
        7, 8, 9, 10, 11, 12]
# Removing elements from List
# using iterator method
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)

# Method 2: Using pop() method
'''pop() function can also be used to remove and return an element 
from the list, but by default it removes only the last element of 
the list, to remove an element from a specific position of the List, 
the index of the element is passed as an argument to the pop() method.'''

List = [1, 2, 3, 4, 5]

# Removing element from the
# Set using the pop() method
List.pop()
print("\nList after popping an element: ")
print(List)

# Removing element at a
# specific location from the
# Set using the pop() method
List.pop(2)
print("\nList after popping a specific element: ")
print(List)