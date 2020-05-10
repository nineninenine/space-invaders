import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a clss to represent a single alien on the screen"""

    def __init__(self, ai_settings, screen):
        """init the alien and its starting position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the alien and get its rect
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        #start every alien in the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """draw the aliens current position"""
        self.screen.blit(self.image, self.rect)