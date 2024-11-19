import pygame
 
class Link:
    """A class to manage the image."""
 
    def __init__(self, l_game):
        """Initialize the image and set its starting position."""
        self.screen = l_game.screen
        self.screen_rect = l_game.screen.get_rect()

        # Load the link image and get its rect.
    
        self.image = pygame.image.load('images/link.bmp')
        self.rect = self.image.get_rect()

        # Start each image at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw image at its current location."""
        self.screen.blit(self.image, self.rect)