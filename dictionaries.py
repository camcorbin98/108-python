student = {
    "name": "Cam",
    "age": 28,
    "major": "Political Science"
}

print(student)

print(student["name"])
print(student.get("major"))

student["graduation_year"] = 2025
print(student)

student["age"] = 30
print(student)

student.pop("major")
print(student)

if "name" in student:
    print("yes name exists")

#Nested Dictionary
studentsss = {
    "student1":{"name": "Leo", "age": 20},
    "student2":{"name": "Alex", "age": 25}
}

print(studentsss["student2"]["name"])

"""
A list of dictionaries is like a table: each dictionary is one row (one record).
This is the shape of a store catalog, an api response (JSON) and the documnts,
stored in the database like MongoDB
"""


products = [
    {"id": 1, "title": "Mouse", "price": 14.99},
    {"id": 2, "title": "Keyboard", "price": 29.99},
]

print(products[0]["title"])

for product in products:
    # FIXED: Changed inner quotation marks
    print(f"{product['title']}: ${product['price']}")

products.append({"id": 3, "title": "Monitor", "price": 150.99})

print(products)
print(len(products))

# Create the student dictionary if not already defined
student = {
    "name": "Cam",
    "age": 28,
    "major": "Political Science"
}

# FIXED: Changed "gap" to "gpa"
student.update({"age": 19, "gpa": 3.8})

print(student)



"""
MINI CHALLENGE: STUDENT REPORT CARD
"""

# 1. Create a dictionary with student information
report_card = {
    "name": "Leo",
    "subject": "Math",
    "grades": (90, 85, 88)
}

# 2. Print the student's name and subject
print(f"Student Name: {report_card['name']}")
print(f"Subject: {report_card['subject']}")

# 3. Calculate the average grade
average = sum(report_card["grades"]) / len(report_card["grades"])

# 4. Add the average to the dictionary
report_card["average"] = average

# 5. Evaluate the student's performance
if average >= 90:
    print("Excellent!")

elif average >= 70:
    print("Good job!")

else:
    print("Needs improvement!")

# 6. Remove the subject key
report_card.pop("subject")

# Print the updated dictionary
print(report_card)
