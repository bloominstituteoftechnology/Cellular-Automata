import pygame, random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)
WIN_SIZE = 500

#Create set of initial states w/ simple patterns
cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1
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
 
    # --- Game logic should go here

    # Any live cell with fewer than two live neighbours dies, as if by underpopulation.
    # Any live cell with two or three live neighbours lives on to the next generation.
    # Any live cell with more than three live neighbours dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
    
    # 3. Work on rules that i) look at all neighbors, ii) save new state
    # in next_states[]

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    cur_index = 0
    x = 5
    while x < 500:
        y = 5
        while y < 500:
            state = cur_states[cur_index]
            if state == 0:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, 20, 20))
            else: 
                pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, 20, 20))
            cur_index +=1
            y+= 25
        x+= 25
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()
