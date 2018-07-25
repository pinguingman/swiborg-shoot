import sys
import pygame

import enemy

def check_events(ship):
    """work with button pressed and mouse"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print(sys.argv)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        if event.type == pygame.MOUSEMOTION:
            check_mouse_move_events(event, ship)
        if event.type == pygame.MOUSEBUTTONDOWN:
            check_mouse_press_events(event, ship)

def check_mouse_move_events(event, ship):
    ship.mouse_pos = event.pos

def check_mouse_press_events(event, ship):
    ship.shoot()

def check_keydown_events(event, ship):
    """work with keydown events"""
    if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
        ship.moving_right = True
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = True
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = True
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = True
    if event.key == pygame.K_r:
        print("Oh hi Mark")

def check_keyup_events(event, ship):
    """work with keyup events"""
    if (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
        ship.moving_right = False
    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
        ship.moving_left = False
    if event.key == pygame.K_UP or event.key == pygame.K_w:
        ship.moving_up = False
    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
        ship.moving_down = False

def next_lvl(screen, settings, enemys):
    lvl_number = settings.lvl_number
    if lvl_number < len(settings.lvl['enemy_type']):
        enemy_type = settings.lvl['enemy_type'][lvl_number]
        enemy_number = settings.lvl['enemy_number'][lvl_number]
        for i in range(enemy_number):
            if enemy_type == 'normal':
                enemys.append(enemy.Enemy(screen, settings))
            if enemy_type == 'fast':
                enemys.append(enemy.EnemyFast(screen, settings))
            if enemy_type == 'fat':
                enemys.append(enemy.EnemyFat(screen, settings))
            if enemy_type == 'boss':
                enemys.append(enemy.EnemyBoss(screen, settings))
    settings.lvl_number += 1

def update_screen(settings, screen, ship, enemys, interface):
    """updates screen and show new screen"""
    screen.fill(settings.bg_color)    
    for bullet in ship.bullets:
        if bullet.update():
            ship.bullets.remove(bullet)
        else:
            bullet.show()
    ship.kill(enemys)
    ship.update()
    ship.show()
    if not enemys:
        next_lvl(screen, settings, enemys)
    for enemy in enemys:
        enemy.update(ship)
        enemy.show()
    ship.under_attack(enemys)

    interface.update(ship)
    interface.show()


