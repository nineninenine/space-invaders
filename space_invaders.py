import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from alien import Alien


def run_game():
	#init the game and create a screen object
	pygame.init()

	#create a settings object
	ai_settings = Settings()

	#create the game window
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Space Invaders")

	#create a ship object. comes before while loop so
	#we dont make a new ship object each time thru the loop.
	ship = Ship(ai_settings, screen)

	#make an alien
	alien = Alien(ai_settings, screen)

	#make a group obj to store bullets in
	bullets = Group()

	# start the main loop for the game
	while True:

		#watch for keyboard and mouse events.
		#this is an event loop
		gf.check_events(ai_settings, screen, ship, bullets)

		#update the X position of the shjip
		ship.update()

		#update bullet positions and remove old bullets
		gf.update_bullets(bullets)

		#set the background color, repaint screen, draw ship on screen, bullets too
		gf.update_screen(ai_settings, screen, ship, alien, bullets)


#init and start the main loop
run_game()
