# 1. f-String (Most Important )

# Python 3.6+ me use hota hai (best & fastest)

name = "Nishant"
age = 20

print(f"My name is {name} and I am {age} years old")

# 2. format() Method
name = "Nishant"
age = 20

print("My name is {} and I am {} years old".format(name, age))

#  Index use karke:

print("My name is {0} and I am {1}".format(name, age))
# 3. % Formatting (Old Method)
name = "Nishant"
age = 20

print("My name is %s and I am %d years old" % (name, age))
# 4. Formatting Numbers
pi = 3.14159

print(f"Value of pi: {pi:.9f}")   # 9 decimal
#  5. Align Text
text = "Python"

print(f"{text:<10}")  # Left align
print(f"{text:>10}")  # Right align
print(f"{text:^10}")  # Center
# 6. Padding (Extra Space Fill)
num = 5

print(f"{num:05}")  # 00005