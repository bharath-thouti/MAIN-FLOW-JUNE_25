# Creating a list
list_1 = [1, 2, 3, 4, 5, 6]

# Adding an element to the list
print("List after adding an element:", list_1)

# Removing an element from the list
list_1.remove(3)
print("List after removing an element:", list_1)

# Modifying an element in the list
list_1[2] = 10
print("List after modifying an element:", list_1)


# Creating a dictionary
dict_1 = {'a': 1, 'b': 2, 'c': 3}

# Adding a key-value pair to the dictionary
dict_1['d'] = 4
print("Dictionary after adding a key-value pair:", dict_1)

# Removing a key-value pair from the dictionary
del dict_1['b']
print("Dictionary after removing a key-value pair:", dict_1)

# Modifying a value in the dictionary
dict_1['c'] = 30
print("Dictionary after modifying a value:", dict_1)


# Creating a set
set_1 = {1, 2, 3, 4, 5}

# Adding an element to the set
set_1.add(6)
print("Set after adding an element:", set_1)

# Removing an element from the set
set_1.remove(3)
print("Set after removing an element:", set_1)

# Sets do not support indexing, but you can use the discard method to remove an element if it exists
set_1.discard(4)
print("Set after discarding an element:", set_1)
