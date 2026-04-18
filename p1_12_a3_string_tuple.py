# What is a Tuple?

# Tuple ek ordered collection hota hai (list jaisa), lekin immutable hota hai (change nahi hota).

#  Example:

t = (1, 2, 3, 4)
names = ("Nishant", "Rahul", "Aman")
#  Important Difference (List vs Tuple)

# Accessing Elements (Indexing)
t = (10, 20, 30, 40)

print(t[0])   # 10
print(t[-1])  # 40
# Tuple Slicing
t = (1, 2, 3, 4, 5)

print(t[1:4])   # (2, 3, 4)
print(t[:3])    # (1, 2, 3)
print(t[2:])    # (3, 4, 5)
# Tuple is Immutable ❗
t = (1, 2, 3)

# t[1] = 100   # ❌ Error (change nahi kar sakte)
#  Loop in Tuple
t = (1, 2, 3)

for i in t:
    print(i)
# Tuple Methods

#  Tuple me methods bahut kam hote hain:

t = (1, 2, 2, 3)

print(t.count(2))   # 2
print(t.index(3))   # 3
# Special Case (Single Element Tuple)
t = (5,)   # comma important hai
# Tuple Packing & Unpacking
# Packing
t = (1, 2, 3)

# Unpacking
a, b, c = t
print(a, b, c)