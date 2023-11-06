# 이것은 각 상태들을 객체로 구현한 것임.
PIXEL_PER_METER = 100
RUN_SPEED_KMPH = 8.0
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000.0 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5
FRAMES_PER_TIME = ACTION_PER_TIME * FRAMES_PER_ACTION

from pico2d import get_time, load_image, load_font, clamp,  SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT
import game_world
import game_framework
import random

class Bird:

    def __init__(self):
        self.x, self.y = random.randint(0,1550), random.randint(400,500)
        self.frame = random.randint(0,14)
        self.dir = random.choice([1, -1])
        self.left = 0
        self.bottom = 0
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        self.frame = (self.frame + FRAMES_PER_TIME * game_framework.frame_time) % 14

        if 0 <= int(self.frame) < 5:
            self.left = int(self.frame) * 181
            self.bottom = 165 * 2
        elif 5 <= int(self.frame) < 10:
            self.left = int(self.frame-5) * 181
            self.bottom = 165 * 1
        elif 10 <= int(self.frame) < 14:
            self.left = int(self.frame-10) * 181
            self.bottom = 165 * 0

        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        
        if self.x > 1550:
            self. dir = -1
        
        if self.x < 50:
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.left, self.bottom, 181, 165, self.x, self.y)
        if self.dir == -1:
            self.image.clip_composite_draw(self.left, self.bottom, 181, 165, 0, 'h', self.x, self.y, 180, 180)

        self.font.draw(self.x - 60, self.y + 50, f'{get_time()}', (255, 255, 0))
