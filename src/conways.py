import pygame, random
import sys
import random
 
# Define some colors and other constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (25, 25, 25)

starting_margins = 5
square_size_w_padding = 22
border = 2
#### RECCOMMENDED MAX = 45
num_squares = 23 if len(sys.argv) == 1 else int(sys.argv[1])
WIN_SIZE =  square_size_w_padding * num_squares

# curr_states = [Totalarrays = numSQRS , indexPerArr = numSqrs]

# next_states = []

curr_states =[ [random.randint(0,1)  for n in range(num_squares)] for i in range(num_squares)]

print(curr_states)

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE + (2 * starting_margins), WIN_SIZE + (2 * starting_margins))
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("This shit is DOPE")
 
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

    #3. WORK ON RULES THAT 1) LOOK AT ALL NEIGHBORS, 2) SAVE THE NEW STATE IN NEXT_STATES[]
    # for i in len(curr_states):
    #     for node in len(curr_states[i]):
    #         if i-1 <= 0 and node  0 

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(GRAY)
 
    # --- Drawing code should go here
    
    x= starting_margins
    # curr_index = 0
    while x < WIN_SIZE:
        y= starting_margins
        while y < WIN_SIZE:
            # 2 draw based IN CURR_STATES
            COLOR = BLACK if curr_states[round((x - starting_margins)/num_squares)][round((y-starting_margins)/num_squares)] == 0 else WHITE
    
            # 4 Draw based on values in next_states
            pygame.draw.rect(screen, COLOR, pygame.Rect(x, y, (square_size_w_padding - border), (square_size_w_padding - border)) )
            y += square_size_w_padding
        x += square_size_w_padding

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()

# WIN_SIZE/Y 
