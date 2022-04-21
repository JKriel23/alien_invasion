import pygame
import sys
from bullets import Bullets
from aliens import Alien


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

def check_events(settings, screen, ship, bullets):
    # checks for key/mouse events and responds
    # loop that checks for keypress
    for event in pygame.event.get():
        # if escape key press end game
        if event.type == pygame.QUIT:
            # closes game
            sys.exit()

        Key_down(event, settings, screen, ship, bullets)
        Key_up(event, ship)

def walls(settings, ship):
    if ship.center >= settings.screen_width - 16:
        ship.moving_right = False
    if ship.center <= 16:
        ship.moving_left = False

def atmosphere(settings, ship):
    if ship.centery <= 25:
        ship.moving_up = False
    if ship.centery >= ship.screen_rect.bottom -25:
        ship.moving_down = False

def check_collision(bullets, settings, aliens):
    alien_collides = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if alien_collides:
        settings.score +=1



def EndGame(aliens):
    if EndGame:
        pygame.sprite.Sprite.kill(aliens)

def get_number_of_aliens(settings, alien_width):
    available_space_x = settings.screen_width - (2 * alien_width)
    number_of_aliens = int(available_space_x / (2 * alien_width))
    return number_of_aliens

def display_score(screen, settings):
    font = pygame.font.SysFont("Times New Roman", 30, True, False)
    surface = font.render("Score: " + str(abs(63-settings.score)), True, (255, 255, 255))
    screen.blit(surface, (430, 20))

def limit_bullets(bullets):
    for bullet in bullets:
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)
    # if len(bullets) > 1:
    #    pygame.sprite.Group.empty(bullets)

def update_screen(settings, screen, ship, bullets, aliens):
    # draws background
    screen.fill(settings.bg_color)

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
    ship.update()
    # draws bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Displays score
    display_score(screen, settings)

    # sets boundaries
    walls(settings, ship)
    atmosphere(settings, ship)

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