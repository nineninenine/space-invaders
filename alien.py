import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""a clss to represent a single alien on the screen"""

	def __init__(self, ai_settings, screen):
		"""init the alien and its starting position"""
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		#load the alien and get its rect
		self.image = pygame.image.load("images/alien.bmp")
		self.rect = self.image.get_rect()

		#start every alien in the top left
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#store the aliens exact position
		self.x = float(self.rect.x)


	def check_edges(self):
		"""return true if the alien is at the edge of the screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True



	def update(self):
		"""move the alien left or right"""
		#called by the group obj
		#if fleet_direction is postitive, positive ints are added to the x-coord == moves right
		#if fleet_direction is negative, negative ints are added to x-coord == moves left
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x


	def blitme(self):
		"""draw the aliens current position"""
		self.screen.blit(self.image, self.rect)

