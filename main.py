# Josh Kriel

# Imports library
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from aliens import Alien
from button import Button



# define main game function
def alien_invasion():
    # starts up pygame library
    pygame.init()

    # brings in settings
    settings = Settings()

    # creates display by inputting width and height of display
    screen = pygame.display.set_mode((settings.screen_width,settings.screen_length))
    pygame.display.set_caption('Alien_Invasion')

    # add ship
    ship = Ship(screen)

    # adds aliens
    alien = Alien(settings, screen)

    # make a group to store bullets
    bullets = Group()
    aliens = Group()

    # makes play button
    play_button = Button(settings, screen, "Start")

    # Creates alien fleet
    gf.create_fleet(settings, screen, ship, aliens)

    # loop to start animation
    while True:
        # access event handler from game_functions
        gf.check_events(settings, screen, ship, bullets, play_button)

        #
        bullets.update()
        # print(len(bullets))

        # updates screen
        gf.update_screen(settings, screen, ship, bullets, aliens, play_button)


        #ends game
        gf.EndGame(settings, screen, aliens, ship)

        print(settings.score)


alien_invasion()