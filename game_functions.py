import time

import pygame
import sys
from bullets import Bullets
from aliens import Alien
from button import Button



# checks for key press (L/R) (UP/DOWN) (SHOOT)
def Key_down(event, settings, screen, ship, bullets):
    """problem on line 9"""
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True
        if event.key == pygame.K_LEFT :
            ship.moving_left = True
        if event.key == pygame.K_UP :
            ship.moving_up = True
        if event.key == pygame.K_DOWN :
            ship.moving_down = True
        if event.key == pygame.K_SPACE:
            if len(bullets) < settings.bullet_limit:
                new_bullet = Bullets(settings, screen, ship)
                bullets.add(new_bullet)

# checks for key release (L/R)
def Key_up(event, ship):
     if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False
        if event.key == pygame.K_UP:
            ship.moving_up = False
        if event.key == pygame.K_DOWN:
            ship.moving_down = False

def check_events(settings, screen, ship, bullets, play_button):
    # checks for key/mouse events and responds
    # loop that checks for keypress
    for event in pygame.event.get():
        # if escape key press end game
        if event.type == pygame.QUIT:
            # closes game
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                settings.game_active = True

        Key_down(event, settings, screen, ship, bullets)
        Key_up(event, ship)

def walls(settings, ship):
    if ship.rect.right >= settings.screen_width:
        ship.moving_right = False
    if ship.rect.left <= 0:
        ship.moving_left = False

    if ship.rect.top <= 0:
        ship.moving_up = False
    if ship.rect.bottom >= ship.screen_rect.bottom:
        ship.moving_down = False

def check_collision(bullets, settings, aliens):
    if pygame.sprite.groupcollide(bullets, aliens, True, True):
        settings.score +=1


def player_death(settings, screen, aliens, ship):
    if pygame.sprite.spritecollideany(ship, aliens):
        aliens.empty()
        settings.lives -= 1
        reset_ship(ship, settings)

def new_wave(settings, screen, ship, aliens):
    if len(aliens) == 0 and settings.lives >= 1:
        create_fleet(settings, screen, ship, aliens)

def EndGame(settings, screen, aliens, ship):
    if pygame.sprite.spritecollideany(ship, aliens):

        reset_ship(ship)

        if settings.lives >= 1:
            aliens.empty()
            settings.lives -= 1



    if len(aliens) == 0:
        create_fleet(settings, screen, ship, aliens)

def reset_ship(ship, settings):
    ship.center = settings.screen_width/2
    ship.centery = settings.screen_length - 50


def GameOver(settings, screen):
        if settings.lives < 1:
            font = pygame.font.SysFont("Times New Roman", 50, True, False)
            surface = font.render("GAME OVER" + "   " + "SCORE:" + str(settings.score), True, (255, 0, 255))
            screen.blit(surface, (settings.screen_width/4, settings.screen_length/2))




def get_number_of_aliens(settings, alien_width):
    available_space_x = settings.screen_width - (2 * alien_width)
    number_of_aliens = int(available_space_x / (2 * alien_width))
    return number_of_aliens

def display_score(screen, settings):
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Score: " + str(settings.score), True, (255, 255, 255))
    screen.blit(surface, (430, 20))

def limit_bullets(bullets):
    for bullet in bullets:
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    # if len(bullets) > 1:
    #    pygame.sprite.Group.empty(bullets)

def update_screen(settings, screen, ship, bullets, aliens, play_button):
    # draws background
    screen.fill(settings.bg_color)

    # updates button
    if not settings.game_active:
        play_button.draw_button()

    elif settings.game_active:

        # draw fleet of aliens
        aliens.draw(screen)
        aliens.update(screen)

        # draws ship
        ship.blitme()

        # blows up aliens
        check_collision(bullets, settings, aliens)

        # limits number of bullets
        limit_bullets(bullets)

        # updates ship position
        player_death(settings, screen, aliens, ship)
        ship.update()

        # draws bullets
        for bullet in bullets.sprites():
            bullet.draw_bullet()

        # Displays score
        display_score(screen, settings)

        # sets boundaries
        walls(settings, ship)
        # atmosphere(settings, ship)


        new_wave(settings, screen, ship, aliens)

        GameOver(settings,screen)

    # 'flips through flipbook'/updates display
    pygame.display.flip()

def create_fleet(settings, screen, ship, aliens):
    # creates alien fleet
    alien = Alien(settings, screen)
    number_of_aliens = get_number_of_aliens(settings, alien.rect.width)
    number_of_rows = int(get_number_rows(settings, alien.rect.height, ship.rect.height) / 1.25)

    for row_number in range(number_of_rows):
            for alien_number in range(number_of_aliens):
                create_alien(settings, screen, aliens, alien_number, row_number)



def get_number_rows(settings, alien_height, ship_height):
    available_space_y = (settings.screen_length - 3 *alien_height - ship_height)
    number_of_rows = int(available_space_y/(2 * alien_height))
    return number_of_rows

def create_alien(settings, screen, aliens, alien_number, row_number):
    alien = Alien(settings,screen)
    alien_width = alien.rect.width
    alien.x = 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 *alien.rect.height * row_number
    aliens.add(alien)