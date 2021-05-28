import pygame as pg
from pygame.locals import *
import sys, time

window = (500, 500)
WHITE = (255,255,255)
BLACK = (0,0,0)
PINK = (255,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

scenes = {1:WHITE, 2:BLACK, 3:GREEN, 4:PINK, 5:RED, 6:BLUE}
right = {0:1, 1:2, 2:3, 3:4}
left = {0:1, 1:4, 2:3, 3:2}
up = {0:1,1:5,2:3,3:6}
down = {0:1,1:6,2:3,3:4}
rect = pg.Rect(0,0,window[0],window[1])

def terminate():
    pg.quit()
    sys.exit()

pg.init()

chanl = 0
chanr = 0
chand = 0
chanu = 0

w = pg.display.set_mode(window, 0, 32)

while True:
    for ev in pg.event.get():

        if ev.type == QUIT:
            terminate()

        elif ev.type == MOUSEMOTION:
            if ev.pos[0] > window[0] - 100:
                chanr += 1
                if chanr == 4:
                    chanr = 0
                pg.draw.rect(w, scenes[right[chanr]], rect)
                pg.draw.line(w, (0,255,255), (window[0] - 100, 0), (window[0] - 100, window[1]))
                pg.draw.line(w, (0,255,255), (100, 0), (100, window[1]))
                pg.draw.line(w, (0,255,255), (100, window[1] - 100), (window[0] - 100, window[1] - 100))
                pg.draw.line(w, (0,255,255), (100, 100), (window[0] - 100, 100))
                time.sleep(0.75)
                pg.display.update()

            if ev.pos[0] < 100:
                chanl += 1
                if chanl == 4:
                    chanl = 0
                pg.draw.rect(w, scenes[left[chanl]], rect)
                pg.draw.line(w, (0,255,255), (window[0] - 100, 0), (window[0] - 100, window[1]))
                pg.draw.line(w, (0,255,255), (100, 0), (100, window[1]))
                pg.draw.line(w, (0,255,255), (100, window[1] - 100), (window[0] - 100, window[1] - 100))
                pg.draw.line(w, (0,255,255), (100, 100), (window[0] - 100, 100))
                time.sleep(0.75)
                pg.display.update()

            if ev.pos[1] > window[1] - 100 and ev.pos[0] > 100 and ev.pos[0] < window[0] - 100:
                chand += 1
                if chand == 4:
                    chand = 0
                pg.draw.rect(w, scenes[down[chand]], rect)
                pg.draw.line(w, (0,255,255), (window[0] - 100, 0), (window[0] - 100, window[1]))
                pg.draw.line(w, (0,255,255), (100, 0), (100, window[1]))
                pg.draw.line(w, (0,255,255), (100, window[1] - 100), (window[0] - 100, window[1] - 100))
                pg.draw.line(w, (0,255,255), (100, 100), (window[0] - 100, 100))
                time.sleep(0.75)
                pg.display.update()

            if ev.pos[1] < 100 and ev.pos[0] > 100 and ev.pos[0] < window[0] - 100:
                chanu += 1
                if chanu == 4:
                    chanu = 0
                pg.draw.rect(w, scenes[up[chanu]], rect)
                pg.draw.line(w, (0,255,255), (window[0] - 100, 0), (window[0] - 100, window[1]))
                pg.draw.line(w, (0,255,255), (100, 0), (100, window[1]))
                pg.draw.line(w, (0,255,255), (100, window[1] - 100), (window[0] - 100, window[1] - 100))
                pg.draw.line(w, (0,255,255), (100, 100), (window[0] - 100, 100))
                time.sleep(0.75)
                pg.display.update()
