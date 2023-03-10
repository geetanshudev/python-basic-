#this is mini project in which class takes information from user and store it into text file

file=open("data2.txt","w")
class student:
    def __init__(self):
        self.name=input("enter name = ")
        self.roll=input("enter roll number = ")
        self.marks=input("enter your marks = ")
    def show(self):
        file.write(self.name)
        file.write("\t")
        file.write(self.roll)
        file.write("\t")
        file.write(self.marks)
        file.write("\n")
        
 #calling class


for i in range(3):
    a = student()
    a.show()

file.close()