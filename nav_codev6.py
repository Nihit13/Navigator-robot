# Importing
import pygame
import math
import sys
import sys


# Defining the maze of cells 16*16
maze = [
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e','e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],


]

maze_wall = [
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
              ]
#  Defining the maze of cells and walls 32*31
def maze_wall():
    maze_wall = [
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e','C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ]
    return maze_wall
maze_wall = maze_wall()
# Defining few variables
constant = 37.5
k = 10
close = False

# Initializing pygame and the font
pygame.init()
pygame.font.init()
# Creating the screen
screen = pygame.display.set_mode((600, 630))

# Setting the caption and the font for the pygame window
pygame.display.set_caption("Navigator Grid")
font = pygame.font.SysFont('Showcard Gothic', 15)
font2 = pygame.font.SysFont('Showcard Gothic' , 15)


    
    
    # The fill function writes the numbers into the grid
    # It searches the maze for value = c and it writes the adjecent empty cells a value one higher than c
    # This happens until all the cells have a value
def fill():
    check_t = True
    check_r = True
    check_b = True
    check_l = True
    c = 0
    enter = True
    while enter:

        enter = False
        # Checking all the cells in the maze
        for b in range(16):
            for a in range(16):
                if maze[a][b] == c:
                    enter = True
                    check_b = True
                    check_l = True
                    check_r = True
                    check_t = True
                    # Checking whether there is a wall between the cell and its adjecent cells
                    if+ b == 0 or maze_wall[a * 2][(b * 2) - 1] == 'w':
                        check_l = False

                    if b == 15 or maze_wall[a * 2][(b * 2) + 1] == 'w':
                        check_r = False

                    if a == 0 or maze_wall[(a * 2) - 1][b * 2] == 'w':
                        check_t = False

                    if a == 15 or maze_wall[(a * 2) + 1][b * 2] == 'w':
                        check_b = False

                    # If there is no wall and the cell does not have a number then it assigns the cell with a value of c+1
                    if check_l == True and maze[a][b - 1] == 'e':
                        maze[a][b - 1] = c + 1

                    if check_r == True and maze[a][b + 1] == 'e':
                        maze[a][b + 1] = c + 1

                    if check_t == True and maze[a - 1][b] == 'e':
                        maze[a - 1][b] = c + 1

                    if check_b == True and maze[a + 1][b] == 'e':

                        maze[a + 1][b] = c + 1
        # C is incremented by one so when it finishes all the cells with a value of c, it moves on to the next number that is c+1
        c += 1


def revert():
    for y in range(16):
        for x in range(16):
            if maze[x][y] != 0 :
                maze[x][y] = 'e'


# When a wall is assigned in maze_wall , the user can see the wall on the pygame window because of this function
# Checks all the wall_cell , and those who have a wall , the wall is printed on the pygame window
def wall_detect():
    for wall_y in range(32):
        for wall_x in range(31):
            if maze_wall[wall_x][wall_y] == 'w':
                check_b = True
                check_l = True
                check_r = True
                check_t = True
                if wall_y == 0:
                    check_l = False

                if wall_x == 0:
                    check_t = False

                # If there is a cell surrounding the wall on the left, then draw a rectangle which is vertical
                if check_l == True and maze_wall[wall_x][wall_y - 1] == 'C':
                    pygame.draw.rect(screen, (49, 49, 209),[(wall_y + 1) / 2 * constant - 2, (wall_x) / 2 * constant, 4, 39])

                # If there is a cell surrounding the wall on the top, then draw a rectangle which is horizontal
                if check_t == True and maze_wall[wall_x - 1][wall_y] == 'C':
                    pygame.draw.rect(screen, (49, 49, 209), [(wall_y) / 2 * constant, (wall_x + 1) / 2 * constant - 2, 39, 4])

# The show_num function takes the coordinates and the value of what to print and prints it on the pygame window
def show_num(x, y, val):
    num = font.render(val, True, (0, 0, 0))
    screen.blit(num, (x, y))

def write(x,y,val):
    num = font2.render(val, True, (40, 185, 50))
    screen.blit(num, (x, y))

# The num_detect function scans all the cells in maze and feeds them to the show_num function so they are written on the pygame window
def num_detect():
    for y in range(16):
        for x in range(16):
            d = maze[x][y]
            show_num(y * constant + k, x * constant + k, str(d))

