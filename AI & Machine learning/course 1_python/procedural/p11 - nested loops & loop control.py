# ---nested loops

rows = int(input("how many rows: "))
column = int(input("how many columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(column):
        print(symbol, end="")  #print symbol in one line
    print()  # print new line

# --- loop control statements
# ---- break, continue, pass


#  break

while True:
    name = input("Enter your name: ")
    if name != "":
        break  # exit the loop if name is not empty


#   continue

number = "123-456-789"

for i in number:
    if i == "-":
        continue  # skip the dash character
    print(i, end="")  # print the number without dashes

#   pass , does nothing acts as a placeholder

for i in range(1,21):
    if i == 13:
        pass  # do nothing for 13
    else:
        print(i)  # print all other 
    

