import sys
import pygame

from settings import Settings


def run_game():
	#init the game and create a screen object
	pygame.init()

	#create a settings object
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Space Invaders")




	# start the main loop for the game
	while True:

		#watch for keyboard and mouse events.
		#this is an event loop
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()


		#redraw screen each pass thru the loop
		screen.fill(ai_settings.bg_color)

		#make the most recently drawn screen visible
		#erase the old screen so only the latest screen is visible
		#when we move around in the game or enemies move around
		#flip will update the screen to show new positions of elements
		#and hide old positions
		pygame.display.flip()

	#init and start the main loop
run_game()
