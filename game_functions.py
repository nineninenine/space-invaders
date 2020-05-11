import sys
import pygame

from bullet import Bullet
from alien import Alien

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""respond to key presses"""
	#if the event.key attribute is a right arrow key(pygame.K_RIGHT), move the ship right
	#by ticking moving_right flag to true. the ship moves right as long as
	#the right arrow key is held down.
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True

	#same for the left button	
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True

	#create a new bullet and add it to the bullets group if its < the allowed number of bullets
	elif event.key == pygame.K_SPACE:
		fire_bullets(ai_settings, screen, ship, bullets)

	#quit if the user presses the q key
	elif event.key == pygame.K_q:
		sys.exit()	


def check_keyup_events(event, ship):
	"""respond to key releases"""
	#when a key is released, check to see if its the right arrow key.
	#if it is, stop the ship moving right by ticking th moving_right
	#flag to false
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False

	#same for the left button	
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
	"""respond to keypresses and mouuse events"""
	#watch for keyboard and mouse events.
	#this is an event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		#if someone presses a key aka 
		#if the event.type attribute is pygame.KEYDOWN that means someone pressed a button.
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)

		#when someone releases a key aka
		#if the event.type attribute is pygame.KEYUP that means someone released a button.
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)


def fire_bullets(ai_settings, screen, ship, bullets):
	"""fire a bullet if we havent reached max amt of bullets on screen"""
	if len(bullets) < ai_settings.bullets_allowed:
		#Bullet is the class we wrote
		new_bullet = Bullet(ai_settings, screen, ship)
		#bullets (note thhe plural) is a sprite group object from pygame
		# .add is a function from the sprite object and it adds our bullet
		# obj to the sprite group obj. 
		bullets.add(new_bullet)			


def update_bullets(bullets):
	""""update positions of bullets and remove old bullets"""

	#update bullet positions
	#"bullets" is a sprite group obj. it automatically calls bullet.update() from the class we created
	#for each bullet we place in the group bullets
	bullets.update()

	#remove bullets taht have moved past the top of the screen.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	#print("bullets on screen: "+ str(len(bullets)))


def update_screen(ai_settings, screen, ship, aliens, bullets):
	"""update images on the screen and flip to the new screen"""

	#redraw the screen with each pass thru the loop
	screen.fill(ai_settings.bg_color)

	#redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	#draw the ship on the screen
	ship.blitme()

	#aliens is a group obj that holds instances of our alien class.
	#the draw function draws each element in the group at the position defined in its rect
	aliens.draw(screen)

	#make the most recently drawn screen visible
	#erase the old screen so only the latest screen is visible
	#when we move around in the game or enemies move around
	#flip will update the screen to show new positions of elements
	#and hide old positions
	pygame.display.flip()


def get_number_aliens_x(ai_settings, alien_width):
	"""figure out the number of aliens that fit in a row"""
	#we want the aliens to be spaced out one alien wide. 
	#we calculate 2x an alien for the alien and one alien-width spot to its right.
	available_space_x = ai_settings.screen_width - (2 * alien_width)
	#cast as int to get a whole number of aliens. int() truncates the decimal.
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
	"""determine the nubmer of rows of aliens fit on the screen"""
	#to figure out the amount of vertical space we want to substract 
	# the alien height from the top, the ship height from the bottom,
	# and 2x the alien height from the bottom
	available_space_y = ai_settings.screen_height - (3 * alien_height) - ship_height

	#we want one alien height space between rows, so 2x the height
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
	"""create an alien and put it in a row"""
	#we create one alien and get its rect. 
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width

	#we want a margin around the screen thats one alien width on both sides.
	#calculate the x-coord of the aliens so they line up side by side. 
	#this function is called in a loop and alien_number is the
	#iterator and is used to place the aliens out side by side.
	alien.x = alien_width + (2 * alien_width * alien_number)
	#assign the x-coord to the alien rect
	alien.rect.x = alien.x
	#similar as the x-coord, assign a y-coord
	alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
	#add the alien to the group obj
	aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
	"""create a full fleet of aliens"""
	#we create one alien to get its rect for the number_aliens_x function.
	#we don actually use this alien in the fleet
	alien = Alien(ai_settings, screen)
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

	#create first row of aliens.
	for row_number in range(number_rows):
		for alien_number in range(number_aliens_x):
			#creat an alien and put it in the row
			create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(aliens):
	"""update the position of the alien fleet"""
	#aliens (plural) is a group obj. not the alien (singular) class we made.
	#aliens contains instances of the alien obj.
	#aliens.update() calls the update() function in each instance of the alien class 
	aliens.update()
		
