

class Settings():
	"""class to store settings in space invaders"""

	def __init__(self):
		"""init settins in space invaders"""
		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#ship settings
		self.ship_speed_factor = 1.5

		#bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		#limits the nubmer of bullets allowed onscreen to encourage accurate shooting
		self.bullets_allowed = 3

		#alien settings
		self.alien_speed_factor = 1
		#how fast the fleet drops
		self.fleet_drop_speed = 10
		#fleet direction of 1 == right, -1 == left
		self.fleet_direction = 1