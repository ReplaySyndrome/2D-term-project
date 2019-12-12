from pico2d import *
import game_framework
import GameState
import time

Djbackground = None
pressimage = None
makingtime = None

def enter():
    global Djbackground, pressimage, makingtime
    Djbackground = load_image('bgimage.png')
    pressimage = load_image('pressimage.png')
    makingtime = time.time()
    pass

def draw():
    clear_canvas()
    global Djbackground
    Djbackground.draw(400,300)
    
    if int((makingtime - time.time()) %2 ) == 0:
        pressimage.draw(400,300)
    update_canvas()
    pass

def update():
    pass

def exit():
    pass


def pause():
    pass


def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            game_framework.change_state(GameState)

        if event.type == SDL_QUIT:
            game_framework.quit()
        pass