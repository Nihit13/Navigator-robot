import pygame
import sys
pygame.init()
mapimages = [pygame.image.load('cell type3.png'), pygame.image.load('celltypes4.png'), pygame.image.load('celltypes5.png'), pygame.image.load('celltypes6.png'), pygame.image.load('celltypes7.png'), pygame.image.load('celltypes8.png'), pygame.image.load('celltypes9.png'), pygame.image.load('celltypes10.png'), pygame.image.load('celltypes11.png'), pygame.image.load('celltypes12.png'), pygame.image.load('celltypes13.png'), pygame.image.load('celltypes14.png'), pygame.image.load('celltypes15.png'), pygame.image.load('celltypes16.png')]

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('NAVIGATOR MAP')
map1 =  pygame.image.load('map.png')
map1 = pygame.transform.scale(map1, (600,600))
rob = pygame.image.load('robot.png')

cell1 = pygame.transform.scale(mapimages[0], (200,200))
cell2 = pygame.transform.scale(mapimages[1], (200,200))
cell3 = pygame.transform.scale(mapimages[2], (200,200))
cell4 = pygame.transform.scale(mapimages[3], (200,200))
cell5 = pygame.transform.scale(mapimages[4], (200,200))
cell6 = pygame.transform.scale(mapimages[5], (200,200))
cell7 = pygame.transform.scale(mapimages[6], (200,200))
cell8 = pygame.transform.scale(mapimages[7], (200,200))
cell9 = pygame.transform.scale(mapimages[8], (200,200))
cell10 = pygame.transform.scale(mapimages[9], (200,200))
cell11 = pygame.transform.scale(mapimages[10], (200,200))
cell12 = pygame.transform.scale(mapimages[11], (200,200))
cell13 = pygame.transform.scale(mapimages[12], (200,200))
cell14 = pygame.transform.scale(mapimages[13], (200,200))

def draw_maze():
    draw(cell7, 0, 0)
    draw(cell7, 0, 200)
    draw(cell3, 0, 400)
    draw(cell1, 200, 0)
    draw(cell2, 200, 200)
    draw(cell2, 200, 400)
    draw(cell5, 400, 0)
    draw(cell2, 400, 200)
    draw(cell2, 400, 400)

start_col = int(input("ENTER THE START COLUMN"))
start_row = int(input("ENTER THE START ROW"))
target_col = int(input("ENTER THE TARGET COLUMN"))
target_row = int(input("ENTER THE TARGET ROW"))

maze = [
        ['e', 'e', 'e'],
        ['e', 'e', 'e'],
        ['e', 'e', 'e']        
        ]

#cell_cord = [(0,0),(0,200),(0,400),(200,0),(200,200),(200,400),(400,0),(400,200),(400,400)]

start_col = start_col * 200
start_row = start_row * 200
target_col = target_col * 200
target_row = target_row * 200

def draw(image, x, y):
    screen.blit(image, (x, y))
        
run = True
while run:
    for event in pygame.event.get():
        
        #draw(map1, 0, 0)
        draw_maze()
        draw(rob, start_col + 75, start_row + 75)
        pygame.display.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
pygame.quit()