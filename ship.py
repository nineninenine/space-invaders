import pygame


class Ship():
	"""init the ship and its starting position"""
	def __init__(self, screen):

		self.screen = screen
		#load the shhip and get its rect.
		self.image = pygame.image.load("images/ship.bmp")
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()

		#start each new ship at the bottom center of the screen.

		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

	def blitme(self):
		"""draw the ship at its current location"""
		self.screen.blit(self.image, self.rect)