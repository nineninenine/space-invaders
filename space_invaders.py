import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	#init the game and create a screen object
	pygame.init()

	#create a settings object
	ai_settings = Settings()

	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Space Invaders")

	#create a ship object. comes before while loop so
	#we dont make a new ship object each time thru the loop.
	ship = Ship(screen)

	# start the main loop for the game
	while True:

		#watch for keyboard and mouse events.
		#this is an event loop
		gf.check_events(ship)

		#check to see if the user is moving the ship
		ship.update()
		
		#set the background color, repaint screen, draw ship on screen
		gf.update_screen(ai_settings, screen, ship)


	#init and start the main loop
run_game()
