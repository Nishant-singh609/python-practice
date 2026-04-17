# Types of Functions in Python (Simple) 
#  1. Built-in Functions

# Already available in Python

print("Hello")
len("Nishant")
# 2. User-defined Functions

# Created by user using def

def greet():
    print("Hello")

greet()
# 3. Function with No Arguments & No Return
def show():
    print("Welcome")

show()
#  4. Function with Arguments & No Return
def add(a, b):
    print(a + b)

add(2, 3)
#  5. Function with Arguments & Return Value
def add(a, b):
    return a + b

print(add(4, 5))
#  6. Function with No Arguments & Return
def get_num():
    return 10

print(get_num())
#  7. Lambda Function (Anonymous Function)
square = lambda x: x * x
print(square(5))