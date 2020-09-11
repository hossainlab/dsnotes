# Odd-Even 
n = int(input("Enter a number: "))
if n % 2 == 0: 
    print("Even")
else: 
    print("Odd") 

# Negative-Positive 
m = int(input("Enter a number: ")) 
if m >= 0: 
    print("Positive") 
else: 
    print("Negative")

# greater-less 
a = int(input()) 
b = int(input()) 

if a > b: 
    print(f'{a} is greater than {b}') 
else: 
    print(f'{a} is less than {b}')  

# 1-10 even 
for i in range(1, 11): 
    if i % 2 == 0:
        print(i) 

# 1-10 odd  
for i in range(1, 11): 
    if i % 2 != 0:
        print(i) 

# Positive 
li = [-3, -4, - 5, 11, 14, 14, 5] 
for n in li: 
    if n >= 0: 
        print(n)

# Negative
li = [-3, -4, - 5, 11, 14, 14, 5] 
for n in li: 
    if n < 0: 
        print(n)