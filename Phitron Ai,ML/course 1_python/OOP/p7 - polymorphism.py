# ---- polymorphism =  the ability of an entity (like a variable, function, or object) to take on multiple forms or behave differently in different contexts


# operator overloading using dunder methods
# dunder methods = special methods that starts and end with double undercscores. they allows arithmetic operations between customized objects
class complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def shownumber(self):
        print(self.real,"i +",self.imag,"j")

    def __add__(self,num2):                     # dunder method that overloads the + operator , self is num1 and num2 is num2
        newreal = self.real + num2.real
        newimag = self.imag + num2.imag
        return complex(newreal, newimag)
    
num1 = complex(2, 3)
num2 = complex(4, 5)
num3 = num1 + num2  # this will call the __add__ method
num3.shownumber()  # Output: 6 i + 8 j