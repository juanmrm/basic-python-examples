# We can put diferent type of objects
# items = ["Kevin", 2, False]

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)

# Print third element, from the begining
print(friends[2])

# Indexing from the back of the list
print(friends[-1])

# Take a range
print(friends[1:])

# Append another list to the end of the current list
friends.extend(lucky_numbers)
print(friends)
for lucky_number in lucky_numbers:
    friends.remove(lucky_number)

# Add individual elements to a list
friends.append("Creed")
print(friends)

# Insert an element in a position
friends.insert(1, "Kelly")
print(friends)

# Remove an element
friends.remove("Jim")
print(friends)

# Remove last element in the list
print(friends.pop())

# See if an element exists
print(friends.index("Kevin"))

# Count how many times an element appears
print(friends.count("Jim"))

# Sort elements in ascending
friends.sort()
print(friends)

# Reverse
friends.reverse()
print(friends)

# Make a Copy of a list
friends2 = friends.copy()

# Remove all elements
friends.clear()
print(friends)


