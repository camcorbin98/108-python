#Sets are unordered, unindexed, and have no duplicates
fruits = ("apple", "banana", "cherry")
print(fruits)

# No Duplicates Allowed
fruits = ("apple", "banana", "apple")
print(fruits)

# remove duplicates form a list
emails = ["a@.com", "a@.com", "a@.com", "a@.com", "a@.com", "a@.com"]
unique_emails = set(emails)
print(unique_emails)
print(list(unique_emails))

#adding items
fruits.add("orange")
print(fruits)

# adding multiple items
fruits.update(["kiwi", "mango"])
print(fruits)

#removing an item
fruits.remove("banana")
print(fruits)

fruits.discard("water")
print(fruits)

#SET OPERATIONS (like in math)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.symetric_difference(set2))


"""
MINI CHALLENGE: STUDY GROUPS
"""

# 1. Create two sets of study groups
group_a = {"Leo", "Sam", "Alex", "Nina"}
group_b = {"Nina", "Jordan", "Sam", "Taylor"}

print("Group A:", group_a)
print("Group B:", group_b)

# 2. Find students in both groups
both_groups = group_a.intersection(group_b)
print("Students in both groups:", both_groups)

# Find students in exactly one group
one_group = group_a.symmetric_difference(group_b)
print("Students in exactly one group:", one_group)

# 3. Create a sign-in list with duplicate names
signed_in = ["Leo", "Nina", "Leo", "Maya", "Nina", "Sam"]

# Convert the list into a set to remove duplicates
unique_students = set(signed_in)

# Print how many different students showed up
print("Total different students:", len(unique_students))

# 4. Find students from group A who did not show up
absent_students = group_a.difference(unique_students)
print("Group A students who did not show up:", absent_students)

# 5. Combine both groups
all_students = group_a.union(group_b)

# Find students who showed up but are not in either group
unregistered = unique_students.difference(all_students)

# 6. Check for unregistered students
if len(unregistered) == 0:
    print("Everyone belongs to a group!")
else:
    print("Unregistered students:", unregistered)







