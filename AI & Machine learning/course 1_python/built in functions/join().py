# join converts an iterable(ex: list, tuple, set) to a string.
# the separator is defined by us that will sit in between the iterable
# we can use it to rejoin the string after splitting it using split()
# syntax: separator.join(iterable)



# example 
string = ["hello", "world", "from", "python"]
result = "-".join(string)
print(result)




# example
prompt = "what is philosophy?"

tokens = prompt.split(" ")
print(tokens)

rejoined = " ".join(tokens)
print(rejoined)