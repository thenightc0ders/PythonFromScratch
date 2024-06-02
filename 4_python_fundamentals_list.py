# Define a list
numbers_list = [10, 12, 23, 34, 75]
          #      0   1   2   3   4
string_list = ["Hello", "World", "Python", "Java"]
mixed_list = [1, "Hello", True, 2.5]

# Print list
print("Printing List Elements")
print(numbers_list)
print(string_list)
print(mixed_list)
print()

# Access list elements
print("Access list elements")
print(numbers_list[0])
print(string_list[1])
print(mixed_list[3])
print()

# Update list elements
numbers_list[0] = 100
string_list[2] = "Programming"
mixed_list[3] = False
print("Update list elements")
print(numbers_list)
print(string_list)
print(mixed_list)
print()

#Append to list
#numbers_list = [10, 12, 23, 34, 75]
numbers_list.append(6)
print("Append to list")
print(numbers_list)
print()

# Delete list elements
del numbers_list[3]
print("Delete list elements")
print(numbers_list)
print()

# Create a list
#numbers_list = [10, 12, 23, 34, 75]
numbers_list = list(range(1, 100, 3))
print("Create a list")
print(numbers_list)
print()


# iterate over list
print("Create a list")
for i in numbers_list:
    print(i**2)
print()

#Comprehension in list
numbers_list_temp = [i for i in numbers_list if i % 2 == 0]
print("Comprehension a list")
print(numbers_list_temp)
print()

#Sort list
numbers_list = [2, 23, 34, 5, 75, 10]
numbers_list.sort()
print("Sort list")
print(numbers_list)
print()

#Join List
mixed_list.extend(string_list)
print("Join List")
print(mixed_list)
print()

#Copy list
numbers_list_copy = numbers_list.copy()
print("Copy list")
print(numbers_list_copy)
print("Original list appended")
numbers_list.append(101)
print(numbers_list)
print()

#List Methods
print("List Methods")
print("Length:", len(numbers_list))
print("Max: ", max(string_list))
print("Min: ", min(string_list))
print("Sum: ", sum(numbers_list))
print("Sorted: ", sorted(string_list))
print("Any: ", any(numbers_list))
print("All: ", all(numbers_list))
print("Count: ", numbers_list.count(1))
print("Number at index 101: ", numbers_list.index(101))
print("Search number 101 from index 0: ", numbers_list.index(101, 1))
print("Search number 101 from index 0 and stop at 4: ", numbers_list.index(101, 0, 1000))
print(numbers_list)
print("Search number 101 from index 0: ", numbers_list.insert(0, 102))
print("Print List: ", numbers_list)
print("Pop number at index 0: ", numbers_list.pop(0))
print("Print List: ", numbers_list)
print("Remove number at index 1: ", numbers_list.remove(101))
print("Print List: ", numbers_list)
print("Reverse List: ", numbers_list.reverse())
print("Print List: ", numbers_list)
# print()






























#

#

#

#

#

#

#

#
#

#

#

