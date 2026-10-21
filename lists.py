my_list = [1, 2, 3, 4, 5]
print(my_list)

# Mixed list
mix_list = [1, "apple", 3.5, True]
print(mix_list)

# Accessing items by INDEX- index starts at 0
fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[1])
print(fruits[2])

print(fruits[-1])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numbers[2:5])
print(numbers[:4])
print(numbers[6:])
print(numbers[-3:])
print(numbers[::2])

# modifying list items
fruits[1] = "mango"
print(fruits)

# Adding Items
fruits.append("orange")
print(fruits)

fruits.insert(1, "kiwi")
print(fruits)

fruits.extend(["grape", "pear"])
print(fruits)

fruits.remove("apple")
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(0)
print(fruits)

fruits.clear()
print(fruits)

for fruit in fruits:
    print(fruit)
print(len(fruits))

numbers = [4, 2, 6, 1, 7, 9]
print(numbers.count(2))
print(numbers.index(1))

numbers.sort()
print(numbers)

numbers.sort(reverse=True)
print(numbers)

numbers.reverse()
print(numbers)


"""
MINI CHALLENGE: THE GROCERY LIST
"""

# 1. Create a list with at least 5 grocery items
groceries = ["bread", "apples", "bananas", "chicken", "rice"]

# 2. Print the first and last items using indexing
print(f"First item: {groceries[0]}")
print(f"Last item: {groceries[-1]}")

# 3. Print the first 3 items using slicing
print(f"First 3 items: {groceries[:3]}")

# 4. Add eggs to the end of the list
groceries.append("eggs")

# 5. Insert milk at the beginning of the list
groceries.insert(0, "milk")

# 6. Remove one item from the list
groceries.remove("rice")

# 7. Check if bread is in the list
if "bread" in groceries:
    print("Bread is on the grocery list!")
else:
    print("Bread is not on the grocery list!")

# 8. Sort the list alphabetically
groceries.sort()
print(f"Sorted grocery list: {groceries}")

# 9. Print the total number of items
print(f"Total grocery items: {len(groceries)}")




