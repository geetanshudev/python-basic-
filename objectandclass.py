#to make simple class and object
class w:  #declaring class
    a="python"
    b="classes"
obj = w()
print(obj.a)
print(obj.b)

#with class metjhod
class student:
    def getdata(self):
        self.name=input("enter name=")
        self.idnumber=int(input("enter idnumber="))
        self.roll=int(input("enter roll number="))
        self.branch=input("enter branch=")
    def display(self):
        print("name=",self.name)
        print("idnumber=",self.idnumber)
        print("roll numnber=",self.roll)
        print("branch=",self.branch)

d=student()
d.getdata()
d.display()
