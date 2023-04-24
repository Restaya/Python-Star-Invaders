import pygame

import random


class Enemy(pygame.sprite.Sprite):

    def __init__(self, position, screen_width, screen_height, hp=1):
        super().__init__()
        self.image = pygame.image.load("../assets/images/ship/tiefighter.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=position)
        self.max_x = screen_width
        self.max_y = screen_height
        self.hp = hp
        self.score_value = self.hp * 1

    # ensures enemy doesn't generate outside the window
    def check_constraint(self):
        if self.rect.left <= 10:
            self.rect.left = 10
        if self.rect.right >= self.max_x - 10:
            self.rect.right = self.max_x - 10
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.max_y - self.max_y/3:
            self.rect.bottom = self.max_y - self.max_y/3

    # makes enemies move in a random direction
    def movement(self):

        directions = ["up", "down", "left", "right"]

        direction = random.choice(directions)

        if direction == "up":
            self.rect.top -= 1
            self.check_constraint()
        if direction == "down":
            self.rect.bottom += 1
            self.check_constraint()
        if direction == "left":
            self.rect.left -= 1
            self.check_constraint()
        if direction == "right":
            self.rect.right += 1
            self.check_constraint()
