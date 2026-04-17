# to cheak the  whi many v wels are presents in the user given sting data
a=input("enter the stings=")
vol=0
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="u" :
        vol+=1
        print("the number of the volwel",vol)
    else:
        print("the number of the volwel",vol) 
