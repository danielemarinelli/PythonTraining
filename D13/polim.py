# function can have many forms, in this case len() works
# for string, list, tuple, dict
from D13.oop import Student2

country='Italy'
print(len(country))

grades=[6,8,4,7]
print(len(grades))

tuple = (99,'W',44,88,True,"hello")
print(len(tuple))

student={
    "name":"Paul",
    "country":"Italy",
    "age": 48
}
print(len(student))

# method overloading -POLYMORPHISM-
class People:
    def eat(self,food=None): #None is a keyword
        print("eating",food)
p=People()
p.eat("spaghetti")
p.eat()   # if no arguments are passed, None will be printed


class Calculation:  # ONE METHOD USED IN DIFFERENT FORMS -->OVERLOADING IN PYTHON , different from JAVA
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
c=Calculation()
c.add()
c.add(a=20)
c.add(a=9,b=20)
c.add(a=4,b=200,c=3)
