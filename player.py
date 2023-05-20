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
        mouse_x = mouse[0]
        mouse_y = mouse[1]
        gun = pg.image.load("shooter_pygame\gun.png")
        gun = pg.transform.scale(gun, (90,58))

        dx = mouse_x - self._x
        dy = mouse_y - self._y

        # finner vinkelen mellom musen og bildet "gun" i radianer
        angle = math.atan2(-dy, dx)

        # regner ut hvor mye utafor spilleren pistolen/hånden skal være i x og y retning relativ til hvor musen er
        x_out = math.cos(angle)*75
        y_out = math.sin(angle)*-75

        print(x_out, y_out)
        # gjør radianer om til grader
        angle = math.degrees(angle)

        # roterer til å peke mot musen
        rotated_gun = pg.transform.rotate(gun, angle)
        # lager en rektangel med lik størrelse som bildet
        rect = rotated_gun.get_rect(center=((self._x+x_out), (self._y+y_out)))

        screen.blit(rotated_gun, rect)
        pg.draw.circle(screen, "black", (self._x, self._y), 55)
        pg.draw.circle(screen, "darkred", (self._x, self._y), 50)

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