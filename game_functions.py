import sys
import pygame
import sys

from time import sleep
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


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets):
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

		elif event.type == pygame.MOUSEBUTTONDOWN:
			#get the x,y of hte mouse postion at click
			mouse_x, mouse_y = pygame.mouse.get_pos()
			#stats argument is passed so method can access game_active attrb
			check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
	"""start a new game when the player clicks the play button"""
	#rect collidepoint method used check if mouseclick overlaps with button rect
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)

	if button_clicked and not stats.game_active:
		#hide teh mouse cursor dude
		pygame.mouse.set_visible(False)
		#reset stats and start game
		stats.reset_stats()
		stats.game_active = True

		#empty aliens and bullets group obj
		aliens.empty
		bullets.empty

		#create fresh alien fleet and center ship
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()


def fire_bullets(ai_settings, screen, ship, bullets):
	"""fire a bullet if we havent reached max amt of bullets on screen"""
	if len(bullets) < ai_settings.bullets_allowed:
		#Bullet is the class we wrote
		new_bullet = Bullet(ai_settings, screen, ship)
		#bullets (note thhe plural) is a sprite group object from pygame
		# .add is a function from the sprite object and it adds our bullet
		# obj to the sprite group obj. 
		bullets.add(new_bullet)			


def update_bullets(ai_settings, screen, ship, aliens, bullets):
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

	check_bullet_alien_collisions(ai_settings, screen, ship, aliens,bullets)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
	"""remove any bullets and aliens that have collided"""
	#check for any bullets that have hit aliens
	#if so, remove the bullet and alien.
	#the 2 True params remove the bullets and aliens
	# change the first to False so keep the bullet going 
	collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

	#if each alien in the aliens (note plural) group are shotdown, make new alien fleet
	if len(aliens) == 0:
		#remove all bullets and make a new fleet
		bullets.empty()
		create_fleet(ai_settings, screen, ship, aliens)



def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
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

	#draw play button if the game is inactive
	if not stats.game_active:
		play_button.draw_button()

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


#def update_aliens(aliens):
#	"""update the position of the alien fleet"""
#	#aliens (plural) is a group obj. not the alien (singular) class we made.
#	#aliens contains instances of the alien obj.
#	#aliens.update() calls the update() function in each instance of the alien class 
#	aliens.update()
		
def check_fleet_edges(ai_settings, aliens):
	"""respond if any aliens reach the edge of the screen"""
	#move the aliens down one row and start moving the other way
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings, aliens)
			break

def change_fleet_direction(ai_settings, aliens):
	"""drop an entire fleet and change the fleets direction."""
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
		#change the fleet direction by flpping from positive to neg or vice versa
	
	ai_settings.fleet_direction *= -1



def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
	"""check if the fleet is at the edge of the screen and then update the postion of all aliens in the fleet"""
	
	check_fleet_edges(ai_settings, aliens)
	#aliens (plural) is a group obj. not the alien (singular) class we made.
	#aliens contains instances of the alien obj.
	#aliens.update() calls the update() function in each instance of the alien class 
	aliens.update()

	#check for alien-ship collisions
	#takes 2 arguements, a sprite and a group
	if pygame.sprite.spritecollideany(ship, aliens):
		ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
		#print("Ship was hit!!")

	#look for aliens getting to the bottom of the screen
	check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
	




def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
	"""respond when the ship is hit by an alien"""
	#one less ship
	if stats.ships_left > 0:
		stats.ships_left -= 1

		#empty out current aliens and bullets group obj (note plurals)
		aliens.empty()
		bullets.empty()

		#create new fleet of aliens and new ship centered on the screen
		create_fleet(ai_settings, screen, ship, aliens)
		ship.center_ship()

		#pause so players have a moment before game restarts
		sleep(0.5)
	else:
		stats.game_active = False
		#bring teh mouse back when player runs out of lives and game is over
		pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
	"""check to see if any aliens ahve reached teh bottom of the screen"""
	screen_rect = screen.get_rect()
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen_rect.bottom:
			#treat this alient the same as if it had hit a ship
			#ie reset fleet, bullets, recenter ship
			ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
			break




