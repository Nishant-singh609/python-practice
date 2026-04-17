x=int(input("Enter the number"))
for i in range(2,x):
    if x%i==0:
        print("not prime number")#STARTIN COAD
        break
else:
    print("prime number")
x=int(input("Enter the number"))
for i in range(2,x):
    if x%i==0:
        print(x,"IS NOT PRIME NUMBER")#BEAGING COAD
        break
else:
    print(x,"IS THEPRIME NUMBER")
x=int(input("Enter the number"))
y=print('prime number=')
for x in range(1,x):
    for i in range(2,x):
        if x%i==0:     #printing prime number
            break
    else:
        print(x,end=" ")
x=int(input("Enter the number"))
y=print('prime number=')
for x in range(1,x):
    for i in range(2,x):
        if x%i==0:
            print(x,end=" ")
            break
    else:
        print()
p=int(input("Enter the  starting range="))
q=int(input("Enter the ending range="))
for x in range(p,q):
    for i in range(2,x):
        if x%i==0: 
            break
    else:
        print(x,end=' ')
p=int(input("Enter the starting ranger"))
q=int(input("Enter the ending range"))
h=[]
for x in range(p,q):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x,end=' ')
        h.append(x)
print()
print()
print()
lengh=len(h)
mid=lengh//2
print(h[mid]+h[mid-1])
p=int(input("Enter the starting range="))
q=int(input('Enter the ending point='))
for x in range(p,q):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x)
p=int(input("Enter the starting range="))
q=int(input("Enter the ending range="))
h=[]
for x in range(p,q):
    for i in range(2,x):
        if x%i==0:
            break
    else:
        print(x,end=' ')
        h.append(x)
print()
lenght=len(h)
mid=lenght//2
d=(h[mid]+h[mid-1])
print("ADDING TWO CENTAR NUMBER(mid-1)=",d)
F=(h[mid]+h[mid+1])
print('ADDION OF THE TWO CENTARL NUMBER(mid+1)=',F)






















      
