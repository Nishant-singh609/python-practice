# there are three type of the method
# 1)instance method
# 2)class method
# 3) static methode
# (instance method)Example:--
class room_mate:
    home_name="Shree ram bhawan"
    def __init__(self,F_r_name,S_r_name,T_r_name,Fo_r_name):
        self.F_r_name=F_r_name
        self.S_r_name=S_r_name
        self.T_r_name=T_r_name
        self.Fo_r_name=Fo_r_name
    @staticmethod
    def data(big_person_name,small_person_name):
        print(big_person_name,small_person_name)
        
        
    def get_info(self):
        print(f"the home_name {self.home_name} first_name {self.F_r_name} secund_room_mate_name {self.S_r_name} third_room_mate_name {self.T_r_name},fourth_room_mate_name {self.Fo_r_name}")
        # its say two be the para  instance methode
r1=room_mate("nishant singh","manshi singh","ajay singh","Aniket singh")
r2=room_mate("nishant singh","manshi singh","nishant singh" , "manshi singh")
room_mate.data("nishant singh" , "manshi singh")
print()
print()
print()
print()
print()
r1.get_info()