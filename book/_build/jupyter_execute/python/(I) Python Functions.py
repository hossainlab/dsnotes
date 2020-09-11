# Python Functions
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

## Today 
- Python Function
- Function Arguments / Parameters 

# Built-in functions 
print("Hello World!")
list(range(10)) 
int(10.3) 
float(3) 
str(3) 

a = int(input()) 
b = int(input()) 
result = a + b 
print(result)

a = int(input()) 
b = int(input()) 
result = a * b 
print(result)

## User Defined Function Template 
```python
def func_name(param1, param2, param3....N): 
    result = param1+param2....N
    return result
# Function Call 
func_name(param_value1, param_value2....N) 
```

## Steps of Creating Function

# Step-1: Define function with name and argument 
def add(num1, num2):
    pass 

# Step-2: Write your statement 
def add(num1, num2):
    result = num1 + num2 

# Step-3: Return your output 
def add(num1, num2):
    result = num1 + num2 
    return result 

# Step-4: Call your function 
add(3, 5) # num1 = 3, num2 = 4 , num1 + num2 , result 

# Call your function one more time or whatever you want 
add(10, 12)

### Documented Your Function
```python
def func_name(param1, param2, param3....N): 
    """Docstring: Documentation for your function"""
    result = param1+param2....N
    return result
# Function Call 
func_name(param_value1, param_value2....N) 
```

# Write a function to add two integers or floats 
def add(num1, num2): 
    """Take two inputs as integer or float and return their sum."""
    result = num1 + num2 
    return result
# Call Function
add(3, 4)

# Check your function documentation
help(add)

# Write a function say_hi
def say_hi(name): 
    """Take input name as string. Returns output.""" 
    return f"Hello! {name}"

# Call 
print(say_hi("Sammo"))

# Check your function documentation
help(say_hi)

def say_hi(name): 
    """Take input name as string. Returns ouput.""" 
    print("Inside Function.")
    return f"Hello! {name}"
print("Outside of Function")

### Required Argument / Parameter

def add(a, b, c): 
    """Take three inputs as integer and returns their sum.""" 
    total = a+b+c 
    return total

add(3, 4)

### Keyword argument 

def add(a, b, c): 
    """Take three inputs as integer and returns their sum.""" 
    total = a+b+c 
    return total

# Function call 
add(a = 12, b = 12, c = 20)

### Default argument 


def add(a, b, c=10): 
    """Take three inputs as integer and returns their sum.""" 
    total = a+b+c 
    return total

add(12, 10)

add(12, 10, 12)

def add_num(num1, num2): 
    total = num1 + num2
    return total

def mul_num(num1, num2): 
    mul = num1 * num2
    return mul 

def div_num(num1, num2): 
    div = num1 / num2
    return div  

add_num(33, 34)

mul_num(10, 2)

div_num(10, 2)

## Resources 
- https://www.python.org/doc/essays/blurb/
- https://dev.to/duomly/10-reasons-why-learning-python-is-still-a-great-idea-5abh
- https://www.stat.washington.edu/~hoytak/blog/whypython.html
- https://www.programiz.com/python-programming