import pygame
from math import atan2 as arctan2
from bullet import Bullet

class Ship():
    def __init__(self, screen, settings):
        """init ship and start position"""
        self.settings = settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #load ship image 
        self.original_image = pygame.image.load(settings.image_path + settings.file_prefix + settings.hero_path)
        ##self.original_image.centerx = settings.screen_size[0] / 2
        ##self.original_image.centery = settings.screen_size[1] / 2
        self.rect = self.original_image.get_rect()
        self.image = self.original_image
        #set ship start point
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        #ship moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        #ship rotation
        self.rotation = 0
        self.mouse_pos = (0,0)
        #ship bullets
        self.bullets = []

    def shoot(self):
        """create bullet obj"""
        self.bullets.append(Bullet(self.settings, self.screen, self))

    def kill(self, enemys):
        """check if bullet kills enemy"""
        for enemy in enemys:
            for bullet in self.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    enemy.take_damage(bullet.power)
                    if(enemy.hp <= 0):
                        enemys.remove(enemy)
                    self.bullets.remove(bullet)


    def show(self):
        """draw ship"""
        self.screen.blit(self.image, self.rect)

    def update(self):

        """move ship"""
        if self.moving_right:
            self.centerx += self.settings.ship_speed
        if self.moving_left:
            self.centerx -= self.settings.ship_speed
        if self.moving_up:
            self.centery -= self.settings.ship_speed
        if self.moving_down:
            self.centery += self.settings.ship_speed

        #off screen check
        if self.centerx >= self.settings.screen_size[0]:
            self.centerx -= self.settings.ship_speed 
        if self.centerx <= 0:
            self.centerx += self.settings.ship_speed 
        if self.centery >= self.settings.screen_size[1]:
            self.centery -= self.settings.ship_speed 
        if self.centery <= 0:
            self.centery += self.settings.ship_speed 

        #rotation
        x1 = self.centerx
        x2 = float(self.mouse_pos[0])
        y1 = self.settings.screen_size[1] - self.centery
        y2 = self.settings.screen_size[1] - float(self.mouse_pos[1])
        angle = (arctan2((y2-y1),(x2-x1)) * 180.0 / 3.1416) - 90
        self.image = pygame.transform.rotozoom(self.original_image, angle, 1)
        self.rect = self.image.get_rect()
        self.rect.centerx = int(self.centerx)
        self.rect.centery = int(self.centery)
