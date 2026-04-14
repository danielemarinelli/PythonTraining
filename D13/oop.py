# Creating a class

class MyFirstClass:  # class with 2 methods

    def func(self):  # self is a keyword that represent the class and goes before every argument
        pass   # does not do anything

    def displayName(self,name):
        print(name)


mc1 = MyFirstClass()   # creating the object of the class
mc1.displayName("Mc1")
mc2 = MyFirstClass()
mc2.displayName("Mc2")
mc2.func()

#------------- normal method vs static method
class ToDo:
    def m1(self):  # self represent the class
        print("normal method")

    @staticmethod
    def m2(self, num):  # self inside a static method does not represent the class, self is a NORMAL PARAMETER/Variable
        print(num)

td=ToDo()   # creating the object
td.m1()    # normal method
td.m2(22,100)   # static method

#ONLY STATIC METHODS can be access from the class directly
ToDo.m2(2992,1700)

# define variables inside a class
class ToDo2:
    a,b=2,4  #class variables

    def add(self):
        print(self.a+self.b)  # class variable can be access with self keyword!

    def mult(self):
        print(self.a*self.b)

t = ToDo2()
t.add()
t.mult()


# local variables, global variables & class variables
i,j = 24,45  # --> global variables

class ToDo3:
    a,b=2,4  # --> class variables

    def add_numbers(self,x,z):
        print(x+z)     # --> local variables (direct access)
        print(self.a+self.b)  # --> class variables
        print(i+j)   # --> global variables (direct access)

td_add=ToDo3()
td_add.add_numbers(10,20)


# local variables, global variables & class variables ALL WITH SAME NAME
a,b = 24,45  # --> global variables

class ToDo4:
    a,b=2,4  # --> class variables

    def add_numbers(self,a,b):
        print(a+b)       # local variables
        print(self.a+self.b)   # class variables
        print(a+b)   # -->  # AGAIN LOCAL, not global. To
                     #      have sum of global variables we need to call globals function
        print(globals()['a']+globals()['b'])


td_add=ToDo4()
td_add.add_numbers(10,20)


# CONSTRUCTOR job is to: assign data to che class variables
# Class with constructor
# __init__() --> this is the constructor name
# invoked automatically when object is created
class Student:
    def __init__(self):
        print("Student passed exam")

    def m1(self):
        print("Student likes maths")

    def m2(self,year,age):
        return year-age
s=Student()
s.m1()
print(s.m2(2026,48))

# -----------------
# Constructor with parameters and class variables
# Constructor overloading in Python it is not possible
class Student2:
    name="Paul"   # class variable
    def __init__(self,name):
        print(name,"is a student") # name passed from the constructor
        print(self.name)  #prints the class variable
s2=Student2("Danny")

class Student3:
    def __init__(self,name,age,job):  #constructor is assigning data to the variables
        self.name=name
        self.age=age
        self.job=job

    def display(self):
        print(self.name,self.age,self.job)

s3=Student3("Jack",22,"QA Engineer")
s3.display()
s4=Student3("Jane",24,"Developer")
s4.display()