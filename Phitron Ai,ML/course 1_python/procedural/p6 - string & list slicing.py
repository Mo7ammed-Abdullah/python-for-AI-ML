# create a substring by extracting elements from another string/list
# indexing or slicing
# syntax: string[start:stop:step]
#  if step is positive number[eg:+1] or not given, slicing is done left to right
#  if step is negative number[eg:-1], slicing is done right to left



# --- indexing[start:stop] 

name = "hello world"
first_name = name[2:5]
print(first_name)

# indexing[start:stop:step] = skipping steps in the string

nick_name = name[0:11:2]    
funky_name = name[::2] 

print(nick_name)
print(funky_name)


# string reversing

reversed_name = name[::-1]
print(reversed_name)

# --- slice(front slice:back slice) = string slicing
# means according to example remove 7 characters from front and 4 characters from back

website = "http://google.com"

slice = slice(7,-4)
print(website[slice])
print(website[7:-4])


# backward indexing (this prints last 2 characters)
print(name[-2:])


