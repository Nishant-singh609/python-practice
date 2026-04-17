x=int (input("Enter the number="))
y=int(input("Enter the number="))
for i in range(x):
    for j in range(y):
        if j<=i:
            print("1",end='')
        else:
            print("",end='')
    print()
    

x=int (input("Enter the number="))
y=int(input("Enter the number="))
for i in range(x):
    for j in range(y):
        if j<=i:
            print("1",end='')
        else:
            print("",end='')
    print()


x=int (input("Enter the number="))
y=int(input("Enter the number="))
for i in range(x):
    for j in range(y):
        if i<=j:
            print("*",end='')
        else:
            print("",end='')
    print()

x=int (input("Enter the number="))
y=int(input("Enter the number="))
for i in range(x):
    for j in range(y):
        if i>=j:
            print("*",end='')
        else:
            print("",end='')
    print()

x=int(input(" Phone Pay Number//ACCOUNT NO="))
y=int(input("Amount"))
pin=1234
c=0
while c<4:
    p=int("Enter the pin=")
    if pin==p:
        print("transection is sucessful")
        break
    else:
        print("INcorrect pin number")
        c=c+1

x=int(input("Enter the number="))
y=int(input("Enter the number="))
for i in range(x):
    for j in range(y):
        if j>=x-i and j<=x-j:
            print("*",end='')
        else:
            print(" ",end="")