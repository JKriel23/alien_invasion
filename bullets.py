import pygame
from pygame.sprite import Sprite


class Bullets(Sprite):
    """a class to manage bullets fired from ship"""
    def __init__(self, settings, screen, ship):
        """initializes a bullet object and tracks the position on the screen"""
        super(Bullets, self).__init__()
        self.screen = screen

        # create bullet rectangle
        self.rect = pygame.Rect(0,0, settings.bullet_width, settings.bullet_height)
        # set bullet start point at top of ship
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # stores bullet pos as variable
        self.y = float(self.rect.y)

        # assigns color
        self.color = settings.bullet_color

        # assigns bullet speed
        self.speed = settings.bullet_speed

    def update(self):
        """move bullets up and down"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """puts image of bullet on-screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)