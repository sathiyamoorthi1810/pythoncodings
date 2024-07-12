'''
3)Inheritance :

Create a base class Employee with attributes name and salary. Define a method display_employee_info that prints the employee's information. Create a derived class Manager that adds an attribute department. Override the display_employee_info method in the Manager class to include the department information. Create an object of the Manager class and call the display_employee_info method.

'''

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display_employee_info(self):
        print(f"Employee name is:{self.name}, Employee salary is{self.salary}")

class Manager(Employee):
    def __init__(self,name,salary,department):
        super().__init__(name,salary)
        self.department = department

    def display_employee_info(self):
        super().display_employee_info()
        print(f"department of employee is :{self.department}")

manager = Manager("sakthi",10000,"Developer")
manager.display_employee_info()















