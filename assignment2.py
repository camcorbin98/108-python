
"""
Assignment 2: Practice with Python lists and dictionaries.
"""

# PART 1: LISTS

# 1. Create a new list of places I would like to visit.
places = ["Sedona", "Flagstaff", "San Diego", "Denver", "Los Angeles"]
print("Original list:", places)
print("List length:", len(places))

# 2. Access items by their index.
print("First place:", places[0])
print("Last place:", places[-1])
print("List:", places)
print("List length:", len(places))

# 3. Replace a value in the list.
places[3] = "Seattle"
print("After replacing Denver with Seattle:", places)
print("List length:", len(places))

# 4. Remove an item by its value.
places.remove("San Diego")
print("After removing San Diego:", places)
print("List length:", len(places))


# PART 2: DICTIONARIES

# 1. Create a new dictionary with information about a hiking trip.
hiking_trip = {
    "destination": "Sedona",
    "difficulty": "Moderate",
    "distance_miles": 5
}
print("\nOriginal dictionary:", hiking_trip)
print("Dictionary length:", len(hiking_trip))

# 2. Access values using their keys.
print("Destination:", hiking_trip["destination"])
print("Difficulty:", hiking_trip["difficulty"])
print("Dictionary:", hiking_trip)
print("Dictionary length:", len(hiking_trip))

# 3. Add a new key and value.
hiking_trip["weather"] = "Sunny"
print("After adding weather:", hiking_trip)
print("Dictionary length:", len(hiking_trip))

# 4. Update an existing value.
hiking_trip["distance_miles"] = 7
print("After updating the distance:", hiking_trip)
print("Dictionary length:", len(hiking_trip))

# 5. Remove a key.
hiking_trip.pop("weather")
print("After removing weather:", hiking_trip)
print("Dictionary length:", len(hiking_trip))
