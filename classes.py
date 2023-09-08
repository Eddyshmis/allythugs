from typing import Any
from random import randint
import pygame


class Button():
	def __init__(self, x:int, y:int, image, scale:int):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
class image():
	def __init__(self, x:int, y:int, image, scale:int):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
	def draw(self, surface):

		surface.blit(self.image, (self.rect.x, self.rect.y))

	def draw_multiple(self,surface,amount:int):
		pos_list = [(865, 86), (41, 464), (309, 328), (552, 271), (320, 486), (144, 274), (664, 465), (134, 186), (551, 219), (246, 211), (602, 282), (475, 147), (859, 429), (730, 278), (753, 405), (431, 549), (923, 516), (636, 498)]
		for num in range(amount):
			surface.blit(self.image,pos_list[num])
	def set_vis(self,alpha):
		self.image.set_alpha(alpha)
	def rotate_draw(self, rotation:int):
		self.image = pygame.transform.rotate(self.image,rotation)

		
