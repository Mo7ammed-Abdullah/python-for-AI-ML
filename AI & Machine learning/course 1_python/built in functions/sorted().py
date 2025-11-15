# sorted() function is used to sort an iterable (like a list, tuple, or string) and return a new sorted list.
# syntax: sorted(iterable, key=None, reverse=False)
# iterable: the collection to be sorted
# key: a function that serves as a key based on which the sorting will be done (optional)
# reverse: if True, the sorted list is reversed (optional, default is False)



# example 1: sorting a list of numbers
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = sorted(numbers)
print("Sorted numbers:", sorted_numbers)  # Output: [1, 2, 5, 5, 6, 9]


# example 2: sorting a list of strings
strings = ["banana", "apple", "cherry"]
sorted_strings = sorted(strings)
print("Sorted strings:", sorted_strings)  # Output: ['apple', 'banana', 'cherry']


# example 3: sorting a list of tuples based on the second element
tuples = [(1, 'b'), (2, 'a'), (3, 'c')]
sorted_tuples = sorted(tuples, key=lambda x: x[1] )
print("Sorted tuples by second element:", sorted_tuples)  # Output: [(2, 'a'), (1, 'b'), (3, 'c')]


# example 4: sorting a string (which is an iterable of characters)
string = "python"
sorted_string = sorted(string)
print("Sorted string:", ''.join(sorted_string))  # Output: 'hnopty'


# example 5: sorting in reverse order
sorted_numbers_desc = sorted(numbers, reverse=True)
print("Sorted numbers in descending order:", sorted_numbers_desc)  # Output: [9, 6, 5, 5, 2, 1]


# example 6: sorting with a custom key function (length of strings)
words = ["apple", "banana", "fig", "cherry"]    
sorted_by_length = sorted(words, key=len)
print("Sorted by length of words:", sorted_by_length)  # Output: ['fig', 'apple', 'banana', 'cherry']


# example 7: sorting a list of dictionaries by a specific key
students = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 22}, {'name': 'Dave', 'age': 23}]
sorted_students = sorted(students, key=lambda x: x['age'])
print("Sorted students by age:", sorted_students)  # Output: [{'name': 'Jane', 'age': 22}, {'name': 'Dave', 'age': 23}, {'name': 'John', 'age': 25}]