# 1. Basic Example
i = 1

while i <= 5:
    print("Radhe Radhe maa")
    i += 1

# 2. Sum of Numbers
n = 5
i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)
# 3. User Input Example
num = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
# 4. Infinite Loop (⚠️ careful)// its basicaly not uses in the code
while True:
    print("Running...")
# table 
n = int(input("Enter a number: "))

i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i += 1
    
# 1. break (loop ko turant stop karta hai)
i = 1

while i <= 10:
    if i == 5:
        break   # loop yahin ruk jayega
    print(i)
    i += 1


# 2. continue (current iteration skip karta hai)
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue   # 3 skip hoga
    print(i)


#  Easy Difference
# break → loop khatam
# continue → sirf ek step skip
# Real Example (Multiplication Table Skip 5)





