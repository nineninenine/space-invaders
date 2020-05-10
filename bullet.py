import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""a clss to manage the bullets fired from the shjip"""
	def __init__(self, ai_settings, screen, ship):
		"""make a bullet obj at the ships current position"""
		super().__init__()
		self.screen = screen

		#init bullet rect at (0, 0) and set the correct position.
		#we're drawing it from scratch. we init the rects top left corner to 0,0
		#after init, we update the bullets centerx to be the same as the ships centerx,
		#and the bullets top to the sjhips top to make it look like the bullet
		#emerges from the ship
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		#store the bullets position as a decimal value
		#this is the y value as it moves up the screen
		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		"""move the bullet up the screen"""
		#this function is called automatically by the pygame.sprite group object

		#update the y value of the bullet
		#the bullet travels up so we subtract y (pygame inits the upper left corner
		#of the window as 0,0 and the bottom right as positive integers for maxX, maxY. 
		# maxX and maxY are whtever size of the screen you config'd) so upward
		#movement means we subtract. this will be in the main loop so it will 
		#run a shitload of tiems and move the bullet up. no x coord is needed
		#cuz the bullet travels in a straight line
		self.y -= self.speed_factor

		#update the rect position
		self.rect.y = self.y

	def draw_bullet(self):
		"""draw bullet on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)