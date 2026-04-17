# String in Python (Simple) 

# ->A string is a sequence of characters (text) written inside quotes.
# 1. Creating String
name = "Nishant"
msg = 'Hello World'
#  2. Access Characters
text = "Python"

print(text[0])   # P
print(text[3])   # h
#  3. String Slicing
text = "Python"

print(text[0:3])   # Pyt
print(text[2:])    # thon
# 4. String Operations
a = "Hello"
b = "World"

print(a + " " + b)   # Hello World
print(a * 2)         # HelloHello
#  5. Common String Functions
text = "python"

print(text.upper())   # PYTHON
print(text.lower())   # python
print(len(text))      # 6
#  6. Check in String
name = "Nishant"

print("N" in name)    # True
#  7. Loop in String
for ch in "Python":
    print(ch)