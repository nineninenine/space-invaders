import sys
import pygame

from bullet import Bullet

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

def fire_bullets(ai_settings, screen, ship, bullets):
	"""fire a bullet if we havent reached max amt of bullets on screen"""
	if len(bullets) < ai_settings.bullets_allowed:
		#Bullet is the class we wrote
		new_bullet = Bullet(ai_settings, screen, ship)
		#bullets (note thhe plural) is a sprite group object from pygame
		# .add is a function from the sprite object and it adds our bullet
		# obj to the sprite group obj. 
		bullets.add(new_bullet)


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


def update_screen(ai_settings, screen, ship, bullets):
	"""update images on the screen and flip to the new screen"""

	#redraw the screen with each pass thru the loop
	screen.fill(ai_settings.bg_color)

	#redraw all bullets behind ship and aliens
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	#draw the ship on the screen
	ship.blitme()

	#make the most recently drawn screen visible
	#erase the old screen so only the latest screen is visible
	#when we move around in the game or enemies move around
	#flip will update the screen to show new positions of elements
	#and hide old positions
	pygame.display.flip()