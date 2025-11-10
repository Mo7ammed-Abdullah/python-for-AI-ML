# ---- index operator[] = gives access to a sequence's element (str,list,tuples)

name = "john Doe"

if(name[0].islower()):
    name = name.capitalize() # capitalize first letter of string

print(name) 


first_name = name[0:3].upper() # slice string from index 0 to 3 and convert to uppercase
print(first_name)

last_char = name[-1] # get last character of string
print(last_char)





# nested data structures = a data structure that can contain other data structures
# example: list in a dictionary, list in a list, dictionary in a dictionary etc


# this is a dictionary that contains nested dictionaries and lists
data = {
    "user": {
        "name": "Alice",
        "id": 123,
        "contact": {
            "email": ["alice@example.com", "abc@edu.com"],
            "phone": "555-1234"
        }
    },
    "items": [
        {"name": "Laptop", "price": 1200},
        {"name": "Keyboard", "price": 75}
    ]
}

print("User Name:", data["user"]["name"])
print("First Item Price:", data["items"][0]["price"])
print("User Email:", data["user"]["contact"]["email"][1])