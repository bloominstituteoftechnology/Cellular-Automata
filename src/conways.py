import pygame, random
 
# Define some colors and other constants
BLUE = (66, 87, 245)
WHITE = (255, 255, 255)
PINK = (242, 172, 241)
GRAY = (228, 230, 235)
WIN_SIZE = 500
CELL_SIZE = 20

 
# This sets the margin between each cell
MARGIN = 15

assert WIN_SIZE % CELL_SIZE == 0


def new_grid():
    grid = {}
    for y in range(CELL_SIZE):
        for x in range(CELL_SIZE):
            grid[x, y] = 0
    return grid

def color(cell, grid):
    x = cell[0]
    x = x * CELL_SIZE
    y = cell[1]
    y = y * CELL_SIZE

    if grid[cell] == 0:
        pygame.draw.circle(screen,PINK, (x+50, y+20), 10)
    if grid[cell] == 1:
        pygame.draw.circle(screen,BLUE, (x+50, y+20), 10)
            


def find_neighbors(cell, grid):
    neighbors = 0
    for x in range(-1,2):
        for y in range(-1, 2):
            neighbor_cell = (cell[0] + x, cell[1] + y)

            if neighbor_cell[0] < CELL_SIZE and neighbor_cell[0] >=1:
                if neighbor_cell[1] < CELL_SIZE and neighbor_cell[1] >= 0:
                    if grid[neighbor_cell] == 1:
                        if x == 0 and y == 0:
                            neighbors += 0
                        else:
                            neighbors += 1
    return neighbors

def life(grid):
    nex_gen = {}

    for cell in grid:
        neighbor_sum = find_neighbors(cell, grid)

        if grid[cell] == 1:
            if neighbor_sum < 2: 
                nex_gen[cell] = 0
            elif neighbor_sum > 3:
                nex_gen[cell] = 0 
            else:
                nex_gen[cell] = 1 
        else:
            if neighbor_sum == 3:
                nex_gen[cell] = 1
            else:
                nex_gen[cell] = 0
    
    return nex_gen

# -------- Main Program Loop -----------



def main():
    pygame.init()
    size = (WIN_SIZE, WIN_SIZE)
    global screen
    screen = pygame.display.set_mode(size)

    screen.fill(WHITE)
    game = new_grid()
    
    for cell in game:
        game[cell] = random.randint(0,1)
 




    done = False

    clock = pygame.time.Clock()

    generations = 0



    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.set_caption("Conway's Game of Life ~ Generation: " + str(generations))

        game = life(game)

        for cell in game:
            color(cell, game)

        pygame.display.flip()
        clock.tick(5)
        generations += 1

    pygame.quit()
    

if __name__ == "__main__":
    main()

