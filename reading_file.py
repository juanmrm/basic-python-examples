# Open the file in read mode
employee_file = open("employees.txt", "r")

# Whether or not we can read the file
print("Readable: " + str(employee_file.readable()))

# Read all file
# print(employee_file.read())

# Read a line
# print(employee_file.readline())

# Read all lines and return and array
for employee in employee_file.readlines():
    print(employee)

# Close the file when we finish working with the file
employee_file.close()