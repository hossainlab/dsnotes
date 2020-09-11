# Operators in Python

## Boolean Data Types 
- True: Returns True if the condition is True 
- False: Returns False if the condition is False 

# True 
a = 5 
b = 5 

a == b 

# False 
a > b 

# Case Sensitive 
True 

False 

## What are Operators? 
Operators are **special symbols** in Python that carry out arithmetic or logical computation. The value that the operator operates on is called the **operand**.
![](operators.png)

## Arithmetic operators
- ($+$) **Add** two operands or unary plus
- ($-$) **Subtract** right operand from the left or unary minus
- ($*$) **Multiply** two operands
- ($/$) **Divide** left operand by the right one (always results into **float**)
- (%) **Modulus** - remainder of the division of left operand by the right
- ($//$) **Floor division** - division that results into whole number adjusted to the left in the number line
- ($**$) **Exponent** - left operand raised to the power of right

# Addition
x = 3 
y = 5 
x + y 

# Subtraction
x - y  

# Multiplication
x * y 

# Division
x / y 

result = x / y 
type(result)

# Modulus 
x % y  

# Floor Division
3 // 2 

# Exponent 
2 ** 3 

## Comparison operators
- ($>$) **Greater** than - True if left operand is greater than the right
- ($<$) **Less**  than - True if left operand is less than the right
- ($==$) **Equal**  to - True if both operands are equal
- ($!=$) **Not equal**  to - True if operands are not equal
- ($!=$) **Not equal**  to - True if operands are not equal
- ($>=$) **Greater than or equal**  to - True if left operand is greater than or equal to the right
- ($<=$) **Less than or equal**  to - True if left operand is less than or equal to the right

# Greater than 
m = 20 
n = 15 
m > n 

# Less than 
m < n 

n < m 

# Equal to 
m == n 

# Not equal to 
m != n 

# Greater or equal 
m >= n  

x1 = 5 
x2 = 5 
x1 >= x2 

# Less or equal 
m <= n 

## Logical operators 
- **and**: True if both the operands are true
- **or:** True if either of the operands is true
- **not:** True if operand is false (complements the operand)

# and 
2 == 2 and 4 > 2 

2 == 4 and 4 < 2 

# or 
2 == 4 or 4 > 2 

# not 
a = 3 
b = 2 
result = True 
not result 

## Assignment operators
- Assignment: ($=$)
- Increment: ($+=$)
- Decrement: ($-=$)

# Assignment
x3 = 50 

# Increment 
x3 = x3+1 
print(x3)

x3 = x3 + 2 
print(x3)

x3 += 3 
print(x3)

# Decrement 
x3 = x3 - 2 
print(x3)

x3 -= 6 
print(x3)

##  Identity Operators
- **is:** True if the operands are identical
- **is not:** True if the operands are not identical (do not refer to the same object)

# is 
s1 = "Jubayer"
s2 = "Shihab" 

s1 is s2

# is not 
s1 is not s2  

## Membership Operators
- **in:** True if value/variable is found in the **sequence**
- **not in**: True if value/variable is not found in the sequence

# in
s3 = "Hello World!"
"H" in s3

"h" in s3

# not in 
"h" not in s3