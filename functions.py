# define a function in lowercase and separate words with underscore (snake case)
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))


say_hi("Mike", 35)
say_hi("Steve", 70)


# using the return function to return a value back to the caller
def cube(num):
    return pow(num, 3)
    print("This is not going to be printed") # This code is unrecheachable


result = cube(4)
print(result)

