class student:
    def __init__(self,name,mark,add,fee):
        self.name=name
        self.mark=mark
        self.add=add
        self.fee=fee
    def display(self):
        print(self.name,self.mark,self.add,self.fee)
s1=student("nishant",90,"bari,khamdh,stabarwa,daltongalj",90000)
s2=student("manshi",90,"bari,khamdh,stabarwa,daltongalj",90000)
s3=student("ajay",90,"bari,khamdh,stabarwa,daltongalj",90000)
s4=student("dhareej",90,"bari,khamdh,stabarwa,daltongalj",90000)
s5=student("abhisek",90,"bari,khamdh,stabarwa,daltongalj",90000)
s1.display()
s2.display()
s3.display()
s4.display()
s5.display()

