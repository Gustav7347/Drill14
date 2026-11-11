from pico2d import get_canvas_width, load_image

import game_framework

FRAME_WIDTH = 183
FRAME_HEIGHT = 168
FRAME_COUNT = 14
FRAME_COLUMNS = 5
FRAME_ROWS = 3
DOWNSTROKE_FRAMES = 10
DOWNSTROKE_FRAME_TIME = 0.035
UPSTROKE_FRAME_TIME = 0.11
DRAW_WIDTH = 48
DRAW_HEIGHT = 40


class Bird:
    image = None

    def __init__(self, x, y, speed, direction=1):
        if Bird.image is None:
            Bird.image = load_image('bird_animation.png')
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.frame = 0
        self.frame_elapsed = 0.0

    def update(self):
        frame_time = game_framework.frame_time
        self.x += self.direction * self.speed * frame_time
        if self.x > get_canvas_width() + DRAW_WIDTH / 2:
            self.x = -DRAW_WIDTH / 2
        elif self.x < -DRAW_WIDTH / 2:
            self.x = get_canvas_width() + DRAW_WIDTH / 2

        self.frame_elapsed += frame_time
        while True:
            duration = (DOWNSTROKE_FRAME_TIME
                        if self.frame < DOWNSTROKE_FRAMES
                        else UPSTROKE_FRAME_TIME)
            if self.frame_elapsed < duration:
                break
            self.frame_elapsed -= duration
            self.frame = (self.frame + 1) % FRAME_COUNT

    def draw(self):
        column = self.frame % FRAME_COLUMNS
        row_from_top = self.frame // FRAME_COLUMNS
        row_from_bottom = FRAME_ROWS - 1 - row_from_top
        Bird.image.clip_composite_draw(
            column * FRAME_WIDTH,
            row_from_bottom * FRAME_HEIGHT,
            FRAME_WIDTH,
            FRAME_HEIGHT,
            0,
            'h' if self.direction < 0 else '',
            self.x,
            self.y,
            DRAW_WIDTH,
            DRAW_HEIGHT,
        )
