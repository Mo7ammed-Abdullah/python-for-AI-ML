"""
generator = a function that returns an iterator that produces a chunk of values when iterated over.
basically it is used for large datasets. for example if we have 500 data in main memory and we want to process them one by one,
we can use generator to yield a chunk of small amount of data ex:5 data at a time instead of loading all data in RAM.
"""


lst = [x for x in range(500)] 

def data_loader(chunk_size , lst):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i+chunk_size]  # yield a chunk of data


x = data_loader(5, lst) # create a generator object that yields 5 data at a time
print(next(x)) # output: [0, 1, 2, 3, 4]
print(next(x)) # output: [5, 6, 7, 8, 9]



'''
 in the above function yield is basically an iterator that returns a chunk of data(5 data)  when next() is called on the generator object.
 after printing first chunk of 5 data the next() function call will return the next chunk of 5 data
'''


"""
The yield keyword in Python is used to create generator functions.
 Unlike a regular function that uses return to return a value and terminate, 
a generator function uses yield to return a value and then pause its execution, 
preserving its state. When the generator is called again (e.g., in a for loop or with next()), 
it resumes from where it left off. 
""" 