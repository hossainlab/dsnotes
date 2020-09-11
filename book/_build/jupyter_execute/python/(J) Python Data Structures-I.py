# Python Strings
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
## Today 
- Strings
- String Manipulation 
- String Methods 

## String Operators 

### The `+` Operator
The + operator concatenates strings. It returns a string consisting of the operands joined together.

s1 = "Ub" 
s2 = "er"
s1+s2

s3 = "Fizz"
s4 = "Buzz"
s3+s4

### The `*` Operator
The * operator creates multiple copies of a string. If `s` is a string and `n` is an integer, either of the following expressions returns a string consisting of `n` concatenated copies of `s`
* $s \times n$
* $n \times s$

s = "Fizz"
n = 3 
# n * s 
s * n 

# s * n 
n * s 

__Note__

The multiplier operand n must be an integer. You’d think it would be required to be a positive integer, but amusingly, it can be zero or negative, in which case the result is an empty string.

"foo" * -8

"foo" * .5

### The `in` Operator
Python also provides a membership operator that can be used with strings. The in operator returns True if the first operand is contained within the second, and False otherwise

text = "I love Bangladesh!"
# membership check 
"love" in text 

# Dhaka in text? 
"Dhaka" in text

# Dhaka not in text? 
"Dhaka" not in text

## Built-in String Function

### `ord(c)`
Returns an integer of the given character.

# ASCII value of a 
ord('a')

# ASCII value of A 
ord('A')

# ASCII value of # 
ord("#")

### `chr(i)`  
Converts an integer to character 

# Convert integer to character 97 == a 
chr(97)

# Convert integer to character 65 == A 
chr(65)

### `len(s)` 
Returns the length of a string

# length of a string 
S = "Amar Sonar Bangla!"
len(S) 

### `str(param)`
Returns a string representation of a string

# 10 into '10'
str(10)

# 10.5 into '10.5'
str(10.5)

## String Indexing
In Python, strings are ordered sequences of character data, and thus can be indexed in this way. Individual characters in a string can be accessed by specifying the string name followed by a number in square brackets ([]).
String indexing in Python is zero-based: the first character in the string has index 0, the next has index 1, and so on. The index of the last character will be the length of the string minus one.

![img](../img/String-Indexing.png)

# forward indexing
country = "Bangladesh"

# check length
len(country)

country[0]

country[1]

country[2]

country[3]

country[4]

country[5]

country[6]

country[7]

country[8]

country[9]

country[10]

# reverse indexing
country = "Bangladesh"

country[-1]

country[-2]

country[-3]

country[-4]

country[-5]

country[-6]

country[-7]

country[-8]

country[-9]

country[-10]

## String Slicing
![img](../img/Python-String-Slicing-Illustration.png)

# slicing
country = "Bangladesh"

country[0:2] # 0 included but 2 excluded 

country[3:5]

country[2:len(country)]

country[-1:-3]

## String Operation Function

### `s.lower()`
Returns all characters in lowercase.

name = "Rahim"
name.lower() 

### `s.upper()`
Returns all characters in uppercase

text = "fizzbuzz"
text.upper() 

### `s.capitalize()`
Converts first letter into uppercase

text = "fizzbuzz"
text.capitalize() 

### `s.title()`
Convert first letter lowercase to uppercase in a sentence

text2 = "i love bangladesh!"
text2.title() 

### `s.split(t)`
Converts a sentence into List 

# Split a sentence into list 
sent = "Dhaka is the capital of Bangladesh!"
sent.split(" ")

### `s.strip()`
Removes whitespace from text(both side)

text4 = "     FooBazar"
text4.strip() 

### `s.rstrip()`
Removes whitespace from right end.

text5 = "  FooBazar        "
text5.rstrip() 

### `s.lstrip()`
Removes whitespace from left end 

text6 = "  FooBazar        "
text6.lstrip()

## `s.find(t)`
Returns substring position.if the string not found return `-1`

text7 = "Datastics Lab"
text7.find("s")

text7 = "Datastics Lab"
text7.find("Lab")

text7 = "Datastics Lab"
text7.find("foo")

## `s.count(t)`
Returns the number of character in a sentence or word

country = "Japan"
country.count("a")

### `s.replace(u, v)`
Replace value in a sequence of character(string) 

text8 = "Datastics lab"
text8.replace("l", "L") 

## Word Comparison Functions

### `s.startswith(t)`

text9 = "Lab for Making Insights from Data!"
text9.startswith("Lab")

text9 = "Lab for Making Insights from Data!"
text9.startswith("lab")

### s.endswith(t)

text10 = "Lab for Making Insights from Data!"
text10.endswith("!")

text10 = "Lab for Making Insights from Data!"
text10.endswith("?")

### `s.isupper()`

text11 = "Lab for Making Insights from Data!"
text11.isupper() 

### s.islower()

text12 = "Lab for Making Insights from Data!"
text12.islower() 

### s.istitle()

text13 = "Lab for Making Insights from Data!"
text13.istitle() 

### `s.isalpha()`

text14 = "Lab for Making Insights from Data!"
text14.isalpha() 

### `s.isdigit()`

text15 = "Lab for Making Insights from Data!"
text15.isdigit()

### `s.isalnum()`

text16 = "Lab for Making Insights from Data!"
text16.isalnum()

## String Iteration

S = "Bangladesh!"
for i in S: 
    print(i)

S = "Bangladesh!"
for index, val in enumerate(S): 
    print(index, val)

## Resources 
- https://www.python.org/doc/essays/blurb/
- https://dev.to/duomly/10-reasons-why-learning-python-is-still-a-great-idea-5abh
- https://www.stat.washington.edu/~hoytak/blog/whypython.html
- https://www.programiz.com/python-programming