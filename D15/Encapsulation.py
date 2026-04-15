# getters and setters to protect variables with methods and no direct access

class Employee:
    def __init__(self, name, age):  # constructor
        self.name = name   # public variable
        self.age = age      # public variable
        self.__salary = 1100  # private variable (with double __ in front)

    # getter method
    def get_salary(self):
        return self.__salary

    #setter method
    def set_salary(self, salary):
        if salary > 1100:
            self.__salary = salary
        else:
            print("salary is too low")


e=Employee("Roy", 91)
e.set_salary(200)  # salary can't be set directly, but only in setters or getters
print(e.get_salary())

