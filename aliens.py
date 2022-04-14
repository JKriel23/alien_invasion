import pygame
# from settings import Settings
from pygame.sprite import Sprite

class Alien(Sprite):
    """class which represents each alien"""

    def __init__(self, settings, screen):
        super(Alien, self).__init__()

        # defines attributes
        self.screen = screen
        self.settings = settings

        # load alien ship image as scaled version & get rectangle properties
        self.image = pygame.image.load('images/ufo.png')
        self.image = pygame.transform.scale(self.image, (50, 26))
        self.rect = self.image.get_rect()

        # set starting location
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # allows for x to be decimal
        self.x = float(self.rect.x)

        # spacing for aliens
        self.available_space_x = self.settings.screen_width - (2 * self.rect.width)
        self.number_of_aliens = int(self.available_space_x / (2 * self.rect.width))

        self.speed = .5
        self.direction = 1
        self.move = True

    def blitme(self):
        """ draws the alien on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self, settings):
        """moves alien"""
        if self.check_screen():
            self.direction = self.direction * -1
            self.rect.y += 25

        self.x += self.speed * self.direction
        self.rect.x = self.x




    def check_screen(self):
        """returns true if alien hits wall"""
        screen_rect = self.screen.get_rect()
        if self.rect.right > screen_rect.right:
            return True
        elif self.rect.left < 0:
            return True