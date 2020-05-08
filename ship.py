import pygame


class Ship():
	"""init the ship and set its starting position"""
	def __init__(self, ai_settings, screen):

		self.screen = screen

		#to make the settings object accessible here
		self.ai_settings = ai_settings
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

		#store a decimal value for the ships center
		self.center = float(self.rect.centerx)


		#movement flags
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""update the ships position based on the left or right movement flag"""
		#update the center rect attribute to track the X position of the ship
		#use 2 if statement instead of elif so that both left and right flags
		#can be turned on when the player holds both buttons. this causes the
		#ship not to move when both left and right and held down together
		
		#dont move left or right past the end of the screen
		if ( self.moving_right == True ) and ( self.rect.right < self.screen_rect.right ):
			#update the center attribute to accurately store the decimal
			self.center += self.ai_settings.ship_speed_factor
		if ( self.moving_left == True ) and ( self.rect.left > self.screen_rect.left ):
			#update the center attribute to accurately store the decimal
			self.center -= self.ai_settings.ship_speed_factor

		#update the centerx of the rect with the decimal, which
		#will only take the int portion and drop the fraction
		self.rect.centerx = self.center

	def blitme(self):
		"""draw the ship at its current location"""
		#draw the ship to the screen by the postion specified by rect
		self.screen.blit(self.image, self.rect)	