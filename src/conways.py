import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500

# 1. set up initial states

cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1
# next_states = []

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

    # 3. night 2: work on rules that i) look at all neighbors, ii) save new state in 
    # next_states[]

    current_index = 398
    # ADD LOGIC TO CHECK NEIGHBORS DEPENDING ON CURRENT INDEX! corners, upper 
    # a. find cur_rect's neighbors
    # b. find neighbor states
    neighbors = []
    # CORNER NEIGHBORS
    if current_index == 0:
        neighbors = [1, 20, 21]
    elif current_index == 19:
        neighbors = [18, 38, 39]
    elif current_index == 380:
        neighbors = [360, 361, 381]
    elif current_index == 399:
        neighbors = [378, 379, 398]
    # BORDER NEIGHBORS
    elif current_index in range(1, 19):
        neighbor_values = [-1, +1, 19, 20, 21]
        neighbors = [current_index + i for i in neighbor_values]
    elif current_index in range(381, 399):
        neighbor_values = [-21, -20, -19, -1, +1]
        neighbors = [current_index + i for i in neighbor_values]
        print('works???')
    # ALL OTHER NEIGHBORS
    else:
        neighbor_values = [-21, -20, -19, -1, +1, 19, 20, 21]
        neighbors = [current_index + i for i in neighbor_values]
    print(neighbors)
    # c. sum neighbor states
    neighbor_states = [cur_states[i] for i in neighbors]
    print(neighbor_states)
    state_sum = 0 
    for i in neighbor_states:
        state_sum += i
    print(state_sum)
    # d. update cur_rect state based on sum of neighbor states
    new_state = 0
    if cur_states[current_index] == 1:
        # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
        # Any live cell with more than three live neighbours dies, as if by overpopulation.
        if state_sum < 2 or state_sum > 3:
            new_state = 0
        # Any live cell with two or three live neighbours lives on to the next generation.
        else:
            new_state = 1
    else:
        # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
        if state_sum == 3:
            new_state = 1
        else:
            new_state = 0

 

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    # pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))
    cur_index = 0
    x = 5
    while x < 500:
        y = 5
        while y < 500: 
            # 2. draw rectangles based on states 
            state = cur_states[cur_index]
            if state == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20))
            else:
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20))
            # 4. draw based on values in next_state
            cur_index += 1
            y += 25
        x += 25

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
