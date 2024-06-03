# Define Dictionary
numbers_dict = {
    10: "One",
    12: "Two",
    23: "Three",
    34: "Four",
    75: "Five"
}
string_dict = {"Hello": "World", "Python": "Programming", "Java": "Script"}
mixed_dict = {1: "Hello", True: "World", 2.5: "Python"}



# Print Dictionary
print("Printing Dictionary Elements")
print(numbers_dict)
print(string_dict)
print(mixed_dict)
print()

# Dictionary Constructor
# numbers_dict = dict({10: "One", 12: "Two", 23: "Three", 34: "Four", 75: "Five"})
# print("Dictionary Constructor")
# print(numbers_dict)
# print()

# Accessing elements of Dictionary
print("Accessing elements of Dictionary")
print(numbers_dict[10])
print(string_dict["Python"])
print(mixed_dict[2.5])
print()

# Access Elements using get Method
print("Access Elements using get Method")
print(numbers_dict.get(10))
print(string_dict.get("Python"))
print(mixed_dict.get(2.5))
print()

#Get keys method
print("Get keys method")
print(numbers_dict.keys())
print()

#Values method
print("Get values method")
print(numbers_dict.values())
print()
#

#Items method
print("Get items method")
print(numbers_dict.items())
print()

#Check is key exists in dictionary
print("Check is key exists in dictionary")
print(10 in numbers_dict)
print()

#Update Dictionary
numbers_dict[10] = "Ten"
print("Update Dictionary Elements")
print(numbers_dict)
print()

#Update using update method
numbers_dict.update({12: "Twelve", 23: "Twenty Three", 34: "Thirty Four", 75: "Seventy Five"})
print("Update using update method")
print(numbers_dict)
print()

#The pop method
numbers_dict.pop(10)
print("The pop method")
print(numbers_dict)
print()

#popitem method
popitem = numbers_dict.popitem()
print("The popitem method")
print(numbers_dict)
print(popitem)
print()


#del method to delete an intem
del numbers_dict[12]
print("The del method")
print(numbers_dict)
print()

# #del dictionary
# del numbers_dict
# print("The del dictionary")
# print(numbers_dict)
# print()

#clear method
# numbers_dict.clear()
# print("The clear method")
# print(numbers_dict)
# print()



#loop through dictionary
print("Loop through dictionary")
for i in numbers_dict:
    print(i)
print()

#loop through dictionary
print("Loop through dictionary")
for i in numbers_dict:
    print(numbers_dict[i])
print()

#loop through dictionary values
print("Loop through dictionary")
for i in numbers_dict.values():
    print(i)
print()

#loop through dictionary items
print("Loop through dictionary")
for i in numbers_dict.items():
    print(i)
print()

#loop through dictionary keys
print("Loop through dictionary")
for i in numbers_dict.keys():
    print(i)
print()

#copy and dict
numbers_dict = {10: "One", 12: "Two", 23: "Three", 34: "Four", 75: "Five"}
numbers_dict2 = numbers_dict.copy()
numbers_dict3 = dict(numbers_dict)
print("Copy and dict")
print(numbers_dict2)
print(numbers_dict3)
print()

# Dictionary with List Keys
numbers_dict = {
    10: ["One", "Two", "Three"],
    12: ["Four", "Five", "Six"],
    23: ["Seven", "Eight", "Nine"],
    34: ["Ten", "Eleven", "Twelve"],
    75: ["Thirteen", "Fourteen", "Fifteen"]
}
print("Dictionary with List Keys")
print(numbers_dict)
print()

# Length of Dictionary
print("Length of Dictionary")
print(len(numbers_dict))
print()

#Dictionary with Tuple Values
numbers_dict = {
    10: (1, 2, 3),
    12: (4, 5, 6),
    23: (7, 8, 9),
    34: (10, 11, 12),
    75: (13, 14, 15)
}
print("Dictionary with Tuple Values")
print(numbers_dict)
print()

#Dictionary with Set Values
numbers_dict = {
    10: {1, 2, 3},
    12: {4, 5, 6},
    23: {7, 8, 9},
    34: {10, 11, 12},
    75: {13, 14, 15}
}
print("Dictionary with Set Values")
print(numbers_dict)
print()

#Dictionary with Dictionary Values
print("Dictionary with Dictionary Values")
numbers_dict = {
    10: {"a": 1,
         "b": 2,
         "c": 3
         },
    12: {"d": 4,
         "e": 5,
         "f": 6
         }
}
print(numbers_dict)
print()


#Delete Dictionary Elements
del numbers_dict[10]
print("Delete Dictionary Elements")
print(numbers_dict)
print()


# Type Method
print("Type Method")
print(type(numbers_dict))
print()

