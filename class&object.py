'''
1) Class and objects :

Create a class Student with attributes name and age. Include a method display_info that prints the student's information. Create an object of the Student class and call the display_info method.

'''


class Student:
    name = "Sakthi"
    age = 25
    def display_info(self):
        print(f"name is:{self.name},age is:{self.age}")
stu = Student()
stu.display_info()