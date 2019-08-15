import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (138, 43, 226)
GRAY = (25, 25, 25)
WIN_SIZE = 500
MATRIX_SIZE = 20

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def make_grid(x, y):
    grid = []
    for r in range(x): #rows
        row = []
        for c in range(y): #columns
            row.append(0) #initialize to 0
        grid.append(row) 
    return grid


def check_neighbors(grid, row, column):
    x = row
    y = column
    #neighbor directions: 
    ngb_cells = [(x-1,y-1),(x-1,0),(x-1,y+1),
                (x,y-1),        (x,y+1),   
                (x+1,y-1),(x+1,0),(x+1,y+1),]
    count = 0
    for x,y in ngb_cells:
        if x >= 0 and y >= 0:
            try:
                count += grid[x][y]
            except:
                pass
    
    return count

def cell_rules(cell, neighbors):
# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    #if cell is alive and has less than 2 or more than 3 neighbors it dies
    # otherwise it lives on
    if cell:
        if neighbors < 2 or neighbors > 3:
            return 0
        else:
            return 1
    # if cell is dead it must have 3 neighbors to come alive
    else:
        if neighbors == 3:
            return 1

def make_new_grid(grid):
    x = len(grid)
    y = len(grid[0])

    new_grid = make_grid(x, y)
    for row in range(x):
        for col in range(y):
            cell = grid[row][col]
            neighbors = check_neighbors(grid, row, col)
            new_grid[row][col] = cell_rules(cell, neighbors)
    return new_grid

#make starting grid
grid = make_grid(MATRIX_SIZE, MATRIX_SIZE)

# make testing blinker pattern
grid[2][1] = 1
grid[2][2] = 1
grid[2][3] = 1
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
    
    # 3. Work on rules that i) look at all neighbors, ii) save new state
    # in next_states[]
    tmp = 0
    if tmp < 10:
        temp = check_neighbors(grid, 2, 2)
        print(f"***********{temp}**************")
        tmp += 1
    else:
        pygame.quit()
    # new_grid = make_new_grid(grid)


    # if grid[row][column] == 1:
    #     if sum_of_neighbors(grid, (row,column)) < 2:
    #         grid[row][column] = 0
    #     elif sum_of_neighbors(grid, (row,column)) < 4:
    #         grid[row][column] = 1
    #     else:
    #         grid[row][column] = 0
    # else:
    #     if sum_of_neighbors(grid, (row,column)) == 3:
    #         grid[row][column] = 1
    #     else:
    #         grid[row][column] = 0

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    row = 0
    y = 3.5
    while y < WIN_SIZE:
        col = 0
        x = 3.5
        while x < WIN_SIZE:
            # draw based on current state
            state = grid[row][col]
            # draw based on next states
            if state == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, MATRIX_SIZE, MATRIX_SIZE))
            else:
                pygame.draw.rect(screen, BLUE, pygame.Rect(x, y, MATRIX_SIZE, MATRIX_SIZE))
            col += 1
            x += 25
        row += 1
        y += 25

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()