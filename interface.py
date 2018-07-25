import pygame

from help_functions import remap

class Interface():
	"""class Interface for score hp and more"""
	def __init__(self, settings, screen):
		self.screen = screen
		self.settings = settings
		self.score = 0
		self.rect = pygame.Rect(0, settings.screen_height - settings.hp_barh, settings.screen_width, settings.hp_barh)
		self.hp = settings.ship_hp

	def update(self, ship):
		"""get current hp and score"""
		self.hp = ship.hp
		self.rect.right = int(remap(self.hp, 0, self.settings.ship_hp, 0, self.settings.screen_width))

	def show(self):
		"""show hp bar and score"""
		pygame.draw.rect(self.screen, self.settings.hp_color, self.rect)