#to make abstract data with parameter
from abc import ABC
class student(ABC):
    def fcn1(self):
        pass
class tony(student):
    def func2(self,fname):
        self.fname=fname
        print("name=",fname)
    def func3(self,idnumber,contract):
        self.idnumber=idnumber
        self.contract=contract
        print("idnumber=",idnumber)
        print("contract=",contract)

fol=tony()
fol.func2("tony stark")
fol.func3(8088,"mk84")
