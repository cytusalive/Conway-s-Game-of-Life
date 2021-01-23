gridsize = 10
life = [[0 for a in range(gridsize)] for b in range(gridsize)]

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


flip(4,3)
flip(3,4)
flip(4,4)
flip(5,4)
flip(4,5)
for i in life:
    print(i)


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
    if life[leftx][upy]:
        lifecount += 1
    if life[leftx][y]:
        lifecount += 1
    if life[leftx][downy]:
        lifecount += 1
    if life[x][upy]:
        lifecount += 1
    if life[x][downy]:
        lifecount += 1   
    if life[rightx][upy]:
        lifecount += 1
    if life[rightx][y]:
        lifecount += 1
    if life[rightx][downy]:
        lifecount += 1     
    return lifecount


cont = input("Press enter to begin:\n")
while cont != "exit":
    to_flip = []
    for a in range(len(life)):
        for b in range(len(life[a])):
            nearby = check(a, b)
            if life[a][b]:
                if nearby <= 1:
                    to_flip.append([a, b])
                if nearby >= 4:
                    to_flip.append([a, b])
            else:
                if nearby == 3:
                    to_flip.append([a, b])
    for x, y in to_flip:
        flip(x, y)
    for i in life:
        print(i)
    cont = input("Press enter to continue the game:\n")
                
                
                
