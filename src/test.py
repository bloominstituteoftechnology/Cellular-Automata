grid = []
for row in range(20):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(20):
        grid[row].append(0)  # Append a cell

grid[9][10] = 1
grid[10][10] = 1
grid[11][10] = 1

for i in grid:
    print(i)


def sum_of_neighbors(grid, cell):
    x = cell[1]
    y = cell[0]
    neighbors_coords = [(y-1,x-1), (y-1, x), (y-1, x+1),(y, x-1),(y, x+1),(y+1, x-1),(y+1, x),(y+1, x+1)]
    neighbors = []

    for coords in neighbors_coords:
        try:
            neighbors.append(grid[coords[0]][coords[1]])
        except IndexError:
            neighbors.append(None)

    neighbor_total = 0
    for i in neighbors:
        if i != None:
            neighbor_total += i


    return neighbor_total

def next_gen(grid):
    new_grid=[]
    for row in range(20):
    # Add an empty array that will hold each cell
    # in this row
        new_grid.append([])
        for column in range(20):
            new_grid[row].append(0)  # Append a cell
    for row in range(20):
        for column in range(20):
            if grid[row][column] == 1:
                if sum_of_neighbors(grid, (row,column)) < 2:
                    new_grid[row][column] = 0
                elif sum_of_neighbors(grid, (row,column)) < 4:
                    new_grid[row][column] = 1
                else:
                    new_grid[row][column] = 0
            else:
                if sum_of_neighbors(grid, (row,column)) == 3:
                    new_grid[row][column] = 1
                else:
                    new_grid[row][column] = 0
    return new_grid

gentwo = next_gen(grid)

print('')
print('')
for i in gentwo:
    print(i)


