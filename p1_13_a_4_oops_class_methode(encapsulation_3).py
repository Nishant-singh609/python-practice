class student:
    def __init__(self,name,class_1,roll_no,fee):
        self.name=name
        self.class_1=class_1
        self.roll_no=roll_no
        self.fee=fee
    def display(self):
        return self.class_1,self.roll_no,self.fee
s1=student("nishant singh","b.tech student","0501Ad231041",20000)
print(f"{s1.name} has the roll_no  {s1.display()}")

