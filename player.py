import pygame as pg
import math

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
        gun = pg.transform.scale(gun, (90,58))

        dx = mouse_x - self._x
        dy = mouse_y - self._y

        # finner vinkelen mellom musen og bildet "gun" i radianer og gjør det om til grader
        self._angle = math.degrees(math.atan2(-dy, dx))

        # roterer til å peke mot musen
        rotated_gun = pg.transform.rotate(gun, self._angle)
        rect = rotated_gun.get_rect(center=(self._x, self._y))

        screen.blit(rotated_gun, rect)

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