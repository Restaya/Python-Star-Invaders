import pygame


class Bolt(pygame.sprite.Sprite):

    def __init__(self, position, color, screen_height, speed=-10, ):
        super().__init__()

        if color == "red":
            self.image = pygame.image.load("star_invaders/assets/images/bolts/redblasterbolt.png").convert_alpha()
        if color == "green":
            self.image = pygame.image.load("star_invaders/assets/images/bolts/greenblasterbolt.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (10, 10))
        self.image = pygame.transform.rotate(self.image, 90)
        self.speed = speed
        self.screen_height = screen_height

        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.rect.y += self.speed
        self.destroy()

    def destroy(self):
        if self.rect.y <= -10 or self.rect.y > self.screen_height + 10:
            self.kill()
