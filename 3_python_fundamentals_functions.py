# Define functions in Python

# Define a function to print a value
# Syntax def <function_name>(<arguments>):
def print_value(value):
    print("1 Param Functions")
    print(value)
    print()


def no_param():
    print("No Params")
    print()

#Multiple args function
def multiple_params(param1, param2):
    print("2 Params Functions")
    print(param1)
    print(param2)
    print()

# *args params function
def multiple_params(*args):
    print("Multiple Params Functions")
    print(args)
    for i in args:
        print(i)
    print()

def keywords_function(key3,key2,key1):
    print("Keyword Params Functions")
    print(key1)

def keywords_function(**kwargs):
    print("Variable size Keyword Params Functions")
    print(kwargs)
    for i in kwargs:
        # print(i)
        print(kwargs[i])
    print()

#function with a default value
def default_function(param1="Hello", param2="World"):
    print("Default Params Functions")
    print(param1)
    print(param2)
    print()

#define a function with list param
def list_param(list):
    print("List as Param Functions")
    print(list)
    for i in list:
        print(i)
    print()

def no_body():
    pass

#Positional arguments function
def positional_arguments(param1, param2, / , param3, param4):
    print("Positional Arguments Functions")
    print(param1)
    print(param2)
    print()

def keywordonly_function(*, param1, param2):
    print("Keyword Only Arguments Functions")
    print(param1)
    print(param2)
    print()




# Call the function
print_value("Hello, World!")
print_value(5)
no_param()
multiple_params("Hello", "World")
multiple_params("Hello", "World", "Python", "Programming")
keywords_function(key1="Hello",key2="World",key3="Python",key4="Programming")
keywords_function(key1="Hello",key2="World",key3="Python")
default_function("Hello")
list_param([1,2,3,4,5])
positional_arguments(1,2,param4=5,param3=3)
keywordonly_function(param1="Hello", param2="World")
no_body()