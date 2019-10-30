import random
import json
import os

from pico2d import *

import game_framework


name = "GameState"

cookie = None


class Cookie:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('114550.png')
        self.dir = 1
        self.height = int(229)
        self.width = int(283)

    def update(self):
        self.frame = (self.frame + 1) % 4
        self.x += self.dir
        if self.x >= 800:
            self.dir = -1
        elif self.x <= 0:
            self.dir = 1

    def draw(self):
        self.image.clip_draw(self.frame * self.width, self.height * 3,  self.width, self.height, self.x, self.y,self.width*0.7,self.height*0.7)


def enter():
    global cookie
    cookie = Cookie()


def exit():
    global cookie
    del(cookie)


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.pop_state()


def update():
    cookie.update()


def draw():
    clear_canvas()

    cookie.draw()
    update_canvas()
    delay(0.1)
