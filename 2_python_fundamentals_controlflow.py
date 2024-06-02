#Control flow statements (if/else, loops)

# if statement
a = 5
b = 10

if a < b:
    print("a is less than b")

# if statement with elif
a = 5
b = 10
if a < b:
    print("a is less than b")
elif a == b:
    print("a is equal to b")
else:
    print("a is greater than b")

# if statement with else
a = 5
b = 10
if a < b:
    print("a is less than b")
else:
    print("a is greater than b")

# Switch statement
a = 5
b = 10
c = 15

match a:
    case 5:
        print("a is 5")
    case 10:
        print("a is 10")
    case 15:
        print("a is 15")
    case _:
        print("a is not 5, 10, or 15")

# while loop
a = 0
while a < 5:
    print(a)
    a += 1

# for loop
for i in range(5):
    print(i)

# break and continue
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

# for loop without range
for i in [1, 2, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
    print(i)

# for loop with range
for i in range(1, 21):
    print(i)

# for loop with range and step
for i in range(1, 21, 2):
    print(i)

# for loop with reversed range
for i in range(20, 0, -1):
    print(i)

# for loop with reversed range and step
for i in range(20, 0, -2):
    print(i)

# break and continue in for loop
for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 3:
        continue
    print(i)

# break and continue in for loop without range
for i in [1, 2, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
    if i == 3:
        break
    print(i)

for i in [1, 2, 5, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
    if i == 3:
        continue
    print(i)


