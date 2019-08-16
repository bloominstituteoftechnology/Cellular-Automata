import pygame, random
 





# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
BLUE = (0,0,255)
WIN_SIZE = 500



WIDTH = 20
HEIGHT = 20
MARGIN = 5
grid = []
generation = 0
is_paused = False 


for row in range(20):
    grid.append([])
    for column in range(20):
        grid[row].append(0)
# 1. create a set of inital states with simple patterns blinker?
# cur_states = [0] * 400
# cur_states[0:1] = '1'
# cur_states[1:2] = '1'
# cur_states[2:3] = '1'
# cur_states[42:43] = '1'

    # if event.type == pygame.MOUSEBUTTONDOWN:# and #our button clicked looking at coordinates
    #     is_paused = not is_paused

    # if event.type == pygame.MOUSEBUTTONDOWN:# and #our button clicked looking at coordinates
    #     is_paused = not is_paused
    #     # generation 0
    #     # curstate = initial states


def sumOfNeighbors(grid, row, column):

    # for i in range 20:
        # for row
    
    r = row
    rplus = row + 1
    rminus = row - 1
    c = column
    cplus = column + 1
    cminus = column - 1
    # e = grid[r][cminus]
    try:
        e = grid[r][cminus]
    except IndexError:
        e = 0
        # dont increment total
    try:
        w = grid[r][cplus]
    except IndexError:
        w = 0
    
    try:
        n = grid[rminus][c]
    except IndexError:
        n = 0
        
    try:
        s = grid[rplus][c]
    except IndexError:
        s = 0
    
    try:
        ne =  grid[rminus][cplus]
    except IndexError:
        ne = 0
    
    try:
        nw = grid[rminus][cminus]
    except IndexError:
        nw = 0
        
    try:
        se = grid[rplus][cplus]
    except IndexError:
        se = 0

    try:
        sw = grid[rplus][cminus]
    except IndexError:
        sw = 0
        
    value = n + s + e + w + ne + nw + se + sw
    return value


grid[0][0] = 1
grid[0][1] = 1
grid[0][2] = 1
grid[0][3] = 1  

# randomizes the grid 20 by 20 grid
for i in range(20):
    for j in range(20):
        grid[i][j] = random.randint(0,1)


# cur_states[0:5] = '1'
# cur_states[5:6] = '1'
# cur_states[20:21] = '1'
# print(cur_states[10])

next_states = []


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
    generation += 1
    pygame.display.set_caption(f"Conway’s Game of Life Generation: {generation}")
    new_state = grid
    # --- Game logic should go here
    for row in range(20):
        for column in range(20):    
            if grid[row][column] == 1:
                # print(sumOfNeighbors(grid, row, column))
                if sumOfNeighbors(grid, row, column) < 2:
                    
                    new_state[row][column] = 0
                elif sumOfNeighbors(grid, row, column) < 4:
                    new_state[row][column] = 1
                else:
                    new_state[row][column] = 0
            else:
                if sumOfNeighbors(grid, row, column) == 3:
                    new_state[row][column] = 1
                else:
                    new_state[row][column] = 0
            
    
# rules
# 1. any live cell with fewer than to live neighbours dies
# 2. any live cell with two or three live neighbours lives on to the next generation
# 3. any live cell with more than three live neighbours dies
# 4. any dead cell with exactly three live neighbours becomes a live cell

# work on rulse that i look at all neighbours 
        # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
    # x = 5
    # cur_index = 0
    # --- Drawing code should go here
    # for i in range(500):
    for row in range(20):
        for column in range(20):
            color = BLACK
            if grid[row][column] == 1:
                color = WHITE
            pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

    # sumOfNeighbors():
    

    pause_button = pygame.draw.rect(screen, BLUE , pygame.Rect(200, 425, 50, 25))
    font = pygame.font.SysFont('Arial', 25)
    text = font.render('Play/Pause', True, (14, 28, 54))
    screen.blit(text,pause_button)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
