# ---- delete =  deleting an object from allocated memory

class student:
    def __init__(self,name):
        self.name = name

s1 = student("John Doe")
del s1  # delete the object s1
print(s1)


# ---- private = those attributes that cannot be accessed outside the class
# to make an attribute private we add a double underscore before

class account:
    def __init__(self, accno, accpass):
        self.accno = accno
        self.__accpass = accpass # private attribute

    def get_accpass(self):
        return self.__accpass # method to access private attribute


acc1 = account(123456, "password123")

print(acc1.accno)  # This will work
print(acc1.__accpass)  # not work, cannot access
print(acc1.get_accpass())  # This will work, accessing private attribute through a method
