# This is a sample Python file that contains a list of names and ages.
NAME = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
AGES = [25, 30, 35, 40, 45]

ALICE =NAME[0] #Assign the first name in the NAME list to a variable
BOB = NAME[1] #Assign the second name in the NAME list to a variable

ALICE_BOB=NAME[0:2] #Assign the first two names in the NAME list to a variable
CHARLIE_EVE=NAME[2:] #Assign the third name to the end of the NAME list to a variable
REVERSED_NAME=NAME[::-1] #Assign the NAME list in reverse order to a variable
EVERY_OTHER_NAME=NAME[::2] #Assign every other name in the NAME list to a variable
print("===================")
print(ALICE) #Print the first name in the NAME list
print(BOB) #Print the second name in the NAME list
print(sum(AGES)) #Print the sum of all ages in the AGES list
print(min(AGES)) #Print the minimum age in the AGES list
print(max(AGES)) #Print the maximum age in the AGES list    
print(len(NAME)) #Print the number of names in the NAME list
print("===================")
print(ALICE_BOB) #Print the first two names in the NAME list
print(CHARLIE_EVE) #Print the third name to the end of the NAME list
print(REVERSED_NAME) #Print the NAME list in reverse order
print(EVERY_OTHER_NAME) #Print every other name in the NAME list

i = 0
# While loop runs as long as the condition is true
while i < len(NAME):
    print(NAME[i], AGES[i])
    i += 1
# For loop iterates over each name in the NAMES list
for name in NAME:
    print(name)
# For loop iterates over both names and ages using the zip function
for name, age in zip(NAME, AGES):
    print(f"{name} {age}")
# For loop iterates over the NAMES list in reverse order
for name in reversed(NAME):
    print(name)
# For loop iterates over a range of numbers from 0 to 4
for i in range(5):
    print(i)
# enumerate function provides both the index and the value of each item in the NAMES list
for i, name in enumerate(NAME):
    print(f"{i} {name}")