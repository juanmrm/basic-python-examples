# two dimensional list
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Access 2d list element
print(number_grid[2][1])

# Nested for loop
for row in number_grid:
    for col in row:
        print(col)