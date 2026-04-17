# 1. if Statement
a = 10
if a > 5:
    print("a is greater than 5",a)
    
# 2. if–else

a = 3
if a > 5:
    print("Greater")
else:
    print("Smaller")

# 3. if–elif–else

marks = 75
if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")

# age problem to solve the to analysis the data
age=int(input("Enter the age="))
if age<13:
    print(" it ie the chaild")
elif(age<13 and age >=18):
    print("this is the teenager ")
else:
    print("adult")

# user name and password are same so open

user_name=input("Enter the user_name")
password=input("Enter the password")
if (user_name == "nishant_singh_609" and password == "nishat2323"):
    print("the open sucessfull")
elif(user_name != "nishant_singh_609"):
    print("the user name is the wrong")
else:
    print("the pass word is the wrong")
    
    
#  user gives the number devide the multimal 5

x=input("Enter the user_name")
if(x%5==0):
    print("it the multiple of the 5")
else:
    print("it the  not multiple of the5")
# odd even number


x=int(input("enter the number"))
if(x%2==0):
    print("it is the even number")
else:
    print("it is the odd number")
    
    
# it is the nested loop through
# user name and password are same so open

user_name=input("Enter the user_name")
password=input("Enter the password")
if (user_name == "nishant_singh_609" and password == "nishat2323"):
    print("the open sucessfull")
else:
    if user_name != "nishant_singh_609":
        print("the user name is the wrong")
    else:
         print("the pass word is the wrong")
         
         
# match case
color=input("enter the color")

match color:
    case "green":
        print("go")
    case "red":
        print("stop")
    case "yellow":
        print("to ready  go")
    case _:
        print("the wrong color")
        
    

    
    
    