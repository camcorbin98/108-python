"""
Dog Age Converter
Converts a dog's age in human years to dog years.
"""

# Ask the user for their dog's age
dogAge = int(input("How old is your dog in human years? "))

# Calculate the dog's age in dog years
dogYears = dogAge * 7

# Display the result using an f-string
print(f"Your dog is {dogYears} years old in dog years!")
print("Hello world from Python!")
print(2)
print(5 + 3)
print(True)

name = "Leo"
age = 24
print(name, age)

print("Hello my name is " + name + " and my age is " + str(age))

newName = "Cam"
newAge = 28
city = "Phoenix"
hoursStudying = 3.5
likesPython = True

print("My name is " + newName + ".")
print("I am " + str(newAge) + " years old.")
print("I currently live in " + city + ".")
print("I study programming for " + str(hoursStudying) + " hours a day.")
print("Do I enjoy learning Python? " + str(likesPython))

place = "disneyland"
activity = "riding the rollercoaster"
members = 5

# FIXED: Added missing spaces
print("The last time I went to " + place + ", I had a great time " + activity + " with " + str(members) + " people.")

print(type(name))
print(type(age))

user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")
print(type(input("Enter your name: ")))

new_age = int(input("Enter your age: "))
print(age + new_age)

# FIXED: Ask for slices first
slicesn = int(input("How many slices of pizza do you have? "))

# FIXED: Ask for people before calculating
people = int(input("How many people are sharing the pizza? "))

# FIXED: Calculate after both variables exist
slicesPerPerson = slicesn / people

print(f"Each person gets {slicesPerPerson} slices of pizza!")



