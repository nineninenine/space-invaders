class GameStats():
    """track stats for space invaders"""
    def __init__(self, ai_settings):
        """init stats"""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """init stats that can change thru out the game"""
        self.ships_left = self.ai_settings.ship_limit