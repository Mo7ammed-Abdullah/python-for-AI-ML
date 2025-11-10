# ---- list = it is muatable means we can keep many different datatype elements and also add new elements later
# ---- we use square brackets to create a list

food = ["pizza", "hamburger", "hotdog", "spaghetti", "tacos"]

print(food)  # prints the entire list
print(food[0])  # prints the first item in the list

food[0] = "sushi"  # changes the first item in the list to sushi
print(food)  

food.append("ice cream")  # adds ice cream to the end of the list
food.remove("hamburger")  # removes hamburger from the list
food.pop(1)  # removes the second item in the list (index 1)
food.insert(1, "cake")  # inserts cake at index 1
food.sort()  # sorts the list in alphabetical order
food.clear()  # clears the entire list



