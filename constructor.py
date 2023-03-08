#in class and object weuse constructor by __init__()
#they are three type
#1}parameterized constructor - in this parameter have atleat 2 parameters i.e self and other
class d:
    def __init__(self, x,y):
        self.x=x
        self.y=y
    def show(self):
        print("a=",self.x)
        print("b=",self.y)
c = d(34,45)
print("\nthis is parameterized constructor")
c.show()

#2}non-parameterized constructor - in this there is no need for declaring parameters
class A:
    def __init__(self):
        self.a=" python for data science"
    def show(self):
        print(self.a)

w=A()
print("\nthis is non-parameterized constructor")
w.show()

#3}default constructor - in this we don't use constructor function or it is a simple object and class
class G:
     a="data science"
     def output(self):
        print(self.a)
    
       
    

h=G()
print("\nthis is default constructor")
h.output()