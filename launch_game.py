import pygame
from enemy import Enemy
from player import Player

pygame.init()
screen = pygame.display.set_mode((1920, 1080))
clock = pygame.time.Clock()
running = True

enemies = []

bullets = []

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_a:
                player.left()
            if event.key == pygame.K_d:
                player.right()
            if event.key == pygame.K_w:
                player.up()
            if event.key == pygame.K_s:
                player.down()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                player.shoot()

    
    screen.fill("dimgray")

    





    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()