import pygame, random
 
# Define some colors and other constants
BLUE = (66, 87, 245)
WHITE = (255, 255, 255)
PINK = (242, 172, 241)
GRAY = (228, 230, 235)
WIN_SIZE = 505

WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 15






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
 
# -------- Main Program Loop -----------
def new_grid():
    grid = []
    for row in range(20):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(20):
            grid[row].append(1)  # Append a cell
    # grid[9][10] = 1
    # grid[10][10] = 1
    # grid[11][10] = 1
    return grid

grid = new_grid()

# grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]



while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    # --- Game logic should go here
    '''
    Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    Any live cell with two or three live neighbours lives on to the next generation.
    Any live cell with more than three live neighbours dies, as if by overpopulation.
    Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    '''
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
        for row in range(20):
            for column in range(20):
                if grid[row][column] == 1:
                    if sum_of_neighbors(grid, (row,column)) < 2:
                        grid[row][column] = 0
                    elif sum_of_neighbors(grid, (row,column)) < 4:
                        grid[row][column] = 1
                    else:
                        grid[row][column] = 0
                else:
                    if sum_of_neighbors(grid, (row,column)) == 3:
                        grid[row][column] = 1
                    else:
                        grid[row][column] = 0
        return grid
    

    next_gen(grid)

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    for row in range(20):
        for column in range(20):
            color = PINK
            if grid[row][column] == 1:
                color = BLUE
            pygame.draw.circle(screen,
                                color,
                                (((column+1)*22)+15, ((row+1)*22)),
                                10)
   
#    circle(surface, color, center, radius)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
