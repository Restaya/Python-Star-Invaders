import pygame
from space_invaders.entity.bolt import Bolt

class Enemy(pygame.sprite.Sprite):

    def __init__(self,position,screen_width,screen_height,hp = 1):
        super().__init__()
        self.image = pygame.image.load("../../assets/images/ship/tiefighter.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect(center = position)
        self.max_x = screen_width
        self.max_y = screen_height
        self.hp = hp


    def destroy(self):
        if self.hp == 0:
            self.kill()

    #ensures enemy doesn't generate outside of the window
    def check_constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x:
            self.rect.right = self.max_x
        if self.rect.top <= self.max_y - self.max_y/3:
            self.rect.top = self.max_y - self.max_y/3
        if self.rect.bottom >= self.max_y:
            self.rect.bottom = self.max_y

