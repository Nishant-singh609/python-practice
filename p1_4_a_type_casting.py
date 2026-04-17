# 1. Integer → Float
a = 10
b = float(a)
print(b)

print(b)        # 10.0
print(type(b))  # <class 'float'>
# 2. Float → Integer
a = 3.9
b = int(a)


print(b)        # 3 (decimal removed)
# 3. Integer → String
a = 100
b = str(a)

print(b)        # "100"
print(type(b))  # <class 'str'>
# 4. String → Integer
a = "50"
b = int(a)

print(b + 10)   # 60
# 5. String → Float
a = "3.14"
b = float(a)

print(b)        # 3.14
#  Important
a = "hello"
# b = int(a)   # it is the no posible to convet the data string data type to the int data 

print(b)