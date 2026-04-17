# range(start, stop, step)
#  1. Basic Example
for i in range(1, 6):
    print(i)


#  2. Print Multiplication Table
n = int(input("Enter number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n * i)
#  3. Loop through String
name = "Nishant"

for ch in name:
    print(ch)
#  4. Sum of Numbers
total = 0

for i in range(1, 6):
    total += i

print("Sum =", total)
#  5. range() Function
for i in range(0, 10, 2):
    print(i)


# Vowel Count in a String (Python) 


text = input("Enter a string: ")

count = 0
vowels = "aeiouAEIOU"

for ch in text:
    if ch in vowels:
        count += 1

print("Number of vowels =", count)

#  Sum of First n Natural Numbers (Python) 
n = int(input("Enter a number: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum =", total)

