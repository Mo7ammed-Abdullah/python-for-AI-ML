# --- some things to know about oop

# class is the blueprint for an object
# object is the instance of a class , that means it has all properties and methods defined in the class with its own values
# instance means object 


class car:
    color = "red"  # class variable
    model = "BMW"  # class variable

car1 = car()  # creating an object of class car
print(car1.color)  