# String Formatting

## Anatomy of Strings 
- Single Quote
- Double Quotes 
- Single Quote `VS` Double Quote (**Problems & Advantage**)
- Triple Quotes(**also called docstring**)
- New Line 
- Tab

str1 = 'Hello Bangladesh'

str2 = "Rahim's Name" 
print(str2)

str3 = 'Rahim's Name
print(str3)

## Escape Sequence & Comments

str4 = "Badol's Name"
print(str4)

doc = """doctsring"""
print(doc)

"""This is a comment"""

print("I Love \nBangladesh")

I Love <br>
Bangladesh

print("I Love\tBangladesh") 

I Love Bangladesh

## Printing Message / String Formatting

### Printing any variable without message 

#### Syntax
```python
print(name_of_variable)
```

num1 = 10 
print(num1)

pi = 3.1416 
print(pi) 

p = 4.231236700912
print(round(p, 2))

num4 = 3 + 2j 
print(num4)

name = "John Doe"
print(name)

### Printing variable with message 
#### Syntax
```python
print("message",variable)
```

pi = 3.1416 
print("The value of pi is", pi)

g = 9.8 
print("The value of g is", g) 

a = 10 
print(a, "is a integer value")

name = "John Doe"
print("Hello", name) 

### String Interpolation / f-Strings (Python 3.6+)
#### Syntax
```python
print(f"Message {variable_name}")
```

pi = 3.1416 
print(f"The value of pi is {pi}") 

name = "John Doe"
print(f"My name is {name}")

name = "John"
age = 23 
print(f"My name is {name} and I'm {age}")

a = 10 
b = 20
total = a+b 
print(f"The sum of {a} and {b} is {total}")