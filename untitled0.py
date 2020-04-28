import pygame
import sys
pygame.init()
pygame.font.init()
"""
maze = [
    ['w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'e', 'e', 'w'],
    ['w', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'w', 'w', 'e'],
    ['e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e'],
    ['w', 'w', 'e', 'w', 'w', 'w', 'w', 'w', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'w', 'e', 'e', 'e', 'e', 'w'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'w', 'e', 'e', 'e', 'e', 'w'],
    ['w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'w', 'e', 'w'],
    ['w', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e'],
    ['e', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'w', 'e', 'e'],
    ['e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'w'],
    ['w', 'w', 'e', 'w', 'w', 'w', 'w', 'w', 'w', 'e', 'e', 'e', 'w', 'w', 'w', 'w'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'w', 'e', 'w', 'e']

]
"""
maze = [
    ['e', '@', 'e', '@', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'e', 'e', 'w'],
    ['/', '/', '/', '!', '/', '/', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', '/', 'w', '@', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['/', '@', '/', '!', '/', '/', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'w', 'w', 'e'],
    ['e', '/', 'e', '/', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e'],
    ['/', '/', '/', '!', '/', '/', 'w', 'w', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e'],
    ['e', '@', 'e', '/', 'e', 'e', 'e', 'e', 'w', 'e', 'w', 'e', 'e', 'e', 'e', 'w'],
    ['e', '/', 'e', '/', 'e', 'e', 'e', 'e', 'w', 'e', 'w', 'e', 'e', 'e', 'e', 'w'],
    ['e', '/', 'e', '/', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'w', 'e', 'w'],
    ['e', '@', 'e', '/', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e'],
    ['e', '/', 'w', '/', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'w', 'e', 'e'],
    ['e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'w'],
    ['e', '@', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w'], 
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'w', 'e', 'w', 'e', 'w', 'e']
        ]

t_row = int(input("Enter the target row : "))
t_col = int(input("Enter the target column : "))
constant = 37.5
k = 25
d = 0
font = pygame.font.SysFont('comicsans', 20)

# Initializing
pygame.init()
# create the screen
screen = pygame.display.set_mode((600, 600))

pygame.display.set_caption("Navigator Grid")

maze[t_row][t_col] = 0





def show_num(x, y, val):
    num = font.render(val, True, (0, 0, 0))
    screen.blit(num, (x, y))


def detect():
    for y in range(16):
        for x in range(16):
            d = maze[x][y]
            show_num(y * constant + k, x * constant + k, str(d))
            

def fill():
    check_t = True
    check_r = True
    check_b = True
    check_l = True
    c = 0
    enter = True
    while enter:
        enter = False
        for b in range(16):
            for a in range(16):
                if maze[a][b] == c:
                    enter = True
                    check_b = True
                    check_l = True
                    check_r = True
                    check_t = True
                    if b == 0 or maze[a][b - 1] == '/':
                        check_l = False

                    if b == 15 or maze[a][b + 1] == '/':
                        check_r = False

                    if a == 0 or maze[a - 1][b] == '/':
                        check_t = False

                    if a == 15 or maze[a + 1][b] == '/':
                        check_b = False

                    if check_l == True and maze[a][b - 2] == 'e':
                        maze[a][b - 1] = c + 1

                    if check_r == True and maze[a][b + 2] == 'e':
                        maze[a][b + 1] = c + 1

                    if check_t == True and maze[a - 2][b] == 'e':
                        maze[a - 1][b] = c + 1

                    if check_b == True and maze[a + 2][b] == 'e':
                        maze[a + 1][b] = c + 1
        c += 1



def path_finder():
    fill()    
        
    
    s_row = int(input("Enter the starting row : "))
    s_col = int(input("Enter the starting column : "))

    while maze[s_row][s_col] != 0:
        check_b = True
        check_l = True
        check_r = True
        check_t = True
        if s_col == 0 or maze[s_row][s_col - 1] == '/':
            check_l = False

        if s_col == 15 or maze[s_row][s_col + 1] == '/':
            check_r = False

        if s_row == 0 or maze[s_row - 1][s_col] == '/':
            check_t = False

        if s_row == 15 or maze[s_row + 1][s_col] == '/':
            check_b = False

        if check_l == True and maze[s_row][s_col - 1] < maze[s_row][s_col]:
            s_col -= 2

        elif check_r == True and maze[s_row][s_col + 1] < maze[s_row][s_col]:
            s_col += 2

        elif check_t == True and maze[s_row - 1][s_col] < maze[s_row][s_col]:
            s_row -= 2

        elif check_b == True and maze[s_row + 1][s_col] < maze[s_row][s_col]:
            s_row += 2
    

        # Infinite Loop
        running = True
        while running:
            
            keys = pygame.key.get_pressed()
            for event in pygame.event.get():
                if keys[pygame.K_SPACE]:
                    pygame.draw.rect(screen, (255, 0, 0), [s_col, s_row, 37.5, 37.5])
                    running = False
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.fill((255, 255, 255))
            for x in range(16):
                pygame.draw.line(screen, (0, 0, 0), (37.5 * x, 0), (37.5 * x, 600))
            for x in range(16):
                pygame.draw.line(screen, (0, 0, 0), (0, 37.5 * x), (600, 37.5 * x))
                pygame.draw.rect(screen, (255, 0, 0), [s_col * 37.5, s_row * 37.5, 37.5, 37.5])
            detect()
            pygame.display.update()

path_finder()
print("Reached")
pygame.quit()
sys.exit()