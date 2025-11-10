# The split() method splits a string into a list.
# You can specify the separator, default separator is any whitespace.
# syntax: string.split(separator, maxsplit)


text = "10 20 30 40"
parts = text.split()
print(parts)
# Output: ['10', '20', '30', '40']

text = "apple,banana,grape"
parts = text.split(',')
print(parts)
# Output: ['apple', 'banana', 'grape']

text = "one two three four"
parts = text.split(' ', 2)
print(parts)
# Output: ['one', 'two', 'three four']