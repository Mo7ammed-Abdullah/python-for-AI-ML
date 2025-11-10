"""
map() is a built-in Python function that lets you apply a function to each item in an iterable (like a list or string) without writing an explicit loop.

syntax: map(function, iterable)

function = what to apply to each item
iterable = the collection of items (like a list or string or result of split())
"""



#--- EX:Here, map() applies int() to each string in the list, converting them to integers.
nums = list(map(int, ["10", "20", "30"]))
print(nums)
# Output: [10, 20, 30]



#--- Ex: Here, map() applies our own myfunc() to pairs of items from the two tuples.
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))
# Output: ['appleorange', 'bananalemon', 'cherrypineapple']



#--- Ex: Take space-separated integers as input and store in a, b, c, d
a, b, c, d = map(int, input().split())



# ---to square each element in a list
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x * x

squared_numbers = list(map(square, numbers))
print(squared_numbers)  
# Output: [1, 4, 9, 16, 25]



# --- map using lambda
numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)
# Output: [1, 4, 9, 16, 25]



# ---also with condition
squared_numbers = list(map(lambda x: x * x if x % 2 == 0 else x, numbers))
print(squared_numbers)
# Output: [1, 4, 3, 16, 5]