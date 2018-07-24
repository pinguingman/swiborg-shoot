import pygame
from help_functions import calculate_unit_vector

class Bullet():
    """class for controll bullets shout from ship"""
    def __init__(self, settings, screen, ship):
        """create bullet object in current ship location"""
        self.settings = settings
        self.screen = screen
        #creating bullet rect
        self.bullet_size = self.settings.bullet_width
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.centerx = ship.centerx
        self.rect.centery = ship.centery
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
        #calculate unit vector
        self.move_vector = calculate_unit_vector(self.x, self.y, ship.mouse_pos[0], ship.mouse_pos[1])
        #other parameters
        self.power = self.settings.bullet_power
        self.color = self.settings.bullet_color


    def update(self):
        """update bullet position"""
        self.x += self.move_vector[0] * self.settings.bullet_speed
        self.y += self.move_vector[1] * self.settings.bullet_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if self.x < 0 or self.x > self.settings.screen_size[0] or self.y < 0 or self.y > self.settings.screen_size[1]:
            return True

    def show(self):
        """draw ship"""
        pygame.draw.circle(self.screen, self.color, (self.rect.x, self.rect.y), int(self.bullet_size / 2))