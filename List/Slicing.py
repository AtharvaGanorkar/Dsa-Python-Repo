Slicing in Python is a technique used to access specific parts of sequences like lists, 
tuples, or strings. By slicing, you can create a new sequence that contains selected elements from the original sequence.

Slicing Syntax:
T
he general syntax for slicing is sequence[start : stop : step], where:

start: The index where the slice starts (inclusive).
stop: The index where the slice ends (exclusive).
step: The difference between each index in the slice (optional).

Indexing in Sequences:
Sequences in Python are indexed starting from 0 for the first element. Negative indexing starts from −1 for the last element, −2 for the second last, and so on.

Examples of Slicing:
elow is a single comprehensive example that demonstrates various slicing techniques:

# Initialize list
my_list = [10, 20, 30, 40, 50, 60, 70]

# 1. Slicing without start, stop, and step (returns the entire list)
print("Full slice:", my_list[:])

# 2. Slicing with start (from index 2 to the end)
print("Slice with start=2:", my_list[2:])

# 3. Slicing with stop (from beginning to index 4)
print("Slice with stop=4:", my_list[:4])

# 4. Slicing with step (every second element)
print("Slice with step=2:", my_list[0:7:2])

# 5. Slicing with negative step (reversing the list)
print("Slice with -ve step:", my_list[-3:-8:-1])

Output
Full slice: [10, 20, 30, 40, 50, 60, 70]
Slice with start=2: [30, 40, 50, 60, 70]
Slice with stop=4: [10, 20, 30, 40]
Slice with step=2: [10, 30, 50, 70]
Slice with -ve step: [50, 40, 30, 20, 10]

# Initialize list
my_list = [10, 20, 30, 40, 50, 60, 70]

# 6. Slicing with start and step (from index 1 to end, every third element)
print("Slice with start=1 and step=3:", my_list[1::3])

# 7. Slicing with stop and step (from beginning to index 6, every two elements)
print("Slice with stop=6 and step=2:", my_list[:6:2])

# 8. Slicing with negative indices (from index -5 to -2)
print("Slice with negative indices (-5:-2):",  my_list[-5:-2])

# 9. Slicing to reverse a string using shortcut
my_string = "Python"
print("Reversed string:", my_string[::-1])

# 10. Slicing a tuple with start, stop, and step
my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print("Tuple slice with step=3:", my_tuple[::3])

Output
Slice with start=1 and step=3: [20, 50]
Slice with stop=6 and step=2: [10, 30, 50]
Slice with negative indices (-5:-2): [30, 40, 50]
Reversed string: nohtyP
Tuple slice with step=3: (1, 4, 7)



Slicing in List:
List slicing is a common practice in Python and can be used with both positive and negative indexes.

The following program demonstrates list slicing:


# Initialize list
Lst = [50, 70, 30, 20, 90, 10, 50]

# Display sliced list
print(Lst[1:5])

Output
[70, 30, 20, 90]

Slicing in Tuple:
The same slicing technique applies to tuples as well:


tup = (22, 3, 45, 4, 2.4, 2, 56, 890, 1)
print(tup[1:4])

Output
(3, 45, 4)

Slicing Differences Between List, Tuple, and String:

l1 = [10, 20, 30]
l2 = l1[:]
t1 = (10, 20, 30)
t2 = t1[:]          # Tuple having same elements has same id
s1 = "geeks"
s2 = s1[:]          # String of same value has same id
print(l1 is l2)
print(t1 is t2)
print(s1 is s2)

Output
False
True
True
When slicing a list, a new list is created, so l1 and l2 
are different objects. However, slicing a tuple or a string returns the same object since they are immutable.

Everything else is the same in the case of tuples and strings. 
The slicing syntax in the earlier examples is applied similarly to tuples and strings.

