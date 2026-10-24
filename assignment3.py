# Assignment 3: Python Collections Comparison Table

print("PYTHON COLLECTIONS COMPARISON TABLE")
print("-" * 140)

# Table Headers
print(f"{'Data Structure':<17} {'Syntax Example':<32} {'Ordered':<10} {'Mutable':<10} {'Allows Duplicates':<25} {'Access Method'}")

print("-" * 140)

# List
print(f"{'List':<17} {'[1, 2, 2, 3]':<32} {'Yes':<10} {'Yes':<10} {'Yes':<25} {'Indexing [0]'}")

# Dictionary
dictionary_example = '{"name": "Cam", "age": 28}'
dictionary_access = 'Keys ["name"]'

print(f"{'Dictionary':<17} {dictionary_example:<32} {'Yes':<10} {'Yes':<10} {'Keys: No, Values: Yes':<25} {dictionary_access}")

# Set
print(f"{'Set':<17} {'{1, 2, 3}':<32} {'No':<10} {'Yes':<10} {'No':<25} {'Membership (in)'}")

# Tuple
print(f"{'Tuple':<17} {'(1, 2, 2, 3)':<32} {'Yes':<10} {'No':<10} {'Yes':<25} {'Indexing [0]'}")

print("-" * 140)