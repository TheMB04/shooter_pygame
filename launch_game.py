import pygame
from enemy import Enemy
from player import Player
import math

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

enemies = []

bullets = []

player = Player(960, 540)

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
                player.shoot()
        
    
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
    
    


    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()