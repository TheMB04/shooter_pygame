import pygame as pg
from random import randint

class Enemy:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._speed = randint(1, 4)
        self._life = 5 - self._speed
        self._g = self._life*50

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def draw_enemy(self, screen):
        pg.draw.circle(screen, "black", (self._x, self._y), 55)
        pg.draw.circle(screen, (0, self._g, 0), (self._x, self._y), 50)

    def hit(self):
        pass