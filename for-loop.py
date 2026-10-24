#A for loop in Python is a control structure that lets you repeat a block of code for each item in a sequence.

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

print("---------------------------------")

for letter in "Hello":
    print(letter)

print("---------------------------------")

for x in range(5):
    print(x)

print("----------------------------------")

#START and END range()
for x in range(2, 6):
    print(x)

print("-----------------------------------")

#STEP (skip numbers)
for x in range(0, 10, 2):
    print(x)

print("--------------------------------------")

# ELSE in for loops
for x in range (3):
    print(x)

else:
    print("loop done")

print("--------------------------------------")

# else is most useful with Break:

for number in [3, 7, 9]:
    if number % 2 == 0:
        print("Found an even number")
        break #stops the loop completely
else:
    print("no even numbers found")

print("-----------------------------------")

#BREAK and CONTINUE
for x in range(10):
    if x == 5:
        continue
    if x == 8:
        break
    print(x)


"""
MINI CHALLENGE: MULTIPLICATION TABLE
"""

# 1. Ask the user to enter a number
num = int(input("Enter a number: "))

print("-----------------------------------")

# 2. Use a for loop with range(1, 11)
for i in range(1, 11):

    # 3. Multiply num by the current loop value
    result = num * i

    # Print the multiplication result
    print(f"{num} x {i} = {result}")

print("-----------------------------------")




