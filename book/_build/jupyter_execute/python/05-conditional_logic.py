# Conditional Logic 

## `if` Statement
### Syntax 
```python
if condition:
    Statement...1
    Statement...2
    Statement...n
    
```
- The `if` keyword 
- A Condition(that is an expression that evaluates True or False) 
- A colon 
- Starting on the next line, an **indented** block of code(called if clause) 

### Flowchart 
![img](./img/Python_if_statement.jpg)

# Example-1 
x = 5 
if x > 3:
    print("Smaller")
    print("Inside if")
    
print("Outside if")

# Example-2 
if x < 3: 
    print("Smaller") 
if x > 3: 
    print("Larger") 
print("End")

## `else` Statement 
### Syntax 
```python
if condition:
    Body of if block 
else: 
    Body of else block 
    
```
- The `else` keyword 
- A colon 
- Starting on the next line, an **indented** block of code(called else clause) 

### Flowchart 
![img](./img/Python_if_else_statement.jpg)

a = -10 
if a > 0: 
    print("Positive") 
else: 
    print("Negative")

a = 10 
if a > 0: 
    print("Positive") 
else: 
    print("Negative")

a = -3
if a >= 0: 
    print("Positive") 
else: 
    print("Negative")

## `elif` Statement
### Syntax 
```python
if test expression:
    Body of if
elif test expression:
    Body of elif
else: 
    Body of else
```
- The `elif` keyword 
- A Condition(that is an expression that evaluates True or False) 
- A colon 
- Starting on the next line, an **indented** block of code(called elif clause) 

### Flowchart 
![img](./img/Python_if_elif_else_statement.jpg)

bmi = 20
if bmi <= 18.5: 
    print("Unhealthy")
elif bmi >= 18.5 and bmi < 24.5: 
    print("Normal")
elif bmi >= 24.5 and  bmi < 30: 
    print("Healthy") 
else: 
    print("Obese")

# Even or Odd 
A = int(input("Enter a number: "))

if A % 2 == 0: 
    print("Even")
else: 
    print("Odd")

20 % 2 

11 % 2 

25 % 2 