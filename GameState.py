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
background = None
jellyImage = None
flyingObstacleImage = None
flyingObstacles = None
groundImage = None
grounds = None


class Cookie:
    def __init__(self):
        self.x, self.y = 60, 120
        self.frame = 0
        self.image = load_image('DJCookie.png')
        self.dir = 1
        self.height = int(229)
        self.width = int(283)
        self.speed = 150
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

class BackGround:
    def __init__(self):
        self.image = load_image("BackGround.png")
        self.positionX = 0
        self.speedX = 1

    def update(self):
        global deltaTime
        self.positionX = self.positionX + deltaTime * self.speedX

    def draw(self):
        global deltaTime
        #print(self.positionX, deltaTime)
        self.image.clip_draw(2 + int(self.positionX), 4686 - 1010, 200, 318, 400, 300, 800, 600)

class FlyingObstacle:
    def __init__(self):
        self.width = 123
        self.height = 90
        self.frame = 0
        self.spriteSpeedPerSec = 20

    def update(self):
        global deltaTime
        self.frame = (self.frame + deltaTime* self.spriteSpeedPerSec) % 3

    def draw(self):
        global flyingObstacleImage
        flyingObstacleImage.clip_draw(self.width * int(self.frame),0,self.width,self.height,self.x - cookie.x,self.y)

    def setPos(self,x,y):
        self.x = x
        self.y = y

    def setType(self,type):
        self.type = type


class Ground:
    def __init__(self):
        self.x = 0
        self.y = 0

    def draw(self):
        global groundImage
        groundImage.draw(self.x - cookie.x,self.y)

    def update(self):
        pass

    def setType(self,type):
        self.type = type

    def setPos(self,x,y):
        self.x = x
        self.y = y







def enter():
    global cookie, lastTime,Jellies,jellyImage,background,flyingObstacles,flyingObstacleImage,groundImage,grounds

    lastTime = time.time()
    cookie = Cookie()
    Jellies = list()
    grounds =  list()

    for i in range(100000):
        tempGround = Ground()
        tempGround.setPos(124*i,-20)
        grounds.append(tempGround)


    for i in range(100000):
        tempJelly = Jelly()
        if 240 <= (i*40 + 300) % 400 <= 320:
            tempJelly.setPos(i * 40 + 300, 40)
        else:
            tempJelly.setPos(i*40 + 300, 70)
        tempJelly.setType(random.randint(0, 24))
        Jellies.append(tempJelly)
    flyingObstacles = list()
    for i in range(100):
        temp = FlyingObstacle()
        temp.setPos(i*400 - 100,150)
        flyingObstacles.append(temp)

    jellyImage = load_image('Jelly.png')
    flyingObstacleImage = load_image("FlyingObstacle1.png")
    groundImage = load_image("Ground.png")
    background = BackGround()


def exit():
    pass


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
    global currentTime, deltaTime, lastTime, cookie,background,flyingObstacles
    currentTime = time.time()
    deltaTime = currentTime - lastTime
    lastTime = currentTime
    #print(deltaTime)
    for i in range (100):
        flyingObstacles[i].update()
        if flyingObstacles[i].x - cookie.x > 800:
            break

    background.update()
    cookie.update()


def draw():
    global cookie, Jellies,background
    clear_canvas()
    background.draw()
    for jelly in Jellies:
        if 0 < jelly.x - cookie.x < 800:
            jelly.draw()
        elif jelly.x - cookie.x < 0:
            Jellies.remove(jelly)
            #print("remove far Jelly")
        elif jelly.x - cookie.x >= 1000:
            break

    for flyingObstacle in flyingObstacles:
        if 0 < flyingObstacle.x - cookie.x < 800:
            flyingObstacle.draw()
        elif flyingObstacle.x - cookie.x < -200:
            flyingObstacles.remove(flyingObstacle)
            #print("remove far Obstacle")
        elif flyingObstacle.x - cookie.x >= 1000:
            break

    for ground in grounds:
        if -200 < ground.x - cookie.x < 1000:
            ground.draw()
        elif ground.x - cookie.x < -400:
            grounds.remove(ground)
            print("remove far Obstacle")
        elif ground.x - cookie.x >= 1000:
            break

    cookie.draw()
    update_canvas()

