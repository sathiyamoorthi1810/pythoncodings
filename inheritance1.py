'''
4)Create a base class Person with attributes name and age. Create a derived class Employee that inherits from Person and adds an attribute employee_id. Further, create a class Manager that inherits from Employee and adds an attribute department. Define methods to display information at each level. Create an object of the Manager class and display all its information.

'''

class Person:
    def __int__(self,name,age):
        self.name = name
        self.age = age
class Employee(Person):
    def __init__(self,name,age,emp_id):
        Person.__int__(self, name, age)
        self.emp_id = emp_id
class Manager(Employee):
    def __init__(self,name,age,emp_id,department):
        Employee.__init__(self,name,age,emp_id)
        self.department = department

    def display_information(self):
        print(f"your name is:{self.name},your age is:{self.age},your employee id is:{self.emp_id},your department is:{self.department}")

manager = Manager("sakthi",26,123456,"developer")
manager.display_information()














