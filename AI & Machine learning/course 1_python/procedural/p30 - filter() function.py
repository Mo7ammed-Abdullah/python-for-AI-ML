"""
The filter() function lets you select (or filter out) items from an iterable (like a list or tuple) based on a condition.
we basically filter out data from large datasets based on some conditions

syntax: filter(function, iterable)
"""


number =  [x for x in range(100)]

even = list(filter(lambda x: x % 2 == 0, number))
print(even)





data = [0 , 1 , '', 'hello', None, 5.5, [], {}, 25 , None , 'world']

cleaned_data = list(filter(None, data))
print(cleaned_data)
# Output: [1, 'hello', 5.5, 25, 'world']
# Here, filter() removes all "falsy" values from the list, such as 0, '', None, [], and {}.




string = "I am learning Python programming"
vowel = list(filter(lambda x: x in 'aeiou', string))
print(vowel)
# Output: ['a', 'a', 'e', 'i', 'o', 'o', 'a']
# Here, filter() extracts all the vowels from the string.
