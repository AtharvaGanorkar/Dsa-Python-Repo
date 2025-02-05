Comprehensions in Python provide us with a short and concise way to construct new sequences 
(such as lists, set, dictionary etc.) using sequences which have been already defined. 
Python supports the following 4 types of comprehensions:

List Comprehensions
Dictionary Comprehensions
Set Comprehensions
Generator Comprehensions


List Comprehensions:
List Comprehensions provide an elegant way to create new lists. The following is the basic structure of a list comprehension:

output_list = [output_exp for var in input_list if (var satisfies this condition)]

Note that list comprehension may or may not contain an if condition. 
List comprehensions can contain multiple for (nested list comprehensions).

Example #1: Suppose we want to create an output list which contains only the even numbers which are 
present in the input list. Let’s see how to do this using for loops and list comprehension and decide which method suits better.



1
l = [1, 2, 3, 4, 5]
2
​
3
l1 = [x for x in l if x % 2 == 0]
4
print(l1)  # Output: [2, 4]
5
​
6
l2 = [x for x in l if x % 2 != 0]
7
print(l2)  # Output: [1, 3, 5]
 

Output:

[2, 4]
[1, 3, 5]


1
# Using List comprehensions
2
# for constructing output list
3
​
4
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
5
​
6
​
7
list_using_comp = [var for var in input_list if var % 2 == 0]
8
​
9
print("Output List using list comprehensions:",
10
                            list_using_comp)
 

Output:

Output List using list comprehensions: [2, 4, 4, 6]


Dictionary Comprehensions:
Extending the idea of list comprehensions, we can also create a dictionary using dictionary comprehensions. 
The basic structure of a dictionary comprehension looks like below.

output_dict = {key:value for (key, value) in iterable if (key, value satisfy this condition)}

Example #1: Suppose we want to create an output dictionary which contains only the odd numbers that are present 
in the input list as keys and their cubes as values. Let’s see how to do this using for loops and dictionary comprehension.



1
l1 = [1,3,4,2,5]
2
​
3
d1 = {x:x**3 for x in l1}
4
​
5
d2 = {x:f"ID{x}" for x in range(5)} # dictionary comprehension
6
print(d2)
7
​
8
​
9
l2 = [101,103,102]
10
l3 = ['gfg','ide','corse']
11
​
12
d3 = {l2[i]:l3[i] for i in range(len(l2)) }   # dictionary comprehension
13
​
14
print(d3)
15
​
16
​
17
d4 = dict(zip(l2,l3))
18
​
19
print(d4)
 

Output:

{0: 'ID0', 1: 'ID1', 2: 'ID2', 3: 'ID3', 4: 'ID4'}
{101: 'gfg', 103: 'ide', 102: 'corse'}
{101: 'gfg', 103: 'ide', 102: 'corse'}


1
# Using Dictionary comprehensions
2
# for constructing output dictionary
3
​
4
input_list = [1,2,3,4,5,6,7]
5
​
6
dict_using_comp = {var:var ** 3 for var in input_list if var % 2 != 0}

print("Output Dictionary using dictionary comprehensions:",dict_using_comp)
 

Output:

Output Dictionary using dictionary comprehensions: {1: 1, 3: 27, 5: 125, 7: 343}

Set Comprehensions:
Set comprehensions are pretty similar to list comprehensions. 
The only difference between them is that set comprehensions use curly brackets { }. 
Let’s look at the following example to understand set comprehensions.

Example #1 : Suppose we want to create an output set which contains only the even numbers 
that are present in the input list. Note that set will discard all the duplicate values. 
Let’s see how we can do this using for loops and set comprehension.



1
l = {10,20,3,4,10,20,7,3}
2
​
3
s1 = {x for x in l if x%2==0 }
4
s2 = {x for x in l if x%2!=0 }  # set comprehension
5
​

print(s1)
7
print(s2)
 

Output:

{0, 4, 20}
{3, 7}


1
# Using Set comprehensions
2
# for constructing output set
3
​
4
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
5
​
6
set_using_comp = {var for var in input_list if var % 2 == 0}
7
​
8
print("Output Set using set comprehensions:",
9
                            set_using_comp)
 

Output:

Output Set using set comprehensions: {2, 4, 6}
Inverting dictionary:
key becomes value and value becomes key.



1
d1 = {101:'gfg',103:'practice',102:'ide'}
2
d2 = {v:k for (k,v) in d1.items() }
3
​
4
print(d2)
Output:
{'gfg': 101, 'practice': 103, 'ide': 102}

Generator Comprehensions:
Generator Comprehensions are very similar to list comprehensions. One difference between them is that generator 
comprehensions use circular brackets whereas list comprehensions use square brackets. The major difference between 
them is that generators don’t allocate memory for the whole list. Instead, they generate each value one by one which 
is why they are memory efficient. Let’s look at the following example to understand generator comprehension:



1
input_list = [1, 2, 3, 4, 4, 5, 6, 7, 7]
2
​
3
output_gen = (var for var in input_list if var % 2 == 0)
4
​
5
print("Output values using generator comprehensions:", end = ' ')
6
​
7
for var in output_gen:
8
    print(var, end = ' ')
 

Output:

Output values using generator comprehensions: 2 4 4 6 
 