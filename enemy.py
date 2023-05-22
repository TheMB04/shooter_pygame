import pygame as pg
from random import randint
import math

class Enemy:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._speed = randint(1, 4)
        self._life = 5 - self._speed
        self._g = self._speed*50

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def draw_enemy(self, screen):
        pg.draw.circle(screen, "black", (self._x, self._y), 55)
        pg.draw.circle(screen, (0, self._g, 0), (self._x, self._y), 50)

    def follow_player(self, player_x, player_y):
        dx = player_x - self._x
        dy = player_y - self._y

        self._angle = math.atan2(-dy, dx)

        x_speed = math.cos(self._angle)*self._speed
        y_speed = math.sin(self._angle)*-self._speed

        self._x += x_speed
        self._y += y_speed
        

    def detect_bullet_hit(self, bullet_x, bullet_y):
        pass

    def detect_player_hit(self, player_x, player_y):
        pass