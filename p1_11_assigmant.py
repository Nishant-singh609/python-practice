# Q1 Write a program that takes salary as input. Using conditional statements, calculate the final tax based on these rules:

# If salary < 30,000 → 5%
# If salary is 30,000–70,000 → 15%
# If salary > 70,000 → 25%
# Q2 Write a function that takes two integers a and b and prints all even numbers between them (inclusive).

# Q3 Write a function that prints the digits of a number n.
# Example: For n = 312, output should be: 3, 1, 2

# Q4 Write a function to return the count of digits in a number n.

# Q5 Write a function to return the sum of digits of a number n.

# Q6 Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.

# Q7

# Design a program to continuously take input from the user and print whether the number is positive or negative until the user enters "Quit".

# Q8 Create a simple calculator function calculator(a, b, operation) that performs:

# Addition (+)
# Subtraction (-)
# Multiplication (*)
# Division (/)
# Q9 Write a function is_prime(n) that returns True if a number is prime and False otherwise.

# Q10 Create a Number Guessing Game:

# If the guess is above the number → print "Too high"
# If the guess is below the number → print "Too low"
# If the guess matches → print "Correct"


# Q1
salary = float(input("Enter salary: "))
if salary < 30000:
    tax = salary * 0.05
elif salary <= 70000:
    tax = salary * 0.15
else:
    tax = salary * 0.25
print("Tax =", tax)
print("Final Salary =", salary - tax)

# Q2
def print_even(a, b):
    for i in range(a, b + 1):
        if i % 2 == 0:
            print(i)

# Q3
def print_digits(n):
    while n > 0:
        print(n % 10)
        n = n // 10

# Q4
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n = n // 10
    return count

# Q5
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

# Q6
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# Q7
while True:
    value = input("Enter a number or Quit: ")
    if value.lower() == "quit":
        break
    num = float(value)
    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")

# Q8
def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Division by zero not allowed"
    else:
        return "Invalid operation"

# Q9
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Q10
secret_number = 7
guess = int(input("Guess the number: "))
if guess > secret_number:
    print("Too high")
elif guess < secret_number:
    print("Too low")
else:
    print("Correct")