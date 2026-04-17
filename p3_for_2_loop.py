x=int(input("enter the row"))
for i in range(x):
    for j in range(x,1,-1):
        print(" ",end=" ")
    for k in range(i+1):
        print("*",end=" ")
    x-=1
    print(' ')