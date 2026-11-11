import random

from pico2d import SDL_KEYDOWN, SDL_QUIT, SDLK_ESCAPE, clear_canvas, get_events, update_canvas

import game_framework
import game_world
from bird import Bird
from boy import Boy
from grass import Grass

boy = None
NUM_BIRDS = 10
MIN_BIRD_Y = 180
LANE_SPACING = 44
LANE_JITTER = 3


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            game_framework.quit()
            return
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
            return
        boy.handle_event(event)


def init():
    global boy
    game_world.clear()
    boy = Boy()
    game_world.add_oject(boy)
    game_world.add_oject(Grass(), 0)
    lanes = list(range(NUM_BIRDS))
    directions = [1] * (NUM_BIRDS // 2) + [-1] * (NUM_BIRDS // 2)
    random.shuffle(lanes)
    random.shuffle(directions)
    for lane, direction in zip(lanes, directions):
        bird = Bird(
            x=random.uniform(0, 1600),
            y=MIN_BIRD_Y + lane * LANE_SPACING + random.uniform(0, LANE_JITTER),
            speed=random.uniform(90, 180),
            direction=direction,
        )
        game_world.add_oject(bird)


def update():
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    global boy
    game_world.clear()
    boy = None


def pause():
    if boy is not None:
        boy.pause()


def resume():
    pass