def select_target(close):
    # Infinite Loop

    screen.fill((255,255,255))
    running = True
    pressed = False
    global t_row
    global t_col
    t_row = 0
    t_col = 0
    key_pressed = False
    while running:
        
        if close:
            break
        screen.fill((255, 255, 255))
        if not key_pressed:
            write(0, 610, 'Select The Target Cell, Once Done press Enter')
        else:
            write(0, 610, 'Enter a valid target cell')
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    key_pressed = True
                    if pressed :
                        running = False
            if event.type == pygame.QUIT:
                running = False
                close = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                # Recognises which cell the mouse pointer is in
                x_dist = x % 37.5
                y_dist = y % 37.5
                x_cell = x - x_dist
                y_cell = y - y_dist
                x_cell = int(x_cell / 37.5)
                y_cell = int(y_cell / 37.5)
                if x_cell < 16 and y_cell < 16:
                    pressed = True
                    t_row = y_cell
                    t_col = x_cell

        # Creating the Grid
        for x in range(16):
            pygame.draw.line(screen, (0, 0, 0), (37.5 * x, 0), (37.5 * x, 600))
        for x in range(17):
            pygame.draw.line(screen, (0, 0, 0), (0, 37.5 * x), (600, 37.5 * x))


            if pressed :
                pygame.draw.rect(screen,(255,0,0),[t_col*37.5,t_row*37.5,38,38])
        pygame.display.update()
    return close

def select_start(close):
    # Infinite Loop
    running = True
    pressed = False
    revert()
    fill()
    global s_row
    global s_col
    s_row = 0
    s_col = 0
    key_pressed = False
    while running:
        if close:
            break
        screen.fill((255, 255, 255))
        if not key_pressed:
            write(0, 610, 'Select The Start Cell, Once Done press Enter')
        else:
            write(0, 610, 'Enter a valid start cell')
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    key_pressed = True
                    if pressed :
                        running = False
            if event.type == pygame.QUIT:
                running = False
                close = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                # Recognises which cell the mouse pointer is in
                x_dist = x % 37.5
                y_dist = y % 37.5
                x_cell = x - x_dist
                y_cell = y - y_dist
                x_cell = int(x_cell / 37.5)
                y_cell = int(y_cell / 37.5)
                if x_cell < 16 and y_cell < 16:
                    pressed = True
                    s_row = y_cell
                    s_col = x_cell

        # Creating the Grid
        for x in range(16):
            pygame.draw.line(screen, (0, 0, 0), (37.5 * x, 0), (37.5 * x, 600))
        for x in range(17):
            pygame.draw.line(screen, (0, 0, 0), (0, 37.5 * x), (600, 37.5 * x))
        if pressed :
            pygame.draw.rect(screen,(255,0,0),[s_col*37.5,s_row*37.5,38,38])
        wall_detect()
        num_detect()
 
        pygame.display.update()
    start = [s_row,s_col,close]
    return start


def click_detect(close):
    # Infinite Loop
    running = True
    pressed = False
    revert()
    fill()
    while running:
        if close :
            break
        check_b = True
        check_l = True
        check_r = True
        check_t = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN :
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                pressed = True
                (x,y) = pygame.mouse.get_pos()
                # Recognises which cell the mouse pointer is in
                x_dist = x%37.5
                y_dist = y%37.5
                x_wall = x-x_dist
                y_wall = y-y_dist
                x_wall = int((x_wall/37.5)*2)
                y_wall = int((y_wall / 37.5)*2)

                if x_wall == 0 :
                    check_l = False

                if y_wall == 0 :
                    check_t = False

                if y_wall == 31 :
                    check_b = False

                if check_l == True and x_dist < 7:
                    if maze_wall[y_wall][x_wall - 1] == 'w':
                        maze_wall[y_wall][x_wall - 1] = 'e'
                    else:
                        maze_wall[y_wall][x_wall - 1] = 'w'


                elif x_dist > 45:
                    if maze_wall[y_wall][x_wall + 1] == 'w':
                        maze_wall[y_wall][x_wall + 1] = 'e'
                    else:
                        maze_wall[y_wall][x_wall + 1] = 'w'

                elif check_t == True and y_dist < 25:
                    if maze_wall[y_wall - 1][x_wall] == 'e':
                        maze_wall[y_wall - 1][x_wall] = 'w'
                    else:
                        maze_wall[y_wall - 1][x_wall] = 'w'

                elif check_b == True and y_dist > 32:
                    if maze_wall[y_wall + 1][x_wall] == 'w':
                        maze_wall[y_wall + 1][x_wall] = 'e'
                    else:
                        maze_wall[y_wall + 1][x_wall] = 'w'

        for x in range(16):
            pygame.draw.line(screen, (0, 0, 0), (37.5 * x, 0), (37.5 * x, 600))
        for x in range(17):
            pygame.draw.line(screen, (0, 0, 0), (0, 37.5 * x), (600, 37.5 * x))
        wall_detect()
        num_detect()
        pressed = False
        write(0,610,'Enter Walls by clicking on the Grid Lines , Once done click enter')
        pygame.display.update()

    return close

