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
Jellies = None
BackGround = None
jellyImage = None
posX = 10


class Cookie:
    def __init__(self):
        self.x, self.y = 60, 120
        self.frame = 0
        self.image = load_image('DJCookie.png')
        self.dir = 1
        self.height = int(229)
        self.width = int(283)
        self.speed = 100
        self.accY = 0
        self.gravity = 30
        self.jumpCount = 0
        self.slide = False
        self.spriteSpeedPerSec = 20
        self.minY = 120

    def update(self):
        if self.slide == True and self.accY == 0:
            self.frame = (self.frame + self.spriteSpeedPerSec * deltaTime) % 2 + 11
        else:
            self.frame = (self.frame + self.spriteSpeedPerSec*deltaTime) % 4

        self.x += self.speed * deltaTime
        if self.accY != 0:
            self.y += self.accY
            self.accY -= self.gravity*deltaTime

        if self.y < self.minY:
            self.y = self.minY
            self.accY = 0
            self.jumpCount = 0


    def draw(self):

        if self.slide == True and self.accY == 0:
            self.image.clip_draw(int(self.frame) * self.width, self.height * 4, self.width, self.height, 60, self.minY,
                                 self.width * 0.7, self.height * 0.7)
        else:
            self.image.clip_draw(int(self.frame) * self.width, self.height * 3,  self.width, self.height, 60 , self.y,
                             self.width*0.7, self.height*0.7)


class Jelly:
    def __init__self(self):
        self.width = 69
        self.height = 68
    def update(self):
        pass

    def draw(self):
        global jellyImage
        global cookie
        jellyImage.clip_draw(68 * self.type ,0, 62 ,62,self.x - cookie.x,self.y + 23,30,30)

    def setPos(self, x, y):
        self.x = x
        self.y = y

    def setType(self, type):
        self.type = type




def enter():
    global cookie, lastTime,Jellies,jellyImage,BackGround

    lastTime = time.time()
    cookie = Cookie()
    Jellies = list()
    for i in range(10000):
        tempJelly = Jelly()
        tempJelly.setPos(i*40 + 300,70)
        tempJelly.setType(random.randint(0,24))
        Jellies.append(tempJelly)
    for i in Jellies:
        print(i.x , i.y)

    jellyImage = load_image('Jelly.png')
    BackGround = load_image("BackGround.png")


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
                    cookie.accY = 7
                    cookie.jumpCount += 1
                    print("PRESS SPACE")

            if event.key == SDLK_j:
                cookie.slide = True
                print("PRESS J")

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_j:
                cookie.slide = False
                print("UP J")






def update():
    global currentTime, deltaTime, lastTime, cookie
    currentTime = time.time()
    deltaTime = currentTime - lastTime
    lastTime = currentTime
    #print(deltaTime)
    cookie.update()


def draw():
    global cookie, Jellies,BackGround,posX
    clear_canvas()
    posX += deltaTime * 50
    BackGround.clip_draw(2 + int(posX),4686 - 1010,800,318,400,300,800,600)
    for jelly in Jellies:
        if 0 < jelly.x - cookie.x < 800:
            jelly.draw()
        elif jelly.x - cookie.x < 0:
            Jellies.remove(jelly)
            print("remove far Jelly")

    cookie.draw()
    update_canvas()

