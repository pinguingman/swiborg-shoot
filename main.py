import sys
import pygame

from settings import Settings
from ship import Ship
from enemy import Enemy
import game_functions as gf
import help_functions as hf

def run_game():
        #init game, settings and ship
        pygame.init()
        settings = Settings()
        hf.prepare(settings)
        screen = pygame.display.set_mode(settings.screen_size)
        pygame.display.set_caption("Swiborg Shoot")
        ship = Ship(screen, settings)
        enemys = []
        while True:
            gf.update_screen(settings, screen, ship, enemys)
            #mouse and keyboarf events
            gf.check_events(ship)
            #last screen show
            pygame.display.flip()

run_game()