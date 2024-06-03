# Define a set
numbers_set = {10, 12, 23, 34, 75}
string_set = {"Hello", "World", "Python", "Java"}
mixed_set = {1, "Hello", True, 2.5}

# Print tuple 1 & True
print("Printing tuple Elements")
print(numbers_set)
print(string_set)
print(mixed_set)
print()

# Type() function
print("Type Function")
print(type(numbers_set))
print()

# Using set constructor
numbers_set = set((10, 12, 23, 34, 75))
print("Using set constructor")
print(numbers_set)
print()


#Loop through set items
print("Loop through set items")
for i in numbers_set:
    print(i)
print()

# # While loop through set items
# print("While loop through set items")
# i = 0
# while i < len(numbers_set):
#     print(numbers_set[i])
#     i += 1
# print()

#Convert set to list and access elements
print("Convert set to list and access elements")
numbers_list = list(numbers_set)
print(numbers_list)
print(numbers_list[0])
print()

#Check item preset in Set
print("Check item preset in Set")
print(10 in numbers_set)
print()

#Methods of Set
#Add items to Set
print("Add items to Set")
numbers_set.add(6)
print(numbers_set)
print()

#Add 2 Sets
print("Add 2 Sets")
numbers_set.update({7, 8, 9})
print(numbers_set)
print()

#Add list to a set (any iterable)
print("Add list to a set")
numbers_set.update([10, 11, 12, 12])
print(numbers_set)
print()

#Remove and discard from a Set
print("Remove and discard from a Set")
numbers_set.remove(11)
numbers_set.discard(12)
print(numbers_set)
print()

#Set pop method
print("Set pop method")
print(numbers_set)
print(numbers_set.pop())
print(numbers_set)
print()

#Clear Set
print("Clear Set")
numbers_set.clear()
print(numbers_set)
print()


# Join Sets
print("Join Sets")
numbers_set1 = {1, 2, 3, 4, 5, 6}
numbers_set2 = {6, 7, 8, 9, 10}
numbers_set3 = numbers_set1.union(numbers_set2)
print(numbers_set3)
print()

# Union
print("Union")
numbers_set1 = {1, 2, 3, 4, 5}
numbers_set2 = {6, 7, 8, 9, 10}
numbers_set3 = numbers_set1.union(numbers_set2)
print(numbers_set3)
numbers_set4 = numbers_set1 | numbers_set2
print(numbers_set4)
print()

# multi set union
print("multi set union")
numbers_set1 = {1, 2, 3, 4, 5}
numbers_set2 = {6, 7, 8, 9, 10}
numbers_set3 = {11, 12, 13, 14, 15}
numbers_set4 = numbers_set1.union(numbers_set2, numbers_set3)
print(numbers_set4)
numbers_set5 = numbers_set1 | numbers_set2 | numbers_set3
print(numbers_set5)
print(numbers_set1)
print()



# Intersection
print("Intersection")
numbers_set1 = {1, 2, 3, 4, 5, 6,11}
numbers_set2 = {6, 7, 8, 9, 10,11}
number_set0 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers_set3 = numbers_set1.intersection(numbers_set2, number_set0)
print(numbers_set3)
number_set3 = numbers_set1 & numbers_set2 & number_set0
print(number_set3)
print()

# Intersection Update
print("Intersection Update")
numbers_set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers_set2 = {6, 7, 8, 9, 10}
numbers_set1.intersection_update(numbers_set2)
print(numbers_set1)
print()

#Set update
print("Set update")
numbers_set1 = {1, 2, 3, 4, 5}
numbers_set2 = {6, 7, 8, 9, 10}
numbers_set1.update(numbers_set2)
print(numbers_set1)
print()


# Difference
print("Difference")
numbers_set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers_set2 = {6, 7, 8, 9, 10, 11}
numbers_set3 = numbers_set1.difference(numbers_set2)
print(numbers_set3)
numbers_set4 = numbers_set1 - numbers_set2
print (numbers_set4)
print()

# Difference Update
print("Difference Update")
numbers_set1 = {1, 2, 3, 4, 5}
numbers_set2 = {6, 7, 8, 9, 10}
numbers_set1.difference_update(numbers_set2)
print(numbers_set1)
print()

# Symmetric Difference
print("Symmetric Difference")
numbers_set1 = {1, 2, 3, 4, 5, 6}
numbers_set2 = {6, 7, 8, 9, 10}
numbers_set3 = numbers_set1.symmetric_difference(numbers_set2)
print(numbers_set3)
numbers_set4 = numbers_set1 ^ numbers_set2
print(numbers_set4)
print()

#Symmetric Difference Update
print("Symmetric Difference Update")
numbers_set1 = {1, 2, 3, 4, 5, 6, 7}
numbers_set2 = {6, 7, 8, 9, 10}
numbers_set1.symmetric_difference_update(numbers_set2)
print(numbers_set1)
print()

# Copy
print("Copy")
numbers_set1 = {1, 2, 3, 4, 5}
numbers_set2 = numbers_set1
print(numbers_set2)
print()

# Frozen Set
print("Frozen Set")
numbers_set1 = {1, 2, 3, 4, 5}
numbers_set2 = frozenset(numbers_set1)
numbers_set2.union({6, 7, 8, 9, 10})
print(numbers_set2)

#isDisjoint Set
print("isDisjoint Set")
numbers_set1 = {1, 2, 3, 4, 5, 6}
numbers_set2 = {6, 7, 8, 9, 10}
print(numbers_set1.isdisjoint(numbers_set2))

#isSubset
print("isSubset")
numbers_set1 = {1, 2, 3, 4, 5}
numbers_set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(numbers_set1.issubset(numbers_set2))

#isSuperset
print("isSuperset")
numbers_set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
numbers_set2 = {1, 2, 3, 4, 5}
print(numbers_set1.issuperset(numbers_set2))




































