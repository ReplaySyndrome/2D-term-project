from pico2d import *
import game_framework
import BeginningState
import GameState
import time

endbackground = None
showfont = None
pressrimage = None
makingtime = None


def enter():
    global endbackground, showfont,pressrimage,makingtime
    endbackground = load_image('endbg.png')
    showfont = load_font('ENCR10B.TTF', 32)
    pressrimage = load_image('pressr.png')
    makingtime = time.time()
    pass

def draw():
    clear_canvas()

    global showfont
    sc = GameState.getlastscore()
    print(sc)

    endbackground.draw(400,300,800,600)
    showfont.draw(400, 495, str(sc), (0, 56, 174))
    if int(makingtime - time.time()) % 2 == 0:
        pressrimage.draw(700,350)
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
            if event.key == SDLK_r:
                game_framework.change_state(BeginningState)

        if event.type == SDL_QUIT:
            game_framework.quit()
        pass