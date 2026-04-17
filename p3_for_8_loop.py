x=int(input("enter the number"))
y=int(input("inter the number"))
for i in range(x):
    for j in range(y):
        if j<=i:
            print(" ",end="")
        else:
             print("*",end='')
    print('')
    
x=int(input("Enter the number"))
y=int(input("Enter the number"))
for i in range(x):
    for j in range(y):
        if j>=i:
            print("6",end="")
        else:
            print(" ",end='')
    print("\n") 
