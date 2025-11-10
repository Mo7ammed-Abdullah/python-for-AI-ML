# in python strings are immutable, which means they cannot be changed after they are created.
# so the replace() method will not work
# vut we can replace it to a new string

string = "welcome to my house"

string.replace("my", "your")
print(string)

new_string = string.replace("my", "your")
print(new_string)
