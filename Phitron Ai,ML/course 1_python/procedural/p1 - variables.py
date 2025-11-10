# --- variables in python  ---

# 1)---string

f_name = "BRO"
s_name = "code"

multiline = """
this is a multiline
string
example
"""


print(f_name)
print("hello "+ f_name)
print(type(f_name))

full_name = f_name +" "+ s_name
print("hello" + full_name)

print(multiline)

# 2)--- integers

age = 21

age = age + 1
print(age)
print(type(age))
print("your age is : " , age )
print("your age is : " +str(age))   


# 3)--- float

height = 250.5
print(height)
print(type(height))
print("your height is : " +str(height) + "cm")

# 4)--- boolean

human = True
print(human)
print(type(human))
print("are you a human: "+str(human))

# 5)--- multiple assignments

name , age , attractive = "bro" , 21 , True

print(name,age,attractive)