import time

# --- for loop

for i in range(10):
    print(i)

# i in range(start,stop)

for i in range(50,100):
    print(i)

# i in range(start,stop,step)

for i in range(50,100,2):
    print(i)

# for string

for i in "hello world":
    print(i)

# countdown timer

for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)
print("happy new year")
