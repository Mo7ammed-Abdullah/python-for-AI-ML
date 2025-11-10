# ----abstraction = hiding the complex implementation details of a class and only showing the essential features to users

class car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")


car1 = car()
car1.start()# The user does not need to know how the car starts, they just call the start method






# ----encapsulation is the practice of bundling data and the methods that operate on that data into a single unit, typically a class.
# basically typical class object thing
