# ---- module = a file that contains Python code, such as functions, classes, or variables.
# ---- we can create our own modules by saving Python code in a file with a .py extension.



# for example we have a file called message.py that has a function to print hello world, we can call the function like this:
import message
message.hello_world()

# we can also import specific functions from a module like this:
from message import hello_world
hello_world()

# to see all the inbuilt modules type the given command and run it
help("modules")