# Function in Python (Simple) 👇

# A function is a block of code used to perform a task. It helps to reuse code.

#  1. Basic Function
def greet():
    print("Hello!")

greet()
# 2. Function with Parameters
def add(a, b):
    print("Sum =", a + b)

add(5, 3)
# 3. Function with Return Value
def add(a, b):
    return a + b

result = add(4, 6)
print(result)
#  4. Default Parameter
def greet(name="User"):
    print("Hello", name)

greet()
greet("Nishant")
#  5. Function with User Input
x=int(input("Enter the number="))
def square():
    n = int(input("Enter number: "))
    print("Square =", n * n)

square(x)