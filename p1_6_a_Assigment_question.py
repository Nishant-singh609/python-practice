# Q1. Name & Age
name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello", name + ", you are", age, "years old!")
# Q2. Two Numbers Operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)
print("Quotient =", a / b)
# Q3. Average of 2 Integers + 1 Float
a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = float(input("Enter a float number: "))

# convert all to float
a = float(a)
b = float(b)

avg = (a + b + c) / 3
print("Average =", avg)
# Q4. Type Conversion
num = "45"

a = int(num)
b = float(num)
c = str(num)

print(a, type(a))
print(b, type(b))
print(c, type(c))
# Q5. Expression Evaluation
x = 10 + 3 * 2 ** 2
print(x)
# Q6. Celsius → Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * (9/5)) + 32
print("Temperature in Fahrenheit =", fahrenheit)
# Q7. Area of Circle
r = float(input("Enter radius: "))

area = 3.14 * r * r
print("Area of circle =", area)
# Q8. Simple Interest
P = float(input("Enter Principal: "))
R = float(input("Enter Rate: "))
T = float(input("Enter Time: "))

SI = (P * R * T) / 100
print("Simple Interest =", SI)
# Q9. Decimal Number Parts
num = float(input("Enter a decimal number: "))

integer_part = int(num)
fractional_part = num - integer_part

print("Integer part =", integer_part)
print("Fractional part =", fractional_part)
# Q10. Example (45.78)
num = 45.78

print("Integer part =", int(num))        # 45
print("Fractional part =", num - int(num))  # 0.78