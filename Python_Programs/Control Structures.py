# IF/ELSE STATEMENTS 
# Don't forget the colon at the end of if statement: and after the else:
print("If/Else Statements")
x = 30
y = 29

if x > y:
    print("No shit")
else:
    print("you dumb")
print("""""")

# ELIF STATEMENTS (short for else if)
# Same thing for the elif statements
print("Elif Statements")
num = 42 

if num < 12:
    print("Num is less than 12")
elif num == 32:
    print("Num is equal to 32")
elif num > 33:
    print("Num is larger than 33")
else:
    print("Error")
print("""""")

# BOOLEAN LOGIC
# Python uses words for its Boolean operators, 
# whereas most other languages use symbols such as &&, || and !
print("Boolean Logic")
if 1 == 1 and 2 == 2:
    print(True)
if 1 == 2 or 3 == 3:
    print(True)
if not 2 < 4:
    print(True)
print("""""")

# WHILE LOOPS
# Don't forget the colon at the end of the statement
print("While Loops")
i = 0
while i <= 5:
    print(i)
    i = i + 1
print("Finished")
print("""""")

# LISTS 
# Lists are a type of object in Python that used to 
# store an indexed list of items.
print("List Basics")
blankList = []
print(blankList)
print("""""")

# You can include different types in lists or lists within lists
number = 43
names = ["Bob", [1, 2, number], "Kyle", "Rob"]
print(names[0])
print(names[1])
print(names[2])
print(names[3])
print("""""")

# Even certain indexes in a list can be reassigned
rowOfNumbers = [1, 2, 3, 4, 5]
rowOfNumbers[3] = 7
print(rowOfNumbers)
print("""""")

# LIST FUNCTIONS

# You can add to an already existing list using append
# As well as using len function to get the number of list elements
print("List Functions")
allTheNums = [2, 7, 8, 12, 6]
allTheNums.append(4)
print(allTheNums)
print(len(allTheNums))
print("""""")