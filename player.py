import pygame as pg
import math

class Player:
    def __init__(self, x, y, radius):
        self._x = x
        self._y = y
        self._radius = radius

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_angle(self):
        return self._angle

    def draw_player(self, screen, mouse):
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        gun = pg.image.load("gun.png")
        gun = pg.transform.scale(gun, (90,58))

        dx = mouse_x - self._x
        dy = mouse_y - self._y

        # finner vinkelen mellom musen og bildet "gun" i radianer
        self._angle = math.atan2(-dy, dx)

        # regner ut hvor mye utafor spilleren pistolen/hånden skal være i x og y retning relativ til hvor musen er
        x_out = math.cos(self._angle)*75
        y_out = math.sin(self._angle)*-75

        # gjør radianer om til grader
        self._angle = math.degrees(self._angle)

        # roterer til å peke mot musen
        rotated_gun = pg.transform.rotate(gun, self._angle)
        # lager en rektangel med lik størrelse som bildet
        rect = rotated_gun.get_rect(center=((self._x+x_out), (self._y+y_out)))

        screen.blit(rotated_gun, rect)
        pg.draw.circle(screen, "black", (self._x, self._y), self._radius)
        pg.draw.circle(screen, "darkred", (self._x, self._y), (self._radius - 5))

    def left(self, speed):
        self._x -= speed

    def right(self, speed):
        self._x += speed

    def up(self, speed):
        self._y -= speed

    def down(self, speed):
        self._y += speed


class Bullet:
    def __init__(self, x, y, angle, radius):
        self._angle = math.radians(angle)
        self._x_speed = math.cos(self._angle)*8
        self._y_speed = math.sin(self._angle)*-8
        self._radius = radius
        self._x = x + self._x_speed*15
        self._y = y + self._y_speed*15

    def draw_bullet(self, screen):
        pg.draw.circle(screen, "black", (self._x, self._y), self._radius)
        self._x += self._x_speed
        self._y += self._y_speed

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y