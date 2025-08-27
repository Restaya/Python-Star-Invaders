import pygame

from entity.bolt import Bolt


class Player(pygame.sprite.Sprite):

    def __init__(self, position, screen_width, screen_height, speed):
        super().__init__()
        self.image = pygame.image.load("star_invaders/assets/images/ship/xwing.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(midbottom=position)
        self.speed_normal = speed
        self.max_x = screen_width
        self.max_y = screen_height
        self.ready = True
        self.bolt_time = 0
        self.bolt_cooldown = 100
        self.hp = 5

        self.bolts = pygame.sprite.Group()

    # checks for keyboard input from the player
    def get_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.ready:
            self.shoot()
            self.ready = False
            self.bolt_time = pygame.time.get_ticks()
        if keys[pygame.K_d]:
            self.rect.x += self.speed_normal
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed_normal
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed_normal
        elif keys[pygame.K_s]:
            self.rect.y += self.speed_normal

    # controls how often the player can shoot
    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.bolt_time >= self.bolt_cooldown:
                self.ready = True

    # ensures player doesn't leave the window
    def check_constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x:
            self.rect.right = self.max_x
        if self.rect.top <= self.max_y - self.max_y/3:
            self.rect.top = self.max_y - self.max_y/3
        if self.rect.bottom >= self.max_y:
            self.rect.bottom = self.max_y

    # gets player's input, checks for constraints and controls the fire rate of the player
    def update(self):
        self.get_input()
        self.check_constraint()
        self.recharge()

    def shoot(self):
        self.bolts.add(Bolt(self.rect.midleft, "red", self.max_y))
        self.bolts.add(Bolt(self.rect.midright, "red", self.max_y))

    def is_alive(self):
        return self.hp != 0
