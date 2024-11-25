import pygame

class Background:

    def __init__(self, ai_game):
        self.screen = ai_game.screen

        self.screen.rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings

        self.image = pygame.image.load('images/bg.jpg')
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def blitme(self):
        self.screen.blit(self.image, self.rect)