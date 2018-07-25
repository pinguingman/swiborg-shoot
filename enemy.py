import pygame
from random import seed, randint, uniform

from help_functions import calculate_unit_vector

class Enemy():
    """class controlls enemys"""
    def __init__(self, screen, settings):
        """create enemy object and load params"""
        #load image        
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load(settings.image_path + settings.file_prefix + settings.enemy_path)
        self.image_damaged = pygame.image.load(settings.image_path + settings.file_prefix + settings.enemy_damaged_path)
        self.rect = self.image.get_rect()
        #coordinates
        seed()
        self.rect.centerx = randint(0, settings.screen_size[0])
        self.rect.centery = randint(0, settings.screen_size[1])
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        #params (hp, speed)
        self.hp = settings.enemy_hp
        self.being_damaged = 0
        self.speed = settings.enemy_speed 
        self.damage = settings.enemy_damage

    def show(self):
        """show enemy""" 
        if self.being_damaged > 0:
            self.screen.blit(self.image_damaged, self.rect)
            self.being_damaged -= 1
        else:
            self.screen.blit(self.image, self.rect)    

    def take_damage(self, damage):
        """take famage from bullet"""
        self.hp -= damage
        self.being_damaged = self.settings.damage_frame_time

    def update(self, ship):
        """move enemy"""
        #search hero ship
        move_vector = calculate_unit_vector(self.centerx, self.centery, ship.centerx + uniform(-10, 10), ship.centery + uniform(-10, 10))
        self.centerx += move_vector[0] * self.speed
        self.centery += move_vector[1] * self.speed
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

class EnemyFast(Enemy):
    """faster enemy class"""
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.hp = settings.enemy_hp / 2
        self.speed = settings.enemy_speed * 2
        self.image = pygame.transform.rotozoom(self.image, 0, 0.5)
        self.image_damaged = pygame.transform.rotozoom(self.image_damaged, 0, 0.5)
        self.rect = self.image.get_rect()

class EnemyFat(Enemy):
    """bigger enemy class"""
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.hp = settings.enemy_hp * 2
        self.speed = settings.enemy_speed / 0.75
        self.image = pygame.transform.rotozoom(self.image, 0, 1.5)
        self.image_damaged = pygame.transform.rotozoom(self.image_damaged, 0, 1.5)
        self.rect = self.image.get_rect()

class EnemyBoss(Enemy):
    """boss enemy class"""
    def __init__(self, screen, settings):
        super().__init__(screen, settings)
        self.hp = settings.enemy_hp * 10
        self.speed = settings.enemy_speed / 0.75
        self.image = pygame.transform.rotozoom(self.image, 0, 3)
        self.image_damaged = pygame.transform.rotozoom(self.image_damaged, 0, 3)
        self.rect = self.image.get_rect()
    def update(self, ship):
        pass
