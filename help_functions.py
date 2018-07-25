from math import sqrt

import pygame

def convert_image(image_full_path, size, prefix, path_image_folder, file_name):
    """conver image to game format"""
    image = pygame.image.load(image_full_path)
    image = pygame.transform.scale(image, size)
    pygame.image.save(image, path_image_folder + prefix + file_name)

def prepare(settings):
    """game preparations"""
    #convert all game images
    convert_image(settings.hero_full_path, settings.ship_size, settings.file_prefix, settings.image_path, settings.hero_path)
    convert_image(settings.enemy_full_path, settings.enemy_size, settings.file_prefix, settings.image_path, settings.enemy_path)
    convert_image(settings.enemy_damaged_full_path, settings.enemy_size, settings.file_prefix, settings.image_path, settings.enemy_damaged_path)

def calculate_unit_vector(x0, y0, x1, y1):
    """calculate unit vector by 2 dots"""
    v = (x1 - x0, y1 - y0)
    vM = sqrt(v[0] ** 2 + v[1] ** 2)
    return (v[0] / vM, v[1] / vM)

def remap(value, minf, maxf, mins, maxs):
	"""remap a number from one range to another"""
	return mins + (value - minf) * (maxs - mins) / (maxf - minf);

def dist(x0, y0, x1, y1):
	"""calculate dist between 2 dots"""
	return float(sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2))

def collision_test_circle(x0, y0, r0, x1, y1, r1):
	"""test colllision between 2 circles"""
	if dist(x0, y0, x1, y1) < float(r0 + r1):
		return True
	else:
		return False
