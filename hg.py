import pygame as pg
from pygame.locals import *
import sys, time

speed = 1

window = (700, 700)
WHITE = (255,255,255)
SKY = (0,255,255)
BLACK = (0,0,0)
PINK = (255,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

scenes = {1:SKY, 2:BLACK, 3:GREEN, 4:PINK, 5:RED, 6:BLUE}
right = {0:1, 1:2, 2:3, 3:4}
left = {0:1, 1:4, 2:3, 3:2}
up = {0:1,1:5}
down = {0:1,1:6}

def disp_up(mode, objects, rects, wind):
  if mode == 'r':
    for i in objects:
      
      pg.draw.rect(wind, i, rects[objects.index(i)])
      pg.display.update()

  elif mode == 'i':
    for i in objects:

      wind.blit(i, rects[objects.index(i)])
      pg.display.update()

def terminate():
  pg.quit()
  sys.exit()

pg.init()

chanl = 0
chanr = 0
chand = 0
chanu = 0

x = 0
y = 0
x1 = 0
y1 = 0

X_of_Y = window[1]/window[0]
distance = 100
dis_plus = False
dis_minus = False
smena = True

u = False
d = False
l = False
r = False

w = pg.display.set_mode(window, 0, 32)
rect = pg.Rect(int((window[0] / 2) - distance), int(((window[1] / 2) - distance) * X_of_Y), 1 + (2 * distance), int((1 + (2 * distance)) * X_of_Y))

while True:
  w.fill(WHITE)
  for ev in pg.event.get():

    if ev.type == QUIT:
      terminate()

    elif ev.type == MOUSEMOTION and smena:

      x = ev.pos[0]
      y = ev.pos[1]

      u = False
      d = False
      l = False
      r = False
        
      if x - x1 <= -10:
        chanr += 1
        if chanr == 4:
          chanr = 0
        disp_up('r', [scenes[right[chanr]]], [rect], w)
        r = True

      if x - x1 >= 10:
        chanl += 1
        if chanl == 4:
          chanl = 0
        disp_up('r', [scenes[left[chanl]]], [rect], w)
        l = True

      if y - y1 <= -10:
        chand += 1
        if chand == 2:
          chand = 0
        disp_up('r', [scenes[down[chand]]], [rect], w)
        d = True

      if y - y1 >= 10:
        chanu += 1
        if chanu == 2:
          chanu = 0
        disp_up('r', [scenes[up[chanu]]], [rect], w)
        u = True

      smena = False

    elif ev.type == MOUSEBUTTONUP:
      if ev.button == 3:
        smena = True

    elif ev.type == KEYDOWN:

      if ev.key == K_w:
        dis_plus = True
        time.sleep(0.5)

      elif ev.key == K_s:
        dis_minus = True
        time.sleep(0.5)

    elif ev.type == KEYUP:
      
      if ev.key == K_w:
        dis_plus = False

      elif ev.key == K_s:
        dis_minus = False

  if dis_plus and distance < window[0] / 2:
    distance += speed

  elif dis_minus and distance > 10:
    distance -= speed
    
  rect = pg.Rect(int((window[0] / 2) - distance), int(((window[1] / 2) - distance) * X_of_Y), 1 + (2 * distance), int((1 + (2 * distance)) * X_of_Y))

  if u:
    disp_up('r', [scenes[up[chanu]]], [rect], w)
  elif d:
    disp_up('r', [scenes[down[chand]]], [rect], w)
  elif r:
    disp_up('r', [scenes[right[chanr]]], [rect], w)
  elif l:
    disp_up('r', [scenes[left[chanl]]], [rect], w)

  x1 = x
  y1 = y
