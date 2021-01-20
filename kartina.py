import pygame
import math
from pygame.draw import *

def draw_eye(display, x,y, size):
    circle(display, (255, 0, 0), (x, y), size)
    circle(display, (0, 0, 0), (x, y), size/2)
    rect(display, (0,0 , 0), (x-size, y-1.3*size, 50, 10))
pygame.init()

def draw_fon(display):
    rect(display, (100, 150, 255), (0, 0, 800, 150))
    rect(display, (0, 0, 255), (0, 150, 800, 150))
    rect(display, (255, 255, 0), (0, 250, 800, 150))
pygame.init()

def draw_boat(display,start_pos_x,start_pos_y):
    circle(display, (139,69,19), [start_pos_x,start_pos_y], 40, 0, draw_bottom_left=True)
    rect(display, (139,69,19), (start_pos_x,start_pos_y, 250,40),width=0)
    polygon(display, (139,69,19), [[start_pos_x+250,start_pos_y], [start_pos_x+350, start_pos_y], [start_pos_x+250, start_pos_y+40]], 0)
    rect(display, (0, 0, 0), (start_pos_x+100, start_pos_y-150, 10, 150), width=0)
    polygon(display, (240, 240, 150), [[start_pos_x + 110, start_pos_y-150], [start_pos_x + 160, start_pos_y-100], [start_pos_x + 110, start_pos_y -50]],
            0)
def draw_straw(display,start_pos_x,start_pos_y):
    rect(display, (200, 150, 40), (start_pos_x, start_pos_y-150, 10, 150), width=0)
    polygon(display, (240, 40, 40), [[start_pos_x -100, start_pos_y - 150], [start_pos_x + 100, start_pos_y - 150],
                                   [start_pos_x , start_pos_y - 180]], 0)
    for x in range(20,200,20):
        line(display,(0, 0, 0),[start_pos_x - 100+x, start_pos_y - 150], [start_pos_x , start_pos_y - 180],2)

def draw_sun(display,start_pos_x,start_pos_y,size):
    circle(display, (255, 255, 0), (start_pos_x,start_pos_y), size)

def draw_clouds(display,start_pos_x,start_pos_y,size):
    for i in range(10,60,10):
        circle(display, (255, 255, 255), (start_pos_x+20+i, start_pos_y-size/2), size)
        circle(display, (0, 0, 0), (start_pos_x + 20 + i, start_pos_y - size / 2), size,1)
        circle(display, (255, 255, 255), (start_pos_x+15+i, start_pos_y), size)
        circle(display, (0, 0, 0), (start_pos_x + 15 + i, start_pos_y), size,1)
        if i==50:
            print('sas')
            i=60
            circle(display, (255, 255, 255), (start_pos_x + 15 + i, start_pos_y), size)
            circle(display, (0, 0, 0), (start_pos_x + 15 + i, start_pos_y), size, 1)


FPS = 30
screen = pygame.display.set_mode((800, 400))
draw_fon(screen)
draw_boat(screen,330,170)
draw_straw(screen,120,370)
draw_clouds(screen,40,50,15)
draw_sun(screen,700,60,40)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()