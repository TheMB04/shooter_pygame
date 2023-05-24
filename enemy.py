import pygame as pg
from random import randint
import math

class Enemy:
    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius
        self._speed = randint(1, 4)
        self._life = 5 - self._speed
        self._g = self._speed*50

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def draw_enemy(self, screen):
        pg.draw.circle(screen, "black", (self._x, self._y), self._radius)
        pg.draw.circle(screen, (0, self._g, 0), (self._x, self._y), (self._radius - 5))

    def follow_player(self, player_x, player_y):
        dx = player_x - self._x
        dy = player_y - self._y

        self._angle = math.atan2(-dy, dx)

        x_speed = math.cos(self._angle)*self._speed
        y_speed = math.sin(self._angle)*-self._speed

        self._x += x_speed
        self._y += y_speed
        

    def detect_bullet_hit(self, bullet_x, bullet_y, bullet_radius):
        dx = bullet_x - self._x
        dy = bullet_y - self._y

        distance = math.sqrt(dx**2+dy**2)
        

        if distance <= self._radius+bullet_radius:
            self._g += 50
            return True

    def detect_player_hit(self, player_x, player_y):
        dx = player_x - self._x
        dy = player_y - self._y

        distance = math.sqrt(dx**2+dy**2)

        if distance <= self._radius*2:
            return True

    def hit(self):
        self._life -= 1

    def get_life(self):
        return self._life