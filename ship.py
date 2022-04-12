import pygame

import settings

"""Ship width = 32, height = 50"""

class Ship():
    def __init__(self,screen):
        self.screen = screen
        # load image of ship and access image data
        self.image = pygame.image.load('images/ship.png')
        self.image =  pygame.transform.scale(self.image, (32,50))
        # tells computer to interpret image as rectangle
        self.rect = self.image.get_rect()
        # tells computer to interpret screen as rectangle
        self.screen_rect = screen.get_rect()

        # speed setting
        self.speed = .33

        # set starting location of each ship
        # makes center x of ship same as center x of screen
        self.rect.centerx = self.screen_rect.centerx
        # makes a rect around the bottom of the ship
        self.rect.bottom = self.screen_rect.bottom

        # stores centerx as decimal value
        self.center = float(self.rect.centerx)

        # stores centery as decimal value
        self.centery = float(self.rect.centery)

        # create movement flags to determine if ship moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        # draws the ship on the screen
        # image.blit(image being added, location)
        self.screen.blit(self.image, self.rect)


    def update(self):
        # udates image of ship (moves left/right)
        if self.moving_right == True:
            self.center += self.speed
        if self.moving_left == True:
            self.center -= self.speed

        if self.moving_up :
            """and self.rect.top <= 25"""
            self.centery -= self.speed

        if self.moving_down :
            """and self.rect.bottom >= self.screen_rect.bottom"""
            self.centery += self.speed


        self.rect.centerx = self.center
        self.rect.centery = self.centery