'''
7)Create a base class Person with attributes name and age, and a constructor to initialize them. Create a derived class Student that adds an attribute student_id and has its own constructor. Use super() to initialize the name and age attributes in the Student class.
'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self,name, age , stu_id):
        super().__init__(name,age)
        self.stu_id = stu_id
        print(f"Your name is:{self.name}, your age is :{self.age}, your id is:{self.stu_id}")

student = Student("sakthi",26,123456)



