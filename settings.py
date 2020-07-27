

class Settings():
	"""class to store settings in space invaders"""

	def __init__(self):
		"""init static settings in space invaders"""
		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		#ship settings
		#number of lives
		self.ship_limit = 3

		#bullet settings
		self.bullet_width = 300
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		#limits the nubmer of bullets allowed onscreen to encourage accurate shooting
		self.bullets_allowed = 3

		#alien settings
		#how fast the fleet drops
		self.fleet_drop_speed = 100

		#how quickly the game speeds up
		self.speedup_scale = 1.1

		self.initialize_dynamic_settings()


	def initialize_dynamic_settings(self):
		"""init settings that change during the game"""
		#ship settings
		self.ship_speed_factor = 1.5
		#bullet settings
		self.bullet_speed_factor = 4

		#alien settings
		self.alien_speed_factor = 1

		#fleet direction of 1 == right, -1 == left
		self.fleet_direction = 1


	def increase_speed(self):
	"""increase speed settings"""
	self.ship_speed_factor *= self.speedup_scale
	self.bullet_speed_factor *= self.speedup_scale
	self.alien_speed_factor *= self.speedup_scale

