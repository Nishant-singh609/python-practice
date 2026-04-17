# datatime pridefine in the modules
import datetime
x= datetime.datetime.now()
print(x)
y=datetime.datetime(1994,10,12)
print(y.strftime("%A"))
y=datetime.datetime(1994,10,12)
print(y.strftime("%m")) # month
y=datetime.datetime(1994,10,12)
print(y.strftime("%d")) # day
y=datetime.datetime(2075,2,28)
print(y.strftime("%A"))