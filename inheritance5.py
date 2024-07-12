'''
8)Create two base classes ClassA and ClassB with a method show that prints different messages. Create a derived class ClassC that inherits from both ClassA and ClassB and overrides the show method to call the show methods of both ClassA and ClassB using super().
'''

class ClassA:
    def show(self):
        print("Hello...")

class ClassB:
    def show(self):
        print("Sakthi")

class ClassC(ClassA,ClassB):
    def show(self):
        super().show()
        super().show()
        pass

   
c = ClassC()
c.show()











