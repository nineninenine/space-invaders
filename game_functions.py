import sys
import pygame

def check_events(ship):
	"""respond to keypresses and mouuse events"""
	#watch for keyboard and mouse events.
	#this is an event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	
		#if someone presses a key aka 
		#if the event.type attribute is pygame.KEYDOWN that means someone pressed a button.
		elif event.type == pygame.KEYDOWN:
			
			#if the event.key attribute is a right arrow key(pygame.K_RIGHT), move the ship right
			#by ticking moving_right flag to true. the ship moves right as long as
			#the right arrow key is held down.
			if event.key == pygame.K_RIGHT:
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				ship.moving_left = True
		
		#when a key is released, check to see if its the right arrow key.
		#if it is, stop the ship moving right by ticking th moving_right
		#flag to false
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			if event.key == pygame.K_LEFT:
				ship.moving_left = False




def update_screen(ai_settings, screen, ship):
	"""update images on the screen and flip to the new screen"""

	#redraw the screen with each pass thru the loop
	screen.fill(ai_settings.bg_color)
	
	#draw the ship on the screen
	ship.blitme()

	#make the most recently drawn screen visible
	#erase the old screen so only the latest screen is visible
	#when we move around in the game or enemies move around
	#flip will update the screen to show new positions of elements
	#and hide old positions
	pygame.display.flip()