a=0
b=1
x=int(input("enter the to find the focciniser series number number="))
print(a)
print(b)
for i in range(2,x):
    c=a+b
    a=b
    b=c
    print(c)
    
