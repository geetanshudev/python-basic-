#this is inheritance which is most basic concept of object oriented programming
#it allows create a new class from existing classes in which new class inherit methods and property of another class
#they are mostly five types

#1}single inheritance
#in this only one class i.e child class inherit from parent class
class car():
    def func(self):
        print("this is parent class --> car")

class audi(car):
    def func2(self):
        print("this is child class --> audi")

f=audi() #we must have to call child class not parent class
print("this is single inheritance")
f.func()
f.func2()

#2}multilevel inheritance
#in this class is derived fro other class which aleardy derived from another class
class vehicle():
    def func(self):
        print("this is grandparent class")
        
class car(vehicle):
    def func1(self):
        print("this is parent class")

class audi(car):
    def func2(self):
        print("this is child class")

w = audi()
print("\n this is multilevel inheritance")
w.func()
w.func1()
w.func2()


#3}multiple inheritance
#in this single class is inheritance from more than 2 class
class vehicle():
    def func(self):
        print("this is parent class(1)")
        
class car():
    def func1(self):
        print("this is parent class(2)")

class audi(vehicle,car):
    def func2(self):
        print("this is child class of both parents ")

w = audi()
print("\n this is multiple inheritance")
w.func()
w.func1()
w.func2()

#4}hierarchial inheritance
#in this more than one derived class are created from a single base class
#in this all child take derived from parent class 
class vehicle():
    def func(self):
        print("this is parent class")
        
class car(vehicle):
    def func1(self):
        print("this is child class(1)")

class audi(vehicle):
    def func2(self):
        print("this is child class (2)")

class tata(vehicle):
    def func3(self):
        print("this is child class (3)")

w = car()
x = audi()
y = tata()
print("\n this is heirchial inheritance")
w.func()
w.func1()

x.func()
x.func2()

y.func()
y.func3()
