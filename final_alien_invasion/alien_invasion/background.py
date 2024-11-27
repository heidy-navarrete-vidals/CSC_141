import pygame

class Background:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the background image and get its rect
        self.image = pygame.image.load('images/bg.jpg')

        # Use this instead of screen
        self.rect = self.image.get_rect()



    def update(self):
        pass

    def blitme(self):
        self.screen.blit(self.image, self.rect)