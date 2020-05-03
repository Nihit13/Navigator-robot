# -*- coding: utf-8 -*-
"""
Created on Sun May  3 15:55:37 2020

@author: hp
"""


def fill():
    wallsense(cellposition)
    c = 0
    enter = True
    while enter:
        enter = False
        for b in range(9):
            for a in range(9):
                if maze[a][b] == c:
                    enter = True
                    wallleft = False
                    wallright = False
                    wallup = False
                    walldown = False
                    if b == 0 or maze[a][b - 1] == 'w':
                        check_l = False

                    if b == 15 or maze[a][b + 1] == 'w':
                        check_r = False

                    if a == 0 or maze[a - 1][b] == 'w':
                        check_t = False

                    if a == 15 or maze[a + 1][b] == 'w':
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
