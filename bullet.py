import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #Class of ammunition from the ship

    def __init__(self, ai_settings, screen, ship):
        #Creating a bullet object at the ship's  position
        super(Bullet, self).__init__()
        self.screen = screen

        # Creating bullet rect at (0, 0), then setting the correct position.
        self.rect = pygame.Rect(
            0, 0, ai_settings.bullet_width, ai_settings.bullet_height
        )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Store a decimal value for the bullet's position.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #Giving the bullet motion up the screen
        self.y -= self.speed_factor
        # Update the rect position. Lots of help here
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)