import random
import json
import os
import time

from pico2d import *

import game_framework


name = "GameState"

cookie = None
lastTime = None
deltaTime = None
currentTime = None
jellys = None

#JImage = load_image('JELLY.png')


class Cookie:
    def __init__(self):
        self.x, self.y = 50, 90
        self.frame = 0
        self.image = load_image('DJCookie.png')
        self.dir = 1
        self.height = int(229)
        self.width = int(283)
        self.speed = 5
        self.accY = 0
        self.gravity = 140
        self.jumpCount = 0

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.speed * deltaTime
        if self.accY != 0:
            self.y += self.accY
            self.accY -= self.gravity*deltaTime

        if self.y < 89:
            self.y = 90
            self.accY = 0
            self.jumpCount = 0


    def draw(self):
        self.image.clip_draw(self.frame * self.width, self.height * 3,  self.width, self.height, 50 , self.y,
                             self.width*0.7, self.height*0.7)
        #print(self.x)

class Jelly:
    def __init__self(self):
        self.width = 69
        self.height = 68
    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(self.type * self.width, 1936, self.width,self.height ,self.x,self.y)

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def setType(self, type):
        self.type = type




def enter():
    global cookie, lastTime,jellys
    lastTime = time.time()
    cookie = Cookie()
    jellys = list()
    for i in range(10000):
        tempJelly = Jelly()
        tempJelly.setPos(i*10 + 50,90)
        tempJelly.setType(random.randint(0,30))
        jellys.append(tempJelly)
    for i in jellys:
        print(i.x)


def exit():
    global cookie
    del(cookie)


def pause():
    pass


def resume():
    pass


def handle_events():
    global cookie
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                if cookie.jumpCount < 2:
                    cookie.accY = 60
                    cookie.jumpCount += 1
                    print("PRESS SPACE")



def update():
    global currentTime, deltaTime, lastTime, cookie
    currentTime = time.time()
    deltaTime = currentTime - lastTime
    lastTime = currentTime
    #print(deltaTime)
    cookie.update()


def draw():
    global cookie,jellys

    clear_canvas()
    #for jelly in jellys:
    #     if 0 < jelly.x - cookie.x < 800:
    #        jelly.draw()
    cookie.draw()
    update_canvas()
    delay(0.1)
