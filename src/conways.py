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

def sum_of_neighbors(cell):
    x = cell[1]
    y = cell[0]
    neighbors = [grid[y-1][x-1], grid[y-1][x], grid[y-1][x+1], grid[y][x-1], grid[y][x+1], grid[y+1][x-1], grid[y+1][x], grid[y+1][x+1]]

    neighbor_total = 0
    for i in neighbors:
        if i not None:
            neighbor_total += i

    return neighbor_total

    for cell in grid:
        if cell == 1:
            if sum_of_neighbors < 2:
                return 0
            elif sum_of_neighbors < 4:
                return 1
            else:
                return 0
        else:
            if sum_of_neighbors == 3:
                return 1
            else:
                return 0

 
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
