# --- while loop

# run loop until name len is false

name = ""

while len(name) == 0:
    name = input("enter your name ")

print("hello: " +name)

# OR

while not name:
    name = input("enter your name ")

print("hello: " +name)

