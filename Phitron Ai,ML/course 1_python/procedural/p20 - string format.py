# f string formatting

name = "John"
age = 30
height = 5.66045955
print(f"Hello, my name is {name.upper()}. I am {age} years old and my height is {height:.3} feet. his name is also {name}")




# str.format() = optional method that gives users 
#                more control when dispaying output


animal = "cow"
item = "moon"

print("The {} jumped over the {}".format(animal, item)) # will display the values in the brackets
print("The {} jumped over the {}".format("cow", "moon"))
print("The {item} jumped over the {animal}".format(animal="cow", item="moon")) 

text = "the {} jumped over the {}"
print(text.format(animal, item)) 
