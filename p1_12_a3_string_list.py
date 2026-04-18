#  What is a List?

# List ek ordered collection hota hai jisme multiple values store kar sakte ho.

#  Example:

a = [1, 2, 3, 4, 5]
names = ["Nishant", "Rahul", "Aman"]
mixed = [1, "Python", 3.5]
#  Accessing Elements (Indexing)
a = [10, 20, 30, 40]

print(a[0])   # 10
print(a[-1])  # 40
#  List Slicing
a = [1, 2, 3, 4, 5]

print(a[1:4])   # [2, 3, 4]
print(a[:3])    # [1, 2, 3]
print(a[2:])    # [3, 4, 5]
#  List Operations
# 1. Add Elements
a = [1, 2, 3]

a.append(4)      # add at end
a.insert(1, 10)  # insert at index
print(a)
# 2. Remove Elements
a = [1, 2, 3, 4]

a.remove(2)   # remove value
a.pop()       # remove last
print(a)
# 3. Update Elements
a = [1, 2, 3]

a[1] = 100
print(a)
# Loop in List
a = [1, 2, 3, 4]

for i in a:
    print(i)
# Important List Methods
a = [3, 1, 4, 2]

a.sort()        # sort
a.reverse() 
print(a)
# reverse
print(len(a))   # length
print(max(a))   # max value
print(min(a))   # min value
# list by using in the list form
a=[12,3,4,5,6,7,8,6]
for i in a:
    print(i,end=" ")
print()
# linear search
a=[1,5,2,7,8,34,90,23]
ind=0
x=90
for i in a:
    if(i==x):
        print(f"the number searching number is the finding {i}",)
        break
    ind+=1
print(" ",ind)