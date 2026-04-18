# A set in Python is a collection of unique (no duplicates) and unordered elements.

# ✅ 1. Creating a Set
# # Using curly braces
# my_set = {1, 2, 3, 4}

# # Using set() function
# my_set2 = set([1, 2, 2, 3])
# print(my_set2)   # Output: {1, 2, 3}
# ✅ 2. Key Features
# ❌ No duplicate values
# 🔀 Unordered (no indexing)
# 🔄 Mutable (can change)
# ⚡ Fast operations
# ✅ 3. Add & Remove Elements
# my_set = {1, 2, 3}

# my_set.add(4)       # Add element
# my_set.remove(2)    # Remove element

# print(my_set)
# ✅ 4. Set Operations (Very Important 🔥)
# a = {1, 2, 3}
# b = {3, 4, 5}

# print(a | b)   # Union → {1,2,3,4,5}
# print(a & b)   # Intersection → {3}
# print(a - b)   # Difference → {1,2}
# print(a ^ b)   # Symmetric Difference → {1,2,4,5}
# ✅ 5. Loop in Set
# for i in my_set:
#     print(i)
# ❗ Important Notes
# Sets do not support indexing
# Use for removing duplicates
# Elements must be immutable (no list inside set)
# 🎯 Real Example (Remove duplicates)
# numbers = [1, 2, 2, 3, 4, 4]
# unique = set(numbers)
# print(unique)   # {1, 2, 3, 4}