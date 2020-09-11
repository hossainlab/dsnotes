# Python List 
[Datastics Lab](https://github.com/datasticslab/ISCB) | Created by [Jubayer Hossain](https://github.com/jubayer-hossain)

## Previous
- What is Python? 
- Why Python Rocks in Research? 
- Little bit history of Python 
- Variables, Expressions, Comments 
- Data Types 
- Printing Messages 
- Operators in Python
- Python Data Type Conversion 
- Python User Inputs 
- Algorithms and Flowcharts 
- `if` statement 
- `else` statement 
- `elif` statement
- `while` loop 
- `range()` function
- `for` loop 
- `pass` statement
- `break` statement 
- `continue` statement 
- Python Function
- Function Arguments / Parameters 
- Strings
- String Manipulation 
- String Methods 
## Today 
- Python List 
- Methods 

# What is List
In short, a list is a **collection** of arbitrary objects, somewhat akin to an array in many other programming languages but more flexible. Lists are defined in Python by enclosing a comma-separated sequence of objects in square brackets ([])

## Characteristics of List
- Lists are ordered.
- Lists can contain any arbitrary objects.
- List elements can be accessed by index.
- Lists can be nested to arbitrary depth.
- Lists are mutable.
- Lists are dynamic.

# Create a list: string 
fruits = ["apple", "orange", "banana"]

# len() 
len(fruits)

# print
print(fruits)

# forward indexing 
fruits[0]

# reverse indexing 
fruits[-1]

# add element 
fruits[2] = "add"

fruits

# Create a list: integer
integers = [2, 1, 5, 6, 7, 8]

# slicing 
integers[0:2]

integers[:]

integers[:2]

integers[-2:-1]

# Create a list: float
floats = [3.2, 1.2, 5.4, 12.5]

# Create a list: complex 
comp = [3+2j, 4- 2j, 2+4j]

# Create a list: boolean
booleans = [True, False, True, False, True, True] 

# Create a mixed list 
mixed = ["apple", 3, 4.5, 3+2j, True]

# Create a list using range() 
odd = list(range(1, 20, 2))
odd

li = [33, 12, 45, 6, 78, 45]

# len()
len(li)

# max() 
max(li) 

# min()
min(li)

# Create a list: string 
fruits = ["apple", "orange", "banana"]

for i in fruits: 
    print(i) 

for index, elem in enumerate(fruits): 
    print(index, elem)

"apple" in fruits

5 not in fruits

li = [33, 12, 45, 6, 78, 45]

li.sort()

li 

li.append(100)

li 

li.insert(2, 20)

li 

li.remove(20)

li 

li.pop() 

li 

li.count(12)

li 

li.reverse() 

li 

## Resources 
- https://www.python.org/doc/essays/blurb/
- https://dev.to/duomly/10-reasons-why-learning-python-is-still-a-great-idea-5abh
- https://www.stat.washington.edu/~hoytak/blog/whypython.html
- https://www.programiz.com/python-programming