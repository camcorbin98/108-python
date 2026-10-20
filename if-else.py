#An if-else statement in python is a conditional control structure that lets 
#you decide which blick of code to run depending on whether a condition is True or False

#if condition:
    #code black runs if condition is True
#elif another condition:
    #code black runs if the first condition is false and this one is true 

x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

if x > 5: print("x is greater than 5")

# Short hand if...else statements

print("Even") if x % 2 == 0 else print("odd")

if x > 0:
    if x < 20:
        print("x is a positive number less than 20")

age = 20

if age >= 18 and age <= 20:
    print("You are between 18 and 21")


"""
MINI CHALLENGE: Club Entry
Ask the user to enter their age and store it in a variable called age.
Ask the user if they have a valid ID.(The user should enter "yes" or "no".)
Store the answer in a variable called has_id.
Determine admission rules:
If age is 21 or older AND has_id is "yes":
   print "Access Granted"
If age is 21 or older BUT has_id is "no":
   print "Access Denied - ID Required"
If age is between 18 and 20 inclusive:
   print "Access Limited"
Otherwise:
   print "Access Denied - Too Young"
Create a variable called can_enter:
 Set it to True only if the user is 21 or older AND has_id is "yes".
 Otherwise set it to False.
BONUS:
 If can_enter is True:
     print "Welcome inside!"
 Otherwise:
     print "Please see the front desk."
EXTRA BONUS:
 If the user enters a negative age,
 print "Invalid age entered."
"""


"""
MINI CHALLENGE: Club Entry
"""

# Ask the user for their age
age = int(input("Enter your age: "))

# Ask the user if they have a valid ID
has_id = input("Do you have a valid ID? (yes/no): ").lower()

# Determine whether the user can enter
can_enter = age >= 21 and has_id == "yes"

# Check admission rules
if age < 0:
    print("Invalid age entered.")

elif age >= 21 and has_id == "yes":
    print("Access Granted")

elif age >= 21 and has_id == "no":
    print("Access Denied - ID Required")

elif age >= 18 and age <= 20:
    print("Access Limited")

else:
    print("Access Denied - Too Young")

# Bonus: Display welcome message
if can_enter:
    print("Welcome inside!")
else:
    print("Please see the front desk.")
