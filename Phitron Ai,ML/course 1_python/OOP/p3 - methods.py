# ---- methods are functions that belong to the object
# 1) instance/normal method = methods that operates on objects anf has self as an argument *(basic for now)
# 2) static method = methods that does not operate on the object and has no self or cls as an argument, it is used when method doesn't need to access or modify the class
# 3) class method = methods that operates on the class itself and has cls as an argument, Can access and modify class-level data, but not instance-level data.
# 4) super method = used to call the parent class methods from the child class



# 1) instance/normal method 
class student:
    
    def __init__(self, name, marks):     
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome to the class!" , self.name)       
        
    def get_marks(self):
        return self.marks
    

s1 = student("John Doe",97 )
s1.welcome()  
print(s1.get_marks())  



# 2) static method
class MyClass:
    @staticmethod       # Decorator to define a static method
    def say_hello():
        print("Hello!")


MyClass.say_hello()



# 3) class method
class person:
    name = "anonymous"

    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = person()
p1.changename("John Doe")
print(p1.name)  # Accessing the class variable after changing it using class method




# 4) super method
class car:
    def start(self):
        def __init__(self,type):
            self.type = type

class toyota(car):
    def __init__(self, name, type):
        super().__init__(type)  # Calling the parent class constructor
        self.name = name


car1 = toyota("fortuner", "SUV")
print(car1.type)  # Accessing the type from the parent class
    