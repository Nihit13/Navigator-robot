# Importing
import pygame
import math

# Defining the maze of cells 16*16
maze = [
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],
    ['e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e', 'e'],

]
#  Defining the maze of cells and walls 32*31
maze_wall = [
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
    ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C',
     'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
]


def wall_revert():
    #  Defining the maze of cells and walls 32*31
    maze_wall = [
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],
        ['C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e', 'C','e', 'C', 'e', 'C', 'e', 'C', 'e', 'C', 'e'],

    ]
    return maze_wall

# Callsing the wall revert function
wall_revert()

# Defining few variables
constant = 37.5
k = 10
close = False

# Initializing pygame and the font
pygame.init()
pygame.font.init()
# Creating the screen
screen = pygame.display.set_mode((600, 650))

# Setting the caption and the font for the pygame window
pygame.display.set_caption("Navigator Grid")
font = pygame.font.Font('Showcard Gothic', 15)
font2 = pygame.font.Font('Showcard Gothic', 15)
font3 = pygame.font.Font('Showcard Gothic' , 30 )


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
                    if b == 0 or maze_wall[a * 2][(b * 2) - 1] == 'w':
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

# The revert function changes all the values to 'e' in maze apart from the target cell
def revert():
    for y in range(16):
        for x in range(16):
            if maze[x][y] != 0:
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
                    pygame.draw.rect(screen, (49, 49, 209),
                                     [(wall_y + 1) / 2 * constant - 2, (wall_x) / 2 * constant, 4, 39])

                # If there is a cell surrounding the wall on the top, then draw a rectangle which is horizontal
                if check_t == True and maze_wall[wall_x - 1][wall_y] == 'C':
                    pygame.draw.rect(screen, (49, 49, 209),
                                     [(wall_y) / 2 * constant, (wall_x + 1) / 2 * constant - 2, 39, 4])

# The complete revert function changes all the values in maze to 'e' including the target cell
def complete_revert():
    for a in range (16):
        for b in range (16):
            maze[b][a] = 'e'

# Mazewall_revert function changes all the walls in maze_wall back to 'e' which means no wall
def mazewall_revert():
    for a in range (32):
        for b in range (31):
            if maze_wall == 'w':
                maze_wall[b][a] = 'e'

# The show_num function takes the coordinates and the value of what to print and prints it on the pygame window
def show_num(x, y, val):
    num = font.render(val, True, (0, 0, 0))
    screen.blit(num, (x, y))

# The write function writes a value when given its coordinates and color onto the screen
def write(x, y, val,color):
    num = font2.render(val, True, color)
    screen.blit(num, (x, y))

# The write2 function is similar to the write function, only difference is that the font is larger and different to that in write function
def write2(x, y, val,color):
    num = font3.render(val, True, color)
    screen.blit(num, (x, y))

# The num_detect function scans all the cells in maze and feeds them to the show_num function so they are written on the pygame window
def num_detect():
    for y in range(16):
        for x in range(16):
            d = maze[x][y]
            show_num(y * constant + k, x * constant + k, str(d))


# The start_screen function displays the UI for the starting screen and also accepts uesr inputs
def start_screen(close):
    running = True
    color1 = False
    color2 = False
    while running:
        startscreen = pygame.image.load('Screen2.png')
        startscreen = pygame.transform.scale(startscreen, (600, 650))
        screen.blit(startscreen, (0, 0))
        pygame.draw.rect(screen, (0, 0, 0), [230, 350, 130, 50])

        pygame.draw.rect(screen, (0, 0, 0), [230, 410, 130, 50])

        pygame.draw.rect(screen, (255, 128, 0), [235, 415, 120, 40])


        if close :
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                close = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                (x, y) = pygame.mouse.get_pos()
                if 230<x<360 and 350<y<400:
                    running = False

                if 230<x<360 and 410<y<460:
                    running = False
                    close = True

        (x, y) = pygame.mouse.get_pos()
        if 230<x<360 and 350<y<400 :
            pygame.draw.rect(screen,(128, 255, 39),[235,355,120,40])
        else:
            pygame.draw.rect(screen, (255, 128, 0), [235, 355, 120, 40])
        if 230<x<360 and 410<y<460:
            pygame.draw.rect(screen, (128, 255, 39), [235, 415, 120, 40])
        write2(250, 363, 'START', (255, 255, 255))
        write2(260, 423, 'EXIT', (255, 255, 255))
        pygame.display.update()
    return close

# The select_target function is used for the UI while selection of the target cell
def select_target(close):
    # Infinite Loop
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
            write(0, 610, 'Select The Target Cell, Once Done press Enter',(40, 185, 50))
        else:
            write(0, 610, 'Enter a valid target cell',(40, 185, 50))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    key_pressed = True
                    if pressed:
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
        if pressed:
            pygame.draw.rect(screen, (255, 0, 0), [t_col * 37.5, t_row * 37.5, 38, 38])
        pygame.display.update()
    return close

# The select_start function is used for the UI while selection of the start cell
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
            write(0, 610, 'Select The Start Cell, Once Done press Enter',(40, 185, 50))
        else:
            write(0, 610, 'Enter a valid start cell',(40, 185, 50))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    key_pressed = True
                    if pressed:
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
        if pressed:
            pygame.draw.rect(screen, (255, 0, 0), [s_col * 37.5, s_row * 37.5, 38, 38])
        wall_detect()
        num_detect()

        pygame.display.update()
    start = [s_row, s_col, close]
    return start

# The click detect function allows the user to enter the walls accordingly into the maze
def click_detect(close):
    # Infinite Loop
    running = True
    pressed = False
    fill()
    while running:
        if close:
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
                if event.key == pygame.K_RETURN:
                    running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = True
                (x, y) = pygame.mouse.get_pos()
                # Recognises which cell the mouse pointer is in
                x_dist = x % 37.5
                y_dist = y % 37.5
                x_wall = x - x_dist
                y_wall = y - y_dist
                x_wall = int((x_wall / 37.5) * 2)
                y_wall = int((y_wall / 37.5) * 2)

                if x_wall == 0:
                    check_l = False

                if y_wall == 0:
                    check_t = False

                if y_wall == 31:
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

        screen.fill((255, 255, 255))
        for x in range(16):
            pygame.draw.line(screen, (0, 0, 0), (37.5 * x, 0), (37.5 * x, 600))
        for x in range(17):
            pygame.draw.line(screen, (0, 0, 0), (0, 37.5 * x), (600, 37.5 * x))
        wall_detect()
        num_detect()
        pressed = False
        write(0, 610, 'Enter Walls by clicking on the Grid Lines , Once done click enter',(40, 185, 50))
        pygame.display.update()
    return close


# the path_finder function is designed to find the shortest path for the bot.
def path_finder(start, close):
    # Defining few variables
    executed = False
    s_row = start[0]
    s_col = start[1]
    while maze[s_row][s_col] != 0:
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
                robot = pygame.image.load('Robot.png')
                robot = pygame.transform.scale(robot, (38, 38))
                screen.blit(robot, (s_col * constant, s_row * constant))

                write(0, 610, 'Press any key to show the path of the robot to the target cell ',(40, 185, 50))
                pygame.display.update()

# All the functions are called inside this loop which runs until the user quits the program.
while not close:
    close = start_screen(close)
    close = select_target(close)
    maze[t_row][t_col] = 0
    close = click_detect(close)
    start = select_start(close)
    start[2] = close
    path_finder(start, close)
    maze_wall = wall_revert()
    complete_revert()

