"""
In Python, a lambda function is a small, anonymous function defined using the lambda keyword. 
Unlike regular functions defined with def, 
lambda functions do not require a name and are typically used for short, one-time operations. 
"""

# a lambda function can have many arguments but only one expression
# syntax: lambda arguments: expression(return value)



#  this can be written as ...
def sq_add(x, y):
    return x**2 + y**2

print(sq_add(3, 4))  # Output: 25


#  ...this
sq_add = lambda x, y: x**2 + y**2

print(sq_add(3, 4))  # Output: 25