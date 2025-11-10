# ----inheritance = when one class(child) derives the properties and methods of another class(parent)
# 1) single inheritance - one parent class and one child class
# 2) multi-level inheritance - one parent class and one child class, and that child class can also be a parent class for another
# 3) multiple inheritance - one child class can inherit from multiple parent classes



# --- single inheritance
class car:
    def start(self):
        print("Car started")
    
    def stop(self):
        print("Car stopped")

class toyota(car):
    def __init__ (self,name):
        self.name = name


car1 = toyota("fortuner")
car2 = toyota("corolla")
print(car1.start())  # Inherited method from parent class


# --- multi-level inheritance
class car:
    def start(self):
        print("Car started")
    
    def stop(self):
        print("Car stopped")


class toyota(car):
    def __init__ (self,brand):
        self.brand = brand

class fortuner(toyota):
    def __init__ (self, type):
        self.type = type
        

car1 = fortuner("SUV")
car1.start()  



# --- multiple inheritance
class A:
    varA = "welcome to class A "

class B:
    varB = "welcome to class B "

class C(A, B):
    varC = "welcome to class C "

c1 = C()

print(c1.varA)  # Accessing variable from class A
print(c1.varB)  # Accessing variable from class B   
print(c1.varC)  # Accessing variable from class C





