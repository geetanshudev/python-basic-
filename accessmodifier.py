#access modifier
#they are use to give access of class variables and class method outside if the class while implementing concepts of inheritance
#underscore(_) is use to determine access control
#there are mainly three types of assecc modifier

#1}public access modifier
class employee:
    def details(self):
        self.fname=input("Enter first name = ")
        self.lname=input("Enter last name=")
        self.idnumb=int(input("enter id number="))
    def show(self):
        print("first name = ",self.fname)
        print("last name = ",self.lname)
        print("id number=",self.idnumb)
print("this is public access specifier")
obj=employee()
obj.details()
obj.show()

#2}private access modifier
#in this for declaring private variable or method we have write double underscore infront of variable name
class calc:
    def __init__(self):
        self.name="balvinder"
        self.__age=36 #this is private variable
print("\nthis is private acces secifier")
f=calc()
print(f.name)
print(f._calc__age) #for accesing private variable we have to mentioned class name

#3}private access specifier
#memeber that are declared private are only acces to a class derived from it

class student:
    def __init__(self):
        self.name="shyam"
        self._percent=83
print("\nthis is private access specifier")
e=student()
print("name=",e.name)
print("percentage=",e._percent)
