# Conway's Game of Life, calculated using an array of lists
# and displayed using pygame graphics
import pygame
import sys
import random as r

# Setting up pygame with screen size, caption, background color, frames per second
# Screen size can be modified
pygame.init()
pygame.display.set_caption("Conway's game of life")
screen = pygame.display.set_mode((700, 700))
bgcolor = (250, 200, 200)
screen.fill(bgcolor)
clock = pygame.time.Clock()

# gridsize determines the array size and the size of each element, can be modified
gridsize = 100
life = [[0 for a in range(gridsize)] for b in range(gridsize)]
sqsize = screen.get_width() // gridsize

# Input instruction text
textcolor = (0, 100, 0)
font = pygame.font.Font("freesansbold.ttf", 32)
text1 = font.render('Mouse click to add/remove Life', True, textcolor)
text2 = font.render('Press SPACE key to randomize', True, textcolor)
text3 = font.render('Press ENTER key to start/pause', True, textcolor)

# Flips a cell between alive and dead
def flip(x, y):
    for a in range(len(life)):
        if a == y:
            for b in range(len(life)):
                if b == x:
                    if life[a][b] == 1:
                        life[a][b] = 0
                    elif life[a][b] == 0:
                        life[a][b] = 1
    return

# Randomize option automatically flips 10% of cells, may repeat
def randomize():
    startcount = gridsize**2 // 10
    for q in range(startcount):
        flip(r.randint(0, gridsize), r.randint(0, gridsize))

# Checks surronding cells for the number of neighbors
# Loops to the other side if the value is out of bounds 
def check(x, y):
    lifecount = 0
    leftx = x - 1 
    rightx = x + 1
    if rightx >= gridsize:
        rightx -= gridsize
    upy = y - 1
    downy = y + 1
    if downy >= gridsize:
        downy -= gridsize  
    if life[upy][leftx]:
        lifecount += 1
    if life[y][leftx]:
        lifecount += 1
    if life[downy][leftx]:
        lifecount += 1
    if life[upy][x]:
        lifecount += 1
    if life[downy][x]:
        lifecount += 1   
    if life[upy][rightx]:
        lifecount += 1
    if life[y][rightx]:
        lifecount += 1
    if life[downy][rightx]:
        lifecount += 1     
    return lifecount

# Using the check() function to create a list of cells to flip in the next iteration
def flipList():
    to_flip = []
    for a in range(len(life)):
        for b in range(len(life[a])):
            nearby = check(b, a)
            if life[a][b]:
                if nearby <= 1:
                    to_flip.append([b, a])
                if nearby >= 4:
                    to_flip.append([b, a])
            else:
                if nearby == 3:
                    to_flip.append([b, a])
    return to_flip

# Program executes here
state = False
while True:
    screen.fill((250, 200, 200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                state = not state
            if event.key == pygame.K_SPACE:
                randomize()
        #finds mouse position and flips the according item in Life when clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            flip(mousex//sqsize, mousey//sqsize)
    # Help text displays when paused
    if state == False:
        screen.blit(text1, (100, 100))
        screen.blit(text2, (100, 150))
        screen.blit(text3, (100, 200))
    # a to_flip list is created, flipped and the result displayed each iteration
    if state == True:        
        to_flip = flipList()
        for x, y in to_flip:
            flip(x, y)
    for i in range(len(life)):
        for j in range(len(life[i])):
            if life[i][j]:
                pygame.draw.rect(screen, (20,50,200), (j*sqsize, i*sqsize, sqsize, sqsize))
    pygame.display.update()
    msElapsed = clock.tick(3)

                
