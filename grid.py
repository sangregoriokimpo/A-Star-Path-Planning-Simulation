import pygame
from spot import Spot
from config import *

def make_grid(rows, width):
    gap = width // rows
    return [[Spot(i, j, gap, rows) for j in range(rows)] for i in range(rows)]

def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        pygame.draw.line(win, GREY, (i * gap, 0), (i * gap, width))

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    draw_grid(win, rows, width)
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    x, y = pos
    gap = width // rows
    return y // gap, x // gap
