import pygame as pg
import math as m

class Player:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def draw_player(self, screen, mouse):
        pg.draw.circle(screen, "black", (self._x, self._y), 55)
        pg.draw.circle(screen, "darkred", (self._x, self._y), 50)
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        gun = pg.image.load("shooter_pygame\gun.png")
        pg.transform.rotate(gun, 45)

    def left(self):
        pass

    def right(self):
        pass

    def up(self):
        pass

    def down(self):
        pass

    def shoot(self):
        pass


class Bullet:
    def __init__(self, x, y, angle):
        self._x = x
        self._y = y
        self._angle = angle