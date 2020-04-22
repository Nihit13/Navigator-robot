import pygame

pygame.font.init()
maze = [
    ['w', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['w', 'w', 'e', 'w', 'w', 'w', 'w', 'w'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e']

]
t_row = int(input("Enter the target row : "))
t_col = int(input("Enter the target column : "))
constant = 75
k = 25
d = 0
font = pygame.font.Font('JandaManateeSolid.ttf', 32)

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
    for y in range(8):
        for x in range(8):
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
        for b in range(8):
            for a in range(8):
                if maze[a][b] == c:
                    enter = True
                    check_b = True
                    check_l = True
                    check_r = True
                    check_t = True
                    if b == 0 or maze[a][b - 1] == 'w':
                        check_l = False

                    if b == 7 or maze[a][b + 1] == 'w':
                        check_r = False

                    if a == 0 or maze[a - 1][b] == 'w':
                        check_t = False

                    if a == 7 or maze[a + 1][b] == 'w':
                        check_b = False

                    if check_l == True and maze[a][b - 1] == 'e':
                        maze[a][b - 1] = c + 1

                    if check_r == True and maze[a][b + 1] == 'e':
                        maze[a][b + 1] = c + 1

                    if check_t == True and maze[a - 1][b] == 'e':
                        maze[a - 1][b] = c + 1

                    if check_b == True and maze[a + 1][b] == 'e':
                        maze[a + 1][b] = c + 1
        c += 1



def path_finder():
    s_row = int(input("Enter the starting row : "))
    s_col = int(input("Enter the starting column : "))
    h = 1
    while maze[s_row][s_col] != 0:
        check_b = True
        check_l = True
        check_r = True
        check_t = True
        if s_col == 0 or maze[s_row][s_col - 1] == 'w':
            check_l = False

        if s_col == 7 or maze[s_row][s_col + 1] == 'w':
            check_r = False

        if s_row == 0 or maze[s_row - 1][s_col] == 'w':
            check_t = False

        if s_row == 7 or maze[s_row + 1][s_col] == 'w':
            check_b = False

        if check_l == True and maze[s_row][s_col - 1] < maze[s_row][s_col]:
            s_col -= 1

        elif check_r == True and maze[s_row][s_col + 1] < maze[s_row][s_col]:
            s_col += 1

        elif check_t == True and maze[s_row - 1][s_col] < maze[s_row][s_col]:
            s_row -= 1

        elif check_b == True and maze[s_row + 1][s_col] < maze[s_row][s_col]:
            s_row += 1
        cons = 75
        fill()
        # Infinite Loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    running = False

            screen.fill((255, 255, 255))
            for x in range(8):
                pygame.draw.line(screen, (0, 0, 0), (75 * x, 0), (75 * x, 600))
            for x in range(8):
                pygame.draw.line(screen, (0, 0, 0), (0, 75 * x), (600, 75 * x))
                pygame.draw.rect(screen, (255, 0, 0), [s_col * cons, s_row * cons, cons, cons])
            detect()
            pygame.display.update()




path_finder()
print("Reached")







