print("*******  WELCOME TO THE LUCKEY MART  *******")
print('   ')
print('   ')
while True:
    name=input("enter the customer name=")
    total=0

    while True:
        poduct=int(input("enter the product price="))
        quntity=int(input("enter the no of quntity="))
        total+=poduct * quntity
        repite=input("od you want to add more product(yes/No):")
        if(repite=='no' or repite=='NO'):
            break
    print("-"*50)
    print('   ')
    print('   ')
    print("name :",name)
    print("amout to be paid :",total)
    print("-"*50)
    print('   ')
    print('   ')
    print("------------ **** thinkyou for wisite luckey mart **** ----------------")
    print('   ')
    print('   ')
    print('   ')
    repite1=input("do want to the next costumer(yes/no):")
    if(repite1=='no' or repite1=='NO'):
        break
print('   ')
print('   ')
print('   ')
print('   ')
print("------------ **** the process is complite  **** ----------------")

