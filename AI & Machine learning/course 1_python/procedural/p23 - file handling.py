
# --- read file

file = open('./procedural/test.txt', 'r')  # r for read, w for write, a for append
print(file.read())
file.close()  

# --- read one line
file = open('./procedural/test.txt', 'r')
print(file.readline())  
file.close()

 # --- read line by line
with open('./procedural/test.txt', 'r') as file:  # with auto closes the file
    for line in file: 
        print(line)

with open('./procedural/test.txt', 'r') as file:
    for line in file:
        l = line.strip()  # removes extra new line
        print(l)

# ---- read a file with exception handling 
try:
    with open('./procedural/test.txt' , 'r') as f:
        print(f.read())
except FileNotFoundError:
    print ("File not found")

# ---- write a file . clears existing data and write newly
with open('./procedural/test.txt' , 'w') as f:    
    f.write('Hello World')
    

# ---- append a file . adds to existing data
with open('./procedural/test.txt' , 'a') as f:
    f.write('Hello me')



# append multiple lines
string = ['\nhello\n', 'hi\n', 'how are you?\n']

with open('./procedural/test.txt' , 'a') as f:
    f.writelines(string)



# --- file pointer

with open('./procedural/test.txt' , 'r') as f:
    print(f.tell())  # current position of pointer is at 0
    print(f.read())
    print(f.tell())  # current position of pointer is at end of file  
    print(f.read())  # nothing to read since pointer is at end of file

    print(f.seek(0))  # set pointer to position 0
    print(f.tell())  


# --- w+ mode : write and read . clears existing data and write newly
with open('./procedural/test.txt' , 'w+') as f:    
    f.write('Hello World\n') 
    f.write('Hello me\n')  # ponter is at end of file after write
    f.seek(0)   # set pointer to position 0
    print(f.read())


# --- truncate a file
with open('./procedural/test.txt' , 'r+') as f:    
    print(f.read()) 
    f.truncate(5)  # keep first 5 characters, rest will be deleted
    f.seek(0)
    print(f.read())


# ---- copy file
import shutil

shutil.copy('test.txt', 'test2.txt') # source file, destination file



# ---- move file
import os

source = "test.txt"
destination = "C:\\Users\\moham\\Downloads\\test.txt"

try:
    if os.path.exists(destination):
        print("File already exists")
    else:
        os.rename(source, destination)
        print("File moved")
except FileNotFoundError:
    print("File not found")




# ---- delete file
import os

os.remove("test.txt")