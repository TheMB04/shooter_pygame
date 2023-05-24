import pygame
from enemy import Enemy
from player import Player
from player import Bullet
import math
from random import randint

pygame.init()
display_info = pygame.display.Info()
screen = pygame.display.set_mode((display_info.current_w, display_info.current_h))
clock = pygame.time.Clock()
running = True

enemies = []
max_enemies = 5

bullets = []

radius = 55
bullet_radius = 6

score = 0
old_score = 0

game_state = "start_menu"

key_a = False
key_d = False
key_w = False
key_s = False
keys_down = 0

font_score = pygame.font.SysFont("Impact", 104)

while running:

    speed_player = 3

    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if event.key == pygame.K_r:
                if game_state == "start_menu" or game_state == "game_over":
                    player = Player(display_info.current_w/2, display_info.current_h/2, radius)

                    score = 0
                    old_score = 0

                    game_state = "running"


        if game_state == "running":
            if player.get_x() < 0:
                key_a = False
                keys_down -= 1

            elif player.get_x() > display_info.current_w:
                key_d = False
                keys_down -= 1

            elif player.get_y() < 0:
                key_w = False
                keys_down -= 1

            elif player.get_y() > display_info.current_h:
                key_s = False
                keys_down -= 1

            
            if event.type == pygame.KEYDOWN:

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

                if event.key == pygame.K_SPACE:
                    bullet = Bullet(player.get_x(), player.get_y(), player.get_angle(), bullet_radius)
                    bullets.append(bullet)
                

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
                    bullet = Bullet(player.get_x(), player.get_y(), player.get_angle(), bullet_radius)
                    bullets.append(bullet)
        
    
    screen.fill("dimgray")

    mouse = pygame.mouse.get_pos()

    if game_state == "start_menu":
        text = font_score.render(f"Press 'r' to play", True, (255, 255, 255))
        text_rect = text.get_rect(center=(display_info.current_w/2, 100))
        screen.blit(text, text_rect)

        text = font_score.render(f"Or press 'Esc' to exit", True, (255, 255, 255))
        text_rect = text.get_rect(center=(display_info.current_w/2, 550))
        screen.blit(text, text_rect)


    elif game_state == "running":
        player.draw_player(screen, mouse)

        if keys_down == 2:
            speed_player = math.sqrt(speed_player**2/2)

        if key_a:
            player.left(speed_player)
        if key_d:
            player.right(speed_player)
        if key_w:
            player.up(speed_player)
        if key_s:
            player.down(speed_player)
        
        if score - old_score == 10:
            old_score = score
            max_enemies += 1


        if len(enemies) < max_enemies:

            hvor = randint(1, 4)

            if hvor == 1:
                x = 0
                y = randint(0, display_info.current_h)
            elif hvor == 2:
                x = display_info.current_w
                y = randint(0, display_info.current_h)
            elif hvor == 3:
                y = 0
                x = randint(0, display_info.current_w)
            else:
                y = display_info.current_h
                x = randint(0, display_info.current_w)

            enemy = Enemy(x, y, radius)
            enemies.append(enemy)
            

        for bullet in bullets:

            bullet.draw_bullet(screen)

            if bullet.get_x() > display_info.current_w + 10 or bullet.get_x() < -10:
                bullets.remove(bullet)
                del bullet

            elif bullet.get_y() > display_info.current_h + 10 or bullet.get_y() < -10:
                bullets.remove(bullet)
                del bullet


        for enemy in enemies:
            enemy.draw_enemy(screen)
            enemy.follow_player(player.get_x(), player.get_y())

            if enemy.detect_player_hit(player.get_x(), player.get_y()):
                game_state = "game_over"
                key_a = False
                key_d = False
                key_w = False
                key_s = False
                keys_down = 0

            for bullet in bullets:
                if enemy.detect_bullet_hit(bullet.get_x(), bullet.get_y(), bullet_radius):
                    enemy.hit()
                    bullets.remove(bullet)
                    del bullet

            if enemy.get_life() <= 0:
                enemies.remove(enemy)
                del enemy
                score += 1
            

        if score >= 10:
            points = font_score.render(f"Score: {score}", True, (200,197,24))
            text_rect = points.get_rect(center=(display_info.current_w/2, 100))
            screen.blit(points, text_rect)

        elif score >= 100:
            points = font_score.render(f"Score: {score}", True, (200,197,24))
            text_rect = points.get_rect(center=(display_info.current_w/2, 100))
            screen.blit(points, text_rect)

        else:
            points = font_score.render(f"Score: {score}", True, (200,197,24))
            text_rect = points.get_rect(center=(display_info.current_w/2, 100))
            screen.blit(points, text_rect)


    elif game_state == "game_over":
        for enemy in enemies:
            enemies.remove(enemy)
            del enemy

        for bullet in bullets:
            bullets.remove(bullet)
            del bullet

        text = font_score.render(f"GAME OVER", True, (180, 0, 0))
        text_rect = text.get_rect(center=(display_info.current_w/2, 100))
        screen.blit(text, text_rect)

        text = font_score.render(f"Your score: {score}", True, (200,197,24))
        text_rect = text.get_rect(center=(display_info.current_w/2, 250))
        screen.blit(text, text_rect)

        text = font_score.render(f"Press 'r' to try again", True, (255, 255, 255))
        text_rect = text.get_rect(center=(display_info.current_w/2, 400))
        screen.blit(text, text_rect)

        text = font_score.render(f"Or press 'Esc' to exit", True, (255, 255, 255))
        text_rect = text.get_rect(center=(display_info.current_w/2, 550))
        screen.blit(text, text_rect)
    


    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()