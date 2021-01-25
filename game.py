import pygame
import sys
import random as r

pygame.init()
pygame.display.set_caption("Conway's game of life")
screen = pygame.display.set_mode((700, 700))    
screen.fill((250, 200, 200))
clock = pygame.time.Clock()

gridsize = 100
life = [[0 for a in range(gridsize)] for b in range(gridsize)]
sqsize = screen.get_width() // gridsize

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
'''
startcount = 1000
for q in range(startcount):
    flip(r.randint(0, gridsize), r.randint(0, gridsize))

flip(51, 52)
flip(52, 51)
flip(53, 51)
flip(54, 51)
flip(55, 52)
flip(51, 53)
flip(52, 53)
flip(54, 53)
flip(55, 53)
'''
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

def flipList(life):
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

state = False
while True:
    screen.fill((250, 200, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            state = not state
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousex, mousey = pygame.mouse.get_pos()
            flip(mousex//sqsize, mousey//sqsize)
    if state == True:        
        to_flip = flipList(life)
        for x, y in to_flip:
            flip(x, y)
    for i in range(len(life)):
        for j in range(len(life[i])):
            if life[i][j]:
                pygame.draw.rect(screen, (20,50,200), (j*sqsize, i*sqsize, sqsize, sqsize))
    pygame.display.update()
    msElapsed = clock.tick(3)

                
