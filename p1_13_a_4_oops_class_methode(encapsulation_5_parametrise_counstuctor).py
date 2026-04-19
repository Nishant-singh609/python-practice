# there are two type of the constructor in the python
# 1} parametrise constructor
# 2) default constructor
# parametrise constructor in basiclay passing througth the paramitet
#lets example
class hotel:
    def __init__(self,hotel_name,no_of_floor,no_of_room):
        self.hotel_name=hotel_name
        self.no_of_floor=no_of_floor
        self.no_of_room=no_of_room
    def display(self):
        return self.hotel_name,self.no_of_floor, self.no_of_room
h1=hotel("Abhisek in",10,405)
h2=hotel("Aman in",100,4050)
h3=hotel("nishant in",9,45)
h4=hotel("dhiraj in",199,8405)
h5=hotel("sachine in",10,405)
print(h1.display())
 
