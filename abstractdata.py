#to make abstract data type
from abc import ABC
class car(ABC):
    def mileage(self):
        pass
class tesla(car):
    def mileage(self):
        print("mileage is 30 kmph")
class suzuki(car):
    def mileage(self):
        print("mileage is 25 kmph")

class duster(car):
    def mileage(self):
        print("mileage is 24 kmph")

t=tesla()
t.mileage()
s=suzuki()
s.mileage()
d=duster()
d.mileage()

        
