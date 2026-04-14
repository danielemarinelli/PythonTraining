# Inheritance
# class should start with Upper char
class League:
    country = "England"
    def m1(self):
        print("Premier League")

class TeamA(League): # TeamA class is a child of League class
    category = "A"
    def m2(self):
        print("Chelsea Team")

class TeamB(TeamA): # TeamB class is a child of TeamA class
    category = "B"  #class variable accessible with self keyword
    def m3(self):
        print("Sampdoria Team in category",self.category)


t=TeamA()     # class TeamA has two methods now
t.m1()
t.m2()
print(t.country)

t1=TeamB()
t1.m3()
t1.m2()  # comes from TeamA class
t1.m1() # comes from League class
print(t1.country) # comes from League class
#-----------------------------------------------------
#MULTIPLE Inheritance
# one Child C can have TWO parents A,B (In Java not possible)
class A:
    x,y=20,30  # class variables
    def m1(self):
        print(self.x+self.y)

class B:
    a,b=10,20
    def m2(self):
        print(self.a+self.b)

class C(A,B):   #C has total 6 variable and 3 methods
    i,h=7,9
    def m3(self):
        print(self.i, self.h)

c=C()
c.m3()  # from C
c.m2()  # from B
c.m1()  # from A
#-----------------------------------------------------
#OVERRIDING METHOD
# Calling immediate parent class method using child class --> super()
class A:
    def m1(self):
        print("m1 in class A")
class B(A):
    def m1(self):
        print("m1 in class B")
        super().m1()    # invoke the immediate parent class method m1

b=B()  # obj created for B class
b.m1()  # m1 from class B
#-----------------------------------------------------
# Calling parent class variables using child class
class A:
    s,n = 44,32

class B(A):
    p,k=32,66
    def m1(self,a,b):
        print(a+b)    # local vars
        print(self.p,self.k)  # class B vars
        print(self.s-self.n)  # class A vars
b=B()
b.m1(1000,3000)

class C(B):
    p,k=99,101    # Overriding p and k variables of class B
    def getParentVariable(self):
        print("variables of parent",super().p,super().k)

c=C()
print("variables of child",c.k-c.p)
c.getParentVariable()
#-----------------------------------------------------




