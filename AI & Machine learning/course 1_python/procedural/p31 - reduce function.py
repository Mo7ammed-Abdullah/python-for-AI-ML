"""
reduce() is used to apply a function cumulatively to the items of an iterable 
that is, it reduces a sequence of values to a single value.

reduce() applies the function to the first two items of the iterable.
The result of this operation then becomes the first argument for the next application of the function, and the next item from the iterable becomes the second argument.
This process continues until all items in the iterable have been processed, resulting in a single accumulated value. 
"""

from functools import reduce


# Example 1: Sum of all numbers in a list
numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(sum_result)  
# Output: 15
# Here, reduce() takes the first two numbers (1 and 2), adds them to get 3, then adds 3 to the next number (3) to get 6, and so on, until all numbers are summed up.



# Example 2: Finding the maximum number in a list
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
max_result = reduce(lambda x, y: x if x > y else y, numbers)
print(max_result)
# Output: 9
# Here, reduce() compares each pair of numbers and keeps the larger one, ultimately finding the maximum value in the list.