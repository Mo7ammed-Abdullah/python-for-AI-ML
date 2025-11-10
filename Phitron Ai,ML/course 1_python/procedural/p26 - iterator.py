# iterator =  an iterator is an object that implements the iterator protocol, allowing sequential traversal through a collection of items.(basically pointer)
# An iterator object must implement two methods: __iter__() and __next__().
# The __iter__() method returns the iterator object itself, 
# and the __next__() method returns the next item from the collection.


x = [1, 2, 3]
iter = iter(x) # create an iterator object from the list x
print(next(iter)) # output: 1        
print(next(iter)) # output: 2
print(next(iter)) # output: 3


# print(next(y)) # raises StopIteration exception as there are no more items in the iterator
# we can also use a for loop to iterate through the iterator object


# using for loop to iterate through the iterator object
for i in iter: 
    print(i) 
