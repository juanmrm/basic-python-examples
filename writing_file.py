# Open the file in append mode adding characters to the end of the file
employee_file = open("employees.txt", "a")

employee_file.write("\nTobby - Human Resources")

# Close the file when we finish working with the file
employee_file.close()

# Open in write mode (overwrite entire file)
employee_file = open("employees.txt", "w")

employee_file.write("\nTobby - Human Resources")

# Close the file when we finish working with the file
employee_file.close()

