import pygame
from enemy import Enemy
from player import Player
from player import Bullet
import math
from random import randint

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

enemies = []
max_enemies = 5

bullets = []

player = Player(960, 540)
score = 0
old_score = 0

key_a = False
key_d = False
key_w = False
key_s = False
keys_down = 0

while running:

    speed_player = 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                player.left(speed_player)
                key_a = True
                keys_down += 1
            if event.key == pygame.K_d:
                player.right(speed_player)
                key_d = True
                keys_down += 1
            if event.key == pygame.K_w:
                player.up(speed_player)
                key_w = True
                keys_down += 1
            if event.key == pygame.K_s:
                player.down(speed_player)
                key_s = True
                keys_down += 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                key_a = False
                keys_down -= 1
            if event.key == pygame.K_d:
                key_d = False
                keys_down -= 1
            if event.key == pygame.K_w:
                key_w = False
                keys_down -= 1
            if event.key == pygame.K_s:
                key_s = False
                keys_down -= 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                bullet = Bullet(player.get_x(), player.get_y(), player.get_angle())
                bullets.append(bullet)
        
    
    screen.fill("dimgray")

    mouse = pygame.mouse.get_pos()
    player.draw_player(screen, mouse)

    if keys_down == 2:
        speed_player == math.sqrt(speed_player**2/2)

    if key_a:
        player.left(speed_player)
    if key_d:
        player.right(speed_player)
    if key_w:
        player.up(speed_player)
    if key_s:
        player.down(speed_player)
    
    if score - old_score == 10:
        old_score == score
        max_enemies += 1

    if len(enemies) < max_enemies:
        hvor = randint(1, 4)
        if hvor == 1:
            x = 0
            y = randint(0, 1080)
        elif hvor == 2:
            x = 1920
            y = randint(0, 1080)
        elif hvor == 3:
            y = 0
            x = randint(0, 1920)
        else:
            y = 1080
            x = randint(0, 1920)
        enemy = Enemy(x, y)
        enemies.append(enemy)

    for enemy in enemies:
        enemy.draw_enemy(screen)
        enemy.follow_player(player.get_x(), player.get_y())

    for bullet in bullets:
        bullet.draw_bullet(screen)



    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()