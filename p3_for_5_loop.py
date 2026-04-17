# list itration 
a=["nishant singh","roll on","mango","data","ham"]
for i in a:
    print(i,end=" ")
print('')



# new form througt

for i in range(len(a)):
    print(a[i])
    
#to use in the while loop
s=len(a)
print(s)
g=0
while g<s:
    print(a[g])
    g+=1
   # hort form the data
[print(i) for i in a]