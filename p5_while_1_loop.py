h=int(input("Enthe the number"))
x=0
y=1
next_number= y 
count = 1
while count <= h:
    print(next_number,)
    count += 1
    x,y = y,next_number
    next_number = x+y
print()    