# the path_finder function is designed to find the shortest path for the bot.
def path_finder(start,close):

    # Defining few variables
    executed = False
    s_row = start[0]
    s_col = start[1]
    while maze[s_row][s_col] != 0:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    close = True
                    sys.exit()
        
        if close:
            break
        if executed:
            check_b = True
            check_l = True
            check_r = True
            check_t = True
            # Checking whether there is a wall between the adjecent cells
            if s_col == 0 or maze_wall[s_row * 2][s_col * 2 - 1] == 'w':
                check_l = False

            if s_col == 15 or maze_wall[s_row * 2][s_col * 2 + 1] == 'w':
                check_r = False

            if s_row == 0 or maze_wall[s_row * 2 - 1][s_col * 2] == 'w':
                check_t = False

            if s_row == 15 or maze_wall[s_row * 2 + 1][s_col * 2] == 'w':
                check_b = False

            # if there is no wall and the value of the adjecent cell is less than that of the current cell then the bot moves to that cell
            if check_l == True and maze[s_row][s_col - 1] < maze[s_row][s_col]:
                s_col -= 1

            elif check_r == True and maze[s_row][s_col + 1] < maze[s_row][s_col]:
                s_col += 1

            elif check_t == True and maze[s_row - 1][s_col] < maze[s_row][s_col]:
                s_row -= 1

            elif check_b == True and maze[s_row + 1][s_col] < maze[s_row][s_col]:
                s_row += 1

        # Infinite Loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    running = False
                if event.type == pygame.QUIT:
                    running = False
                    close = True
                    pygame.quit()
                    sys.exit()
                    
                executed = True
                screen.fill((255, 255, 255))
                # Creating the Grid
                for x in range(16):
                    pygame.draw.line(screen, (0, 0, 0), (37.5 * x, 0), (37.5 * x, 600))
                for x in range(17):
                    pygame.draw.line(screen, (0, 0, 0), (0, 37.5 * x), (600, 37.5 * x))
                # Calling the functions which display the walls and the numbers
                wall_detect()
                num_detect()
                robot = pygame.image.load('robot.png')
                robot = pygame.transform.scale(robot, (38, 38))
                screen.blit(robot, (s_col * constant, s_row * constant))
                write(0,610,'Press any key to show the path of the robot to the target cell ')
                pygame.display.update()

def startscreen(maze_wall):
    pygame.init()
    win = pygame.display.set_mode((600, 630))

    class button():
        def __init__(self, color, x, y, width, height, text=''):
            self.color = color
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.text = text

        def draw(self, win, outline=None):
            # Call this method to draw the button on the screen
            if outline:
                pygame.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

            if self.text != '':
                font = pygame.font.SysFont('Showcard Gothic', 25)
                text = font.render(self.text, 1, (0, 0, 0))
                win.blit(text, (
                self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

        def isOver(self, pos):
            # Pos is the mouse position or a tuple of (x,y) coordinates
            if pos[0] > self.x and pos[0] < self.x + self.width:
                if pos[1] > self.y and pos[1] < self.y + self.height:
                    return True

            return False

    def redrawgamewindow():
        button_.draw(win, (0, 0, 0))

    run = True
    button_ = button((255, 128, 0), 218, 340, 160, 50, 'START')
    exitbutton = button((255, 128, 0), 218, 400, 160, 50, 'EXIT')
    while run:
        startscreen = pygame.image.load('startscreen.png')
        pygame.transform.scale(startscreen, (600, 630))
        win.blit(startscreen, (0, 0))
        button_.draw(win, (0, 0, 0))
        exitbutton.draw(win, (0,0,0))
        pygame.display.update()

        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            # Condition to check if Windows Close button is clicked
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                # Condition to check if Start Button is pressed
                if button_.isOver(pos):
                    close = 0
                    close = select_target(close)
                    maze[t_row][t_col] = 0

                    close = click_detect(close)
                    start = select_start(close)
                    start[2] = close
                    path_finder(start, close)
                # Condition to check if Exit Button is pressed
                if exitbutton.isOver(pos):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEMOTION:
                if button_.isOver(pos):
                    button_.color = (128, 255, 39)
                else:
                    button_.color = (255, 128, 0)

                if exitbutton.isOver(pos):
                    exitbutton.color = (128, 255, 39)
                else:
                    exitbutton.color = (255, 128, 0)


        startscreen = pygame.image.load('startscreen.png')
        pygame.transform.scale(startscreen, (600, 630))
        win.blit(startscreen, (0, 0))

        maze_wall = maze_wall()

startscreen(maze_wall)