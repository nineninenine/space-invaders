class GameStats():
    """track stats for space invaders"""
    def __init__(self, ai_settings):
        """init stats"""
        self.ai_settings = ai_settings
        self.reset_stats()

        #start game in inactive state
        self.game_active = False

    def reset_stats(self):
        """init stats that can change thru out the game"""
        self.ships_left = self.ai_settings.ship_limit