# and,or,not logical operators
# and and or operation

temp = int(input("what is the temperature outside?"))

if temp>=0 and temp<=30:
    print("the temperature is good today")
elif temp<0 or temp>30:
    print("the temperature is bad today")

# not operation gives result if the statement is false

if not(temp>=0 and temp<=30):
    print("the temperature is good today")
