# there are two type of the Attribute 
# 1)class Attribute
# 2)instance Attribute
# class Attribute--->class Attribute is the belong between 
      # the class it is the present in the common properties in the code 
#instance Attribute-->class Attribute is the belong between 
      # the object and method it is the present in the common or unique value also are present properties in the code 
# example:-
# there are two type of the attribute
#1] class attribute
#2] instance attribute
# class attribute-> the class attribute  is the belong into the under class 
    # it common properties.it is the define in the under the class.
    
# instance attribute-> instance attribute is the belong in the method or object 
   # (it is the unique attribute,diff)

class student:
    college_name="sager institute research of technology -Excellence"# class attribute
    data=900
    def __init__(self,student_name,student_fee,student_add):
        self.student_name=student_name# instance attribute
        self.student_fee=student_fee # instance attribute
        self.student_add=student_add # instance attribute
        self.data=90
    def display(self):
        return self.student_name,self.student_fee,self.student_add
    
    
s1=student("nishant singh",89000,"bari khamdih stabarwadaltonganj")
print(s1.display())
print(s1.college_name)
print(student.college_name)
print(s1.data) # first data will be search in the own object the goto class 
print(student.data) #we want to find the class data so,class_name.data_name


