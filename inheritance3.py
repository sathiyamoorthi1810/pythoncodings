'''
6) Create a base class Animal with a method speak that prints "Animal speaks". Create a derived class Dog that overrides the speak method to print "Dog barks". Use super() in the Dog class to also call the speak method from the Animal class.

'''

class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")

dog = Dog()
dog.speak()