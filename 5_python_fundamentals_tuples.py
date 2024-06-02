# Define a tuple
numbers_tuple = (10, 12, 23, 34, 75)
string_tuple = ("Hello", "World", "Python", "Java")
mixed_tuple = (1, "Hello", True, 2.5)

# Print tuple
print("Printing tuple Elements")
print(numbers_tuple)
print(string_tuple)
print(mixed_tuple)
print()

# Access tuple elements
print("Access tuple elements")
print(numbers_tuple[0])
print(string_tuple[1])
print(mixed_tuple[3])
print()


# # Update tuple elements
# numbers_tuple[0] = 100
# print("Update tuple elements")
# print(numbers_tuple)
# print()

# # Type Function
# numbers_tuple = tuple((100,))
# print("Update tuple elements")
# print(numbers_tuple)
#
# print(type(numbers_tuple))
# print(type(5))
# print(type(5.1))
# print(type("string"))
# num_list = [1, 2, 3]
# print(type(num_list))
# print(type(True))
# print(type(None))
# print()

#Negative indexes
print("Negative indexes")
#  0   1   2   3   4
#(10, 12, 23, 34, 75)
# -5  -4  -3  -2  -1
print(numbers_tuple[-1])
print()

#Range of Indexes
print("Range of Indexes")
#(10, 12, 23, 34, 75)
list_numbers = [10, 12, 23, 34, 75]
print(numbers_tuple[1:3])
print(numbers_tuple[1:])
print(numbers_tuple[:3])
print(list_numbers[:-3])
print()

#Range of Negative Indexes
print("Range of Negative Indexes")
print(numbers_tuple[-3:-1])
print(numbers_tuple[-3:])
print(numbers_tuple[:-1])
print()


#Item exists
print("Item exists")
print(100 in numbers_tuple)
print()

#Change tuple values
print("Change tuple values")
numbers_tuple = (100, 200, 300)
print(numbers_tuple)
number_list = list(numbers_tuple)
number_list.append(400)
numbers_tuple = tuple(number_list)
print(numbers_tuple)
print()

#Add tuple to a tuple
print("Add tuple to a tuple")
numbers_tuple = numbers_tuple + (500,1000)
print(numbers_tuple)
print()

#Delete tuple elements
print("Delete tuple elements")
number_list = list(numbers_tuple)
number_list.remove(500)
numbers_tuple = tuple(number_list)
print(numbers_tuple)
print("Delete tuple")
# del numbers_tuple
# print(numbers_tuple)
# print()

#Packing and Unpacking tuples
numbers_tuple = (10, 12, 23, 34, 75)
a, b, c, d, e = numbers_tuple
print("Packing and Unpacking tuples")
print(a)
print(b)
print(c)
print(d)
print(e)
print()


#Using Astrick
numbers_tuple = (10, 12, 23, 34, 75)
a, *b, c = numbers_tuple
print("Using Astrick")
print(a)
print(b)
print(c)
print()

#Loop through tuple
numbers_tuple = (10, 12, 23, 34, 75)
print("Loop through tuple")
for i in numbers_tuple:
    print(i)
print()

#While loop tuple
numbers_tuple = (10, 12, 23, 34, 75)
print("While loop tuple")
i = 0
while i < len(numbers_tuple):
    print(numbers_tuple[i])
    i += 1
print()

#Join 2 tuples
numbers_tuple = (10, 12, 23, 34, 75)
string_tuple = ("Hello", "World", "Python", "Java")
print("Join 2 tuples")
print(numbers_tuple + string_tuple)
print()

#multiply tuple
numbers_tuple = (10, 12, 23, 34, 75)
print("multiply tuple")
print(numbers_tuple * 2)
print()

#tuple methods
numbers_tuple = (10, 12, 23, 34, 75)
print("tuple methods")
print(len(numbers_tuple))
print(max(numbers_tuple))
print(min(numbers_tuple))
print(sum(numbers_tuple))
print(sorted(numbers_tuple))
print(tuple(range(1, 100, 3)))
print()










