import pygame, random
import pygameMenu
import sys
from patterns import blinker
 
# Define some colors and other constants
BLUE = (66, 87, 245)
WHITE = (255, 255, 255)
PINK = (242, 172, 241)
GRAY = (228, 230, 235)
DGRAY = (192, 192, 192)
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

    if len(sys.argv) == 1 or sys.argv[1] == 'random':
        for cell in game:
            game[cell] = random.randint(0,1)
    elif sys.argv[1] == 'blinker':
        for cell in blinker:
            game[cell] = 1
    elif sys.argv[1] == 'block':
        game[(1,1)] = 1
        game[(1,2)] = 1
        game[(1,7)] = 1
        game[(1,8)] = 1
        game[(1,13)] = 1
        game[(1,14)] = 1
        game[(2,1)] = 1
        game[(2,2)] = 1
        game[(2,7)] = 1
        game[(2,8)] = 1
        game[(2,13)] = 1
        game[(2,14)] = 1
        game[(4,1)] = 1
        game[(4,2)] = 1
        game[(4,7)] = 1
        game[(4,8)] = 1
        game[(4,13)] = 1
        game[(4,14)] = 1
        game[(5,1)] = 1
        game[(5,2)] = 1
        game[(5,7)] = 1
        game[(5,8)] = 1
        game[(5,13)] = 1
        game[(5,14)] = 1
        game[(7,1)] = 1
        game[(7,2)] = 1
        game[(7,7)] = 1
        game[(7,8)] = 1
        game[(7,13)] = 1
        game[(7,14)] = 1
        game[(8,1)] = 1
        game[(8,2)] = 1
        game[(8,7)] = 1
        game[(8,8)] = 1
        game[(8,13)] = 1
        game[(8,14)] = 1
        game[(10,1)] = 1
        game[(10,2)] = 1
        game[(10,7)] = 1
        game[(10,8)] = 1
        game[(10,13)] = 1
        game[(10,14)] = 1
        game[(11,1)] = 1
        game[(11,2)] = 1
        game[(11,7)] = 1
        game[(11,8)] = 1
        game[(11,13)] = 1
        game[(11,14)] = 1
        game[(13,1)] = 1
        game[(13,2)] = 1
        game[(13,7)] = 1
        game[(13,8)] = 1
        game[(13,13)] = 1
        game[(13,14)] = 1
        game[(14,1)] = 1
        game[(14,2)] = 1
        game[(14,7)] = 1
        game[(14,8)] = 1
        game[(14,13)] = 1
        game[(14,14)] = 1
        game[(16,1)] = 1
        game[(16,2)] = 1
        game[(16,7)] = 1
        game[(16,8)] = 1
        game[(16,13)] = 1
        game[(16,14)] = 1
        game[(17,1)] = 1
        game[(17,2)] = 1
        game[(17,7)] = 1
        game[(17,8)] = 1
        game[(17,13)] = 1
        game[(17,14)] = 1
        
 




    done = False

    clock = pygame.time.Clock()

    generations = 0
    is_paused = False



    while not done:
        # --- Main event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        pygame.display.set_caption("Conway's Game of Life ~ Generation: " + str(generations))

        pause_button = pygame.draw.rect(screen, GRAY, (350, 420, 100, 50))
        pygame.draw.line(screen, DGRAY, [350, 471], [450, 471], 3)
        pygame.draw.line(screen, DGRAY, [451, 420], [451, 471], 3)

        font = pygame.font.SysFont('Arial', 25)
        label = 'Pause/Play'
        text = font.render(label, True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (pause_button.center[0], pause_button.center[1])
        screen.blit(text, textRect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_pos = pygame.mouse.get_pos()
            if pause_button.collidepoint(click_pos):
                is_paused = not is_paused

        if not is_paused:
            game = life(game)

            for cell in game:
                color(cell, game)
            generations += 1

        pygame.display.flip()
        clock.tick(5)
        

    pygame.quit()
    

if __name__ == "__main__":
    main()

