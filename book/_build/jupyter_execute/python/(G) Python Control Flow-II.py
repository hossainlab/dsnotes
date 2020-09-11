# Loops
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

## Today 
- `while` loop 
- `range()` function
- `for` loop 
- `pass` statement
- `break` statement 
- `continue` statement 



## Why Loops?

print("Bangladesh!")
print("Bangladesh!")
print("Bangladesh!")
print("Bangladesh!")
print("Bangladesh!")

## `while` loop 
### Syntax 
```python
Counter 
while condition: 
    Body of while 
```

### Flowchart 
![img](../img/whileLoopFlowchart.jpg)

# Sum of 1-100 natural numbers 
total = 0
n = 1 
while n <= 100:
    total = total + n 
    n = n+ 1
print(total)    

# Increment 
i = 0 
while i < 10: 
    i += 1 
    print(i)

# Decrement 
i = 10 
while i > 0:  
    i -= 1 
    print(i) 

## `range()` function

range(1,10) 

range(1, 10, 2)

list(range(10)) # range(i) ==> i - 1 

list(range(1, 10)) # range(i) ==> i - 1 

list(range(1, 11)) # range(i) ==> i - 1 

list(range(1, 11, 2)) # range(i) ==> i - 1 

list(range(10, 1, -2)) # range(i) ==> i - 1 

# 1400, 2000(included) and 2 step  
list(range(1400, 2001, 2))

## `for` loop
### Syntax 
```python
for var in sequence: 
    Body of for 
```
### Flowchart
![img](../img/forLoop.jpg)

# List Iteration
li = [1, 2, 3] 
for i in li: 
    print(i) 

# String iteration
s = "Bangladesh" 
for j in s: 
    print(j) 

# for loop using range function: Increment 
for n in range(1, 11): 
    print(n) 

# for loop using range function: Decrement  
for m in range(10, 0, -1): 
    print(m) 

## `break` statement 
![](./img/how-break-statement-works.jpg)
![img](../img/flowchart-break-statement.jpg)

# Example of break statement in while loop-1
j = 0 
while j < 10: 
    j += 1 
    if j == 5: 
        break 
    print(j) 

# Example of break statement in while loop-2
x = 0 
while x < 100: 
    x += 1 
    if x == 5: 
        break 
    print(x)  

# Example of break statement in for loop-1
for y in range(1, 100):
    if y == 5: 
        break
    print(y)

# Example of break statement in for loop-2
for y in range(1, 100):
    if y % 5 == 0: 
        break
    print(y)

## `continue` Statement in `for` and `while` loop 
![img](../img/how-continue-statment-works.jpg)
![img](../img/continue-statement-flowchart.jpg)

# Example of continue satement in while loop
x = 0 
while x < 10: 
    x += 1 
    if x == 5: 
        continue 
    print(x)  

# Example of continue satement in for loop
for y in range(1, 10):
    if y == 5: 
        continue
    print(y)

## `pass` statement

# pass statement in python control flow structure 
for i in range(10): 
    pass 

x = 2 
if x < 0: 
    pass  

## Resources 
- https://www.python.org/doc/essays/blurb/
- https://dev.to/duomly/10-reasons-why-learning-python-is-still-a-great-idea-5abh
- https://www.stat.washington.edu/~hoytak/blog/whypython.html
- https://www.programiz.com/python-programming