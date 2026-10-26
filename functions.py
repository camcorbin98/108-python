#A function is a block of code that only runs when it is called
#We can pass dataa to a flunctions (parameters), and they can retrn data.

# def function_name(parameters):
#           code block(indented)
#           reform actions using the parameters
#           return value optional

#Simple funcrtion without parameters
def my_function():
    print("This is my function")

my_function()

#Function with parameters
#Parameter allow us to pass information into a function
def print_full_name(fname, lname):
    print(f"The name is:{fname}{lname}")

print_full_name("Leo", "Flores")
def get_full_name(fname, lname):
    return f"{fname, lname}"

full_name = get_full_name("Leo", "Flores")
print(full_name)

# Functions with default parameters
# A default parameter means the function will use that value,
# if no argument is provided when calling the function
def greet(name="Student"):
    print(f"Hello, {name}! Welcome to class.")

greet()
greet("Leo")

# Passing a list into a function
def print_items(items):
    for item in items:
        print("-", item)

print_items(["apple", "banana", "cherry"])

# MINI CHALLENGE: PASSWORD STRENGTH

# Create a function
def check_password(password):
    if len(password) >= 8:
        return "Strong Password"
    elif len(password) >= 5:
        return "Medium Password"
    else:
        return "Weak Password"


# Ask the user to enter a password
password = input("Enter your password: ")

# Call the function and store the result
result = check_password(password)

# Print the result
print(result)

# BONUS: Check for special character
if "!" in password:
    print("Special character detected!")


