# --- constructor = all classes have a init method that is always executed when an object is created , python creates one if you dont have
# constructor always takes self as the first argument
# self refers to the object that called the method


class student:
    
    def __init__(self, name, marks):     
        self.name = name
        self.marks = marks       
        print("adding new student...")


s1 = student("John Doe" , 97)
print(s1.name, s1.marks)




class student:
    university = "MIT"  # class variable is used when we need same variable for all objects 

    def __init__(self, name, marks):     
        self.name = name           #instance variable
        self.marks = marks       
        print("adding new student...")


s1 = student("John Doe" , 97)
print(student.university)  # accessing class variable using class name