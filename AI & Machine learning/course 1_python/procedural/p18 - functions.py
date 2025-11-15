# --- functions = a block of code executed when called

# --- function with no return value
def hello(name):
    print("Hello "+name)

hello("john")
# output: Hello john


def hi(f_name , l_name , age):
    print("Hello "+f_name+" "+l_name)
    print("You are " + str(age) + " years old")

hi("john", "doe" ,21)
# output: Hello john doe
#         You are 21 years old



# --- function with return value
def multiply(num1, num2):
    return num1 * num2

x = multiply(2, 3) 
print(x) 
# output: 6



# --- argument(*args) take parameter as tuple and will print it as tuple
def add(*args):
    print(args)

add(1, 2, 3, 4, 5)
# output: (1, 2, 3, 4, 5)



# --- keyword arguments(**kwargs) take parameter as dictionary and will print it as dictionary
def student(**kwargs):
    print(kwargs)

student(name="john", age=21, grade="A")
# output: {'name': 'john', 'age': 21, 'grade': 'A'}



# --- keyword arguments = allows us to pass arguments in any order by using the parameter name
def hi(f_name , l_name , age):
    print("Hello "+f_name+" "+l_name)
    print("You are " + str(age) + " years old")

hi(age=21, f_name="john", l_name="doe") # keyword arguments allow us to pass arguments in any order
# output: Hello john doe
#         You are 21 years old



# --- nested function calls = a function inside another function
# takes a string input , converts it to float , takes absolute value , rounds it to the nearest integer and prints it
print(round(abs(float(input("Enter a positive number: "))))) 
# output: Enter a positive number: -3.7
#         4


# --- unpacking = unpack a collection into individual elements
def giveprediction():
    x = [1, 2, 3]
    return x

a, b, c = giveprediction() # unpacking the list into individual elements
print(a, b, c)
# output: 1 2 3


def giveprediction():
    return {"name": "john", "age": 21, "grade": "A"},{"city": "new york", "country": "usa"}

a, b = giveprediction() # unpacking the tuple into individual elements
print(a, b)
# output: {'name': 'john', 'age': 21, 'grade': 'A'} {'city': 'new york', 'country': 'usa'}


