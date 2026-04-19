class student:
    def __init__(self,name,roll_no,fee,data):
        self.name=name
        self.roll_no=roll_no
        self.fee=fee 
        self.data=data
    def display(self):
        return (self.name,self.roll_no,self.fee,self.data)
s1=student("nishant singh",8,8900,"i am student in the sirte and i ma superman in the data")
s2=student("abisek sharma",9,8900,"he is strdy in the sirt in the shargar institude")
print(s1.display())
print(s2.display())


