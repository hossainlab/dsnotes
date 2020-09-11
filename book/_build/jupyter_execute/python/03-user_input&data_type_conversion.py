# User Input in Python

## Type Conversion

### Float to Integer

# Convert into integer 
a = 5.25 

# Check of `a` type before conversion
type(a)

# Conversion
int_a = int(a)

# Check of `a` type after conversion
type(int_a) 

### Integer to Float 

# Convert into float 
b = 10 

# Check of `b` type before conversion
type(b)

# Conversion
float_b = float(b)

# Check of `b` type after conversion
type(float_b)

## Integer to String

# Convert into string  
c = 20

# Check of `c` type before conversion
type(c) 

# Conversion
str_c = str(c)

# Check of `c` type after conversion
type(str_c)

### String to Integer 

# Convert into integer or float 
d = '20'

# Check of `d` type before conversion
type(d) 

# Conversion
int_d = int(d) 

# Check of `d` type after conversion
type(int_d)

## Single Input--Without Message 

# Take input from user without message 
input()

# Take input and store it to a variable 
num = input() 

print(num)

# Check your input type 
type(num)

# Convert your input
num2 = int(input())

num3 = float(input())

type(num3)

type(num2)

## Single Input--With Message 

# Take an input with message 
X = int(input("Enter an integer: "))

type(X)

# Check your input type 

# Convert your input

## Put it Together 

A = int(input("Enter an integer: "))

### Examples 

\begin{example}
Write a Python Program to Add Two Integers 
\end{example}

# Write your solution here! 
num1 = int(input("Enter your first number: ")) 
num2 = int(input("Enter your second number: "))

total = num1 + num2
print("Total = ", total)

\begin{example}
Write a Python Program to Multiply Two Floating Point Numbers 
\end{example}


# Write your solution here! 
num3 = float(input("Enter your first float: "))
num4 = float(input("Enter your second float: "))

total2 = num3 + num4 
print("Total = ", total2) 

## Multiple Inputs
- map()
- split()

# Convert and Split

\begin{example}
Write a Python Program to Add Tree Integers.
\end{example}


# Write your solution


\begin{example}
Write a Python Program to Multiply Tree Floating Point Numbers
\end{example}


# Write your solution