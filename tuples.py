#Tuples are immutable, you can't change them after creation.

my_tuple = ("apple", "banana", "cherry")
print(my_tuple)

#Accessing items
print(my_tuple[0])
print(my_tuple[-1])

#Tuples CANT be changed (try it) - to change convert to a list
temp_tuple = ("apple", "banana", "cherry")
temp_list = list(temp_tuple)
temp_list[0] = "kiwi"
temp_tuple = tuple()
print(temp_list)
print(temp_tuple)

#single item tuple
single = ("water",)
print(type(single))
not_tuple = ("apple")
print(type(not_tuple))

#Joining, slicing, and looping
more = ("date", "elderberry")
print(my_tuple + more) #Joins tuples into a NEW tuple
print(more * 2) #REPEATS a tuple
print(my_tuple[1:])
for item in my_tuple: #loops same as lists
    print(item)

#COUNT and INDEX methods
letters = ("a", "b", "a", "c", "a")
print(letters.count("a")) #how many times "a" appears
print(letters.index("c"))

#tuplen UNPACKING
#you can "unpack" a tuple"s items directly into seperate variables
coordinates = (10, 20)
x, y = coordinates
print(x)
print(y)


"""
MINI CHALLENGE: THE TRAVEL BAG
"""

# 1. Create a tuple with at least 5 travel items
travel_bag = ("shirt", "toothbrush", "shoes", "pants", "sunglasses")
print(travel_bag)

# 2. Print the second and fourth items
print(f"Second item: {travel_bag[1]}")
print(f"Fourth item: {travel_bag[3]}")

# 3. Check if shoes are in the travel bag
if "shoes" in travel_bag:
    print("You're ready to walk!")
else:
    print("You forgot your shoes!")

# 4. Create a new tuple with 3 essential items
essentials = ("passport", "wallet", "phone")
print(essentials)

# 5. Combine both tuples into one
final_bag = travel_bag + essentials
print(f"Final travel bag: {final_bag}")

# 6. Print the total number of items
print(f"Total items: {len(final_bag)}")

# 7. Print the last item in the final bag
print(f"Last item: {final_bag[-1]}")





