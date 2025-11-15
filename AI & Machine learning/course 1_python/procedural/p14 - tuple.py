# tuple = it is immuatable and ordered means we can keep many different datatype elements but cant add new elements later
# used to group related data

student = ("John", "21","male")

print(student.count("John"))  # prints the number of times "John" appears in the tuple
print(student.index("21"))  # prints the index of "21" in the tuple


for x in student:  
    print(x)  # prints each item in the tuple


if "John" in student:  
    print("yes")  # prints "yes" if "John" is in the tuple
    