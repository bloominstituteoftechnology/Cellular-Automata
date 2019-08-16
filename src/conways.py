import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0 , 0, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500

# 1. v.1 set up initial states

# cur_states = [0] * 400
# cur_states[10] = 1
# cur_states[30] = 1
# cur_states[50] = 1

# 1. v.2 fill cur_states with random states

cur_states = [0] * 400
for i in range(0, len(cur_states)):
    cur_states[i] = random.randint(0, 1)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Store generation number and pause state
generation = 0
is_paused = False

# Add a title

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
    
    generation += 1
    pygame.display.set_caption("Conway's Game of Life, Generation " + str(generation)) 

    # PAUSE/PLAY

    if event.type == pygame.MOUSEBUTTONDOWN:
        click_pos = pygame.mouse.get_pos()
        if pause_button.collidepoint(click_pos):
            is_paused = not is_paused

    # have a boolean keeping track of if game is paused or stopped...
    # could toggle pause button into a play button
    # could have text be dynamic depending on the state, or put play/pause

    # RESTART

    # if event.type == pygame.MOUSEBUTTONDOWN and our button clicked ( look at x, y of click, compare to area of buttons; if area is clicked, then set generation -> 0, set current state to initial states)

    # is_paused = not is_paused

    # MAIN SIMULATION LOGIC!!!!

    # GUIDED DEMO LOGIC TO CHECK NEIGHBORS

    # Calc number of live neighbors
    # index = current cel

    # width = 20
    # e = index + width
    # w = index - width
    # n = index - 1
    # s = index + 1
    # ne = n + width
    # nw = n - width
    # se = s + width
    # sw = s - width

    # live_neighbors = 0
    # if cur_states[e] == 1:
    #     live_neighbors += 1
    # if cur_states[w] == 1:
    #     live_neighbors += 1
    # if cur_states[n] == 1:
    #     live_neighbors += 1
    # if cur_states[s] == 1:
    #     live_neighbors += 1

    # MY LOGIC TO CHECK NEIGHBORS

    new_states = [None] * 400

    for current_index in range(len(cur_states)):
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
        elif current_index % 20 == 0:
            neighbor_values = [-20, -19, -1, 20, 21]
            neighbors = [current_index + i for i in neighbor_values]
        elif (current_index + 1) % 20 == 0:
            neighbor_values = [-21, -20, -1, 19, 20,]
            neighbors = [current_index + i for i in neighbor_values]
        # ALL OTHER NEIGHBORS
        else:
            neighbor_values = [-21, -20, -19, -1, +1, 19, 20, 21]
            neighbors = [current_index + i for i in neighbor_values]
        # c. sum neighbor states
        neighbor_states = [cur_states[i] for i in neighbors]
        
        state_sum = 0 

        for i in neighbor_states:
            state_sum += i
            
        # *** could move this logic to a separate helper function

        # d. update cur_rect state based on sum of neighbor states

        if cur_states[current_index] == 1:
            # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
            # Any live cell with more than three live neighbours dies, as if by overpopulation.
            if state_sum < 2 or state_sum > 3:
                new_states[current_index] = 0
            # Any live cell with two or three live neighbours lives on to the next generation.
            else:
                new_states[current_index] = 1
        else:
            # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
            if state_sum == 3:
                new_states[current_index] = 1
            else:
                new_states[current_index] = 0
    cur_states = new_states

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
    
        pause_button = pygame.draw.rect(screen, BLUE, pygame.Rect(200, 420, 150, 75))
        font = pygame.font.SysFont('Arial', 25)
        text = font.render('Pause', True, (14, 28, 54))
        screen.blit(text, pause_button)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
