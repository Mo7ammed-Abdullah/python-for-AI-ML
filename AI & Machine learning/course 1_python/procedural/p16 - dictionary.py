# ---- dictionary = a changeable , unordered collection of unique key:value pairs
#  fast because they use hashing , allow us to access a value quickly
#  format = {key:value}


capitals = {'USA': 'Washington D.C.', 
            'India': 'New Delhi',
            'china' : 'Beijing',
            'Russia' : 'Moscow'}

print(capitals['USA']) # access value using key
print(capitals.get('england')) # returns None if key not found\
print(capitals.values()) # returns all values in the dictionary
print(capitals.items()) # returns all key:value pairs in the dictionary
print("\n")

capitals.update({'england': 'London'}) # add new key:value pair
capitals.update({'USA': 'Washington D.C.'}) # update existing key:value pair
capitals.pop('china') # remove key:value pair using key
capitals.clear() # remove all key:value pairs from the dictionary

for key, value in capitals.items(): # iterate through the dictionary
    print(key, value)



