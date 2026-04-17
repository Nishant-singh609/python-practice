x=int(input("enter the row"))
y=int(input("enter the colon"))
for i in range(1,x+1):
    for j in range(i):
        print(j,end=" ")
    print(' ')



x=int(input("enter the row"))
y=int(input("enter the colon"))
for i in range(1,x+1):
    for j in range(x):
        print(i,end=" ")
    x-=1
    print(' ')



