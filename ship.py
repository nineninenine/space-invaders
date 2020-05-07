import pygame


class Ship():
	"""init the ship and its starting position"""
	def __init__(self, screen):

		self.screen = screen
		self.image = pygame.image.load("images/ship.bmp")
		#load the shhip and get its rect.
		#the rect attribute are rectangles that represent game elements even
		#if they are not shaped exactly like rectangles.
		#“When working with a rect object, you can use the x- and 
		#y-coordinates of the top, bottom, left, and right edges 
		#of the rectangle, as well as the center. You can set 
		#any of these values to determine the current position of the rect”

		#get the rect of the ship
		self.rect = self.image.get_rect()

		#get the rect of the screen
		self.screen_rect = screen.get_rect()

		#start each new ship at the bottom center of the screen.
		#by getting the center and botton of the screen rect and
		#passing them to the ship rect, making them the same
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom


	def blitme(self):
		"""draw the ship at its current location"""
		#draw the ship to the screen by the postion specified by rect
		self.screen.blit(self.image, self.rect)