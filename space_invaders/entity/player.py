import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self,pos,screen_width,screen_height,speed,reverse_speed):
        super().__init__()
        self.image = pygame.image.load("../../assets/images/ship/xwing.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(midbottom = pos)
        self.speed_normal = speed
        self.speed_reverse = reverse_speed
        self.max_x = screen_width
        self.max_y = screen_height


    def get_input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d]:
            self.rect.x += self.speed_normal
        elif keys[pygame.K_a]:
            self.rect.x -= self.speed_normal
        elif keys[pygame.K_w]:
            self.rect.y -= self.speed_normal
        elif keys[pygame.K_s]:
            self.rect.y += self.speed_reverse

    #ensures player doesn't leave the window
    def check_constraint(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.right >= self.max_x:
            self.rect.right = self.max_x
        if self.rect.top <= self.max_y - self.max_y/3:
            self.rect.top = self.max_y - self.max_y/3
        if self.rect.bottom >= self.max_y:
            self.rect.bottom = self.max_y


    def update(self):
        self.get_input()
        self.check_constraint()

