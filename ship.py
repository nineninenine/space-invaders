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
		#passing them to the ships center rect, making them the same
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom

		#movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""update the ships position based on the left or right movement flag"""
		#update the center rect attribute to track the X position of the ship
		#use 2 if statement instead of elif so that both left and right flags
		#can be turned on when the player holds both buttons. this causes the
		#ship not to move when both left and right and held down together
		if self.moving_right == True:
			self.rect.centerx += 1
		if self.moving_left == True:
			self.rect.centerx -= 1


	def blitme(self):
		"""draw the ship at its current location"""
		#draw the ship to the screen by the postion specified by rect
		self.screen.blit(self.image, self.rect)	