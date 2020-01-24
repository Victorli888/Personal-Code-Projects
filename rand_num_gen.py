import random

print("How many numbers should be in this list?")
number = int(input(" "))
print("How high do you want it to go?")
max = int(input(" "))

for i in range(0,number):
    print(random.randint(1,max), end=' ')

