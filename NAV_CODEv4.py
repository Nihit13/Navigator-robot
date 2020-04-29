import pygame
import sys
pygame.init()
mapimages = [pygame.image.load('cell type3.png'), pygame.image.load('celltypes4.png'), pygame.image.load('celltypes5.png'), pygame.image.load('celltypes6.png'), pygame.image.load('celltypes7.png'), pygame.image.load('celltypes8.png'), pygame.image.load('celltypes9.png'), pygame.image.load('celltypes10.png'), pygame.image.load('celltypes11.png'), pygame.image.load('celltypes12.png'), pygame.image.load('celltypes13.png'), pygame.image.load('celltypes14.png'), pygame.image.load('celltypes15.png'), pygame.image.load('celltypes16.png')]

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('NAVIGATOR MAP')
map1 =  pygame.image.load('map.png')
map1 = pygame.transform.scale(map1, (600,600))
rob = pygame.image.load('robot.png')
#    win.blit(bg, (0,0))

def draw(image, x, y):
    screen.blit(image, (x, y))
    
#def entry():
     
    
    
    
    
    
    
    
run = True
while run:
    for event in pygame.event.get():
        pygame.display.update()
        draw(map1, 0, 0)
        draw(rob, 50, 50)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            










pygame.quit()