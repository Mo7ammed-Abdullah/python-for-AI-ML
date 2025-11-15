# --- args = parameters that will pack all arguments into the tuple
# --- useful so that a function can accept a varying amounst of arguments


def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

x = add(1, 2, 3, 4, 5)
print(x) 



def add1(*stuff):
    sum = 0
    stuff = list(stuff) # convert tuple to list
    stuff[0] = 10
    for i in stuff:
        sum += i
    return sum

print(add1(1, 2, 3, 4, 5)) 


# --- kwargs = parameters that will pack all arguments into a dictionary
# --- useful so that a function can accept a varying amounst of keyword arguments

def hello(**kwargs):
    # print("hello"+kwargs['first'] + " " + kwargs['last']) # can use this or the for loop one
    
    print("hello")
    for key, value in kwargs.items():
        print(value)

hello(first='John', middle='Doe',last='Smith')