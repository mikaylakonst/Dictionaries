# Make a dictionary
phonebook = {
"Jasmine" : 123,
"Sonja" : 456,
"Liz" : 789
}

print(phonebook)

# Look up a value
print(phonebook["Sonja"])

# Update a value
phonebook["Sonja"] = 777
print(phonebook["Sonja"])


# Add an item
phonebook["Lisa"] = 888
print(phonebook)

# Delete an item
del phonebook["Liz"]
print(phonebook)

# Check if someone is in the phonebook
print("Jasmine" in phonebook)
print("Soliana" in phonebook)


# Go through the keys in the dictionary
for key in phonebook:
    print(key)


# Go through the key, val pairs in a dictionary
for key, val in phonebook.items():
    print("Key: " + key + "\tVal: " + str(val))


# Clear the dictionary
phonebook.clear()
print(phonebook)


# Make an empty dictionary
empty_dict = {}
print(empty_dict)
