# abc ---> Abstract Base Class (default module in Python)
# Giving the access on functionality but hiding the implementation
#
# if you want abstract methods, the class must be abstract
# syntax for abstract class
from abc import ABC, abstractmethod

# Vehicle is abstract class because extends to ABC class
class Vehicle(ABC):    # Vehicle is chield of ABC
    def start(self):   # normal method
        print("Vehicle starting...")

    @abstractmethod
    def engine(self):  #abstract method with annotation
        pass

class Car(Vehicle):
    def engine(self):
        print("Car engine good...")


# can't create object for abstract class  --> v=Vehicle()
c=Car()
c.start()
c.engine()


