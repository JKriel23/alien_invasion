class Settings():
    # class to store all settings for alien invasion

    def __init__(self):
        # screen settings
        self.bg_color = (0,0,0)
        self.screen_width = 1000
        self.screen_length = 625

        # bullet settings
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 0, 0)
        self.bullet_limit = 5

        # player settings
        self.lives = 3
        self.score = 0

        self.game_active = False
