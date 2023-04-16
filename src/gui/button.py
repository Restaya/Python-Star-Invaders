import pygame


class Button:

    def __init__(self,x,y,image,scale=1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image,(int(width * scale),int(height * scale) ))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    #Draws button on screen
    def draw_button(self,surface):
        action = False

        #get mouse position
        mos_pos = pygame.mouse.get_pos()

        #check if mouse on button and conditions
        if self.rect.collidepoint(mos_pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

                print("TODO\n")
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #draw button on screen
        surface.blit(self.image,(self.rect.x,self.rect.y))

        return action

