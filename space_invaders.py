import pygame
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf
from button import Button




def run_game():
	#init the game and create a screen object
	pygame.init()

	#create a settings object
	ai_settings = Settings()

	#create the game window
	screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Space Invaders")
	#make play button
	play_button = Button(ai_settings, screen, "Play")
	#create gamestats instance to store game stats
	stats = GameStats(ai_settings)


	#create a ship object. comes before while loop so
	#we dont make a new ship object each time thru the loop.
	ship = Ship(ai_settings, screen)

	#make a group obj to store bullets in
	bullets = Group()

	#make a group obj to store aliens
	aliens = Group()

	#create a fleet of aliens
	gf.create_fleet(ai_settings, screen, ship, aliens)

	# start the main loop for the game
	while True:

		#watch for keyboard and mouse events.
		#this is an event loop
		gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)

		if stats.game_active:
			#update the X position of the shjip
			ship.update()

			#update bullet positions and remove old bullets
			gf.update_bullets(ai_settings, screen, ship, aliens, bullets)

			#update the position of the aliens
			gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)

		#set the background color, repaint screen, draw ship on screen, bullets too
		gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)


#init and start the main loop
run_game()
