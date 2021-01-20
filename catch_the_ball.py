import pygame
import time
from pygame.draw import *
from random import randint
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 80)
textsurface = myfont.render('BOOM', False, (255, 0, 0))
global dx, dy, dx2,dy2,dx3,dy3
global ingame
ingame=0
score=0
dx,dy,dx2,dy2,dx3,dy3=1,1,1,1,1,1,
SCREEN_SIZE = WIDTH, HEIGHT = (1900, 1000)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def new_ball():
    '''рисует новый шарик '''
    global x, y, r,color
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def new_ball2():
    '''рисует новый шарик '''
    global x2, y2, r2,color2
    x2 = randint(100, 1100)
    y2 = randint(100, 900)
    r2 = randint(10, 100)
    color2 = COLORS[randint(0, 5)]
    circle(screen, color2, (x2, y2), r2)

def new_ball3():
    '''рисует новый шарик '''
    global x3, y3, r3,color3
    x3 = randint(100, 1100)
    y3 = randint(100, 900)
    r3 = randint(10, 100)
    color3 = COLORS[randint(0, 5)]
    circle(screen, color3, (x3, y3), r3)

def ball_special():
    '''рисует новый шарик '''
    global x4, y4, r4, ingame
    x4 = randint(100, 1100)
    y4 = randint(100, 900)
    r4 = randint(10, 100)
    circle(screen, (225,0,0), (x4, y4), 15)
    circle(screen, (225, 255, 255), (x4, y4), 10)
    circle(screen, (0, 0, 0), (x4, y4), 5)
    ingame=1
def ball_move(speed,angle):
    global x, y, r, dx,dy,color
    x+=speed*dx
    y+=angle*dy
    circle(screen, color, (x, y), r)


def ball_move2(speed,angle):
    global x2, y2, r2, dx2,dy2,color2
    x2+=speed*dx2
    y2+=angle*dy2
    circle(screen, color2, (x2, y2), r2)


def ball_move3(speed,angle):
    global x3, y3, r3, dx3,dy3,color3
    x3+=speed*dx3
    y3+=angle*dy3
    circle(screen, color3, (x3, y3), r3)




FPS = 50
# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Circles')

combo_counter=0
randomized_angle1=randint(-20,20)
randomized_angle2=randint(-20,20)
randomized_angle3=randint(-20,20)
pygame.display.update()
clock = pygame.time.Clock()
finished = False
new_ball()
new_ball2()
new_ball3()

while not finished:
    screen.blit(textsurface, (900, 100))
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if (((x-event.pos[0])**2+(y-event.pos[1])**2)**(1/2))<=r:
                score+=100-r
                randomized_angle1 = randint(-20, 20)
                new_ball()
                print('Hit!')
            if (((x2-event.pos[0])**2+(y2-event.pos[1])**2)**(1/2))<=r2:
                score += 100 - r2
                randomized_angle2 = randint(-20, 20)
                new_ball2()
                print('Hit!')
            if (((x3-event.pos[0])**2+(y3-event.pos[1])**2)**(1/2))<=r3:
                score += 100 - r3
                randomized_angle3 = randint(-20, 20)
                new_ball3()
                print('Hit!')

            if ingame==1 and (((x4-event.pos[0])**2+(y4-event.pos[1])**2)**(1/2))<=15:
                combo_counter+=1
                score += 20
                print('comboclick!',combo_counter, 'hit CCCOMBO!!!')
            else:
                print('MISS!')
                score-=10

    ball_move(10, randomized_angle1)
    if y > 1000-r or y < 0+r:
        dy *= -1
    if x > 1900-r or x < 0+r:
        dx *= -1


    ball_move2(10,randomized_angle2)
    if y2 > 1000-r2 or y2 < 0+r2:
        dy2 *= -1
    if x2 > 1900-r2 or x2 < 0+r2:
        dx2 *= -1
    ball_move3(10,randomized_angle3)
    if y3 > 1000-r3 or y3 < 0+r3:
        dy3 *= -1
    if x3 > 1900-r3 or x3 < 0+r3:
        dx3 *= -1
    if randint(-200, 200) == 150:
        combo_counter=0
        ball_special()
        pygame.display.update()
        time.sleep(2)
    pygame.display.update()
    screen.fill(BLACK)
print('score=',score)
pygame.quit()

