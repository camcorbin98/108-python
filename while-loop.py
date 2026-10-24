#Infinite Loop
count = 1

while count <= 5:
    print("Count is", count)
    count += 1 #Add one to count so condition becomes False

print("------------------------")

# Using break to stop the loop 
number = 0
while True: # infinite loop
    print(number)
    number += 1
    if number == 5:
        break

print("----------------------------")

#using CONTINUE to skip an iteration
count = 0
while count < 5:
    count += 1
    if count == 3:
        continue
    print(count)
else:
    print("loop finished")

#WHile loops with LISTS
tasks = ["dishes", "homework", "walk dog"]

while tasks:
    current = tasks.pop()
    print("Doing:", current)

# HANDLING BAD INPUT (try/ except)
# 
#
while True:
    answer = input("Enter a whole number: ")
    try: 
        number = int(answer)
        break
    except ValueError:
        print("Thats not a whole number, try again")

print(f"Thanks! You entered {number}")

# MINI CHALLENGE: Password Gate
# 1. Ask the user to enter a password
# 2. Check if it's correct (password: "secret123")
# 3. If it's wrong, print "Wrong! Try again." and ask again
# 4. When they enter the correct password, print "Access granted!"
# Solution:
password = ""                        # Start empty
while password != "secret123":       # Keep looping while password is wrong
    password = input("Enter password: ")
    if password != "secret123":      # If wrong
        print("Wrong! Try again.")
# Once they finally type "secret123", the while condition (password != "secret123") becomes false, so the loop stops.
print("Access granted!")








