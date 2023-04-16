import pygame

import button
import text

pygame.init()

#window size
SCREEN_WIDTH,SCREEN_HEIGHT = 800,500

#window creation and title
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('Space Invaders Menu')

#favicon
FAVICON = pygame.image.load('../../assets/images/favicon.jpg')
pygame.display.set_icon(FAVICON)

#fonts
custom_font = pygame.font.Font('../../assets/font/Starjedi.ttf', 24)
default_font = pygame.font.SysFont('arial',24)

#text color
TEXT_BLACK_COLOR = (0,0,0)

#button images

exit_image = pygame.image.load('../../assets/images/buttonimages/exitbutton.jpg').convert_alpha()

#buttons
#TODO correct params
level1_button = button.Button(0,0,exit_image,0.4)
level2_button = button.Button(200,200,exit_image,0.4)
level3_button = button.Button(500,500,exit_image,0.4)

exit_button = button.Button(SCREEN_WIDTH/4,SCREEN_HEIGHT/8,exit_image,0.4)

#draws text on screen
def draw_text(text,font,text_color,x,y):
    image = font.render(text,True,text_color)
    window.blit(image,(x, y))


#game loop
run = True
while run:

    #background color of menu
    window.fill((220,141,30))

    #text draw on screen
    text.draw_text(window,'Welcome to Space Invaders!',custom_font,TEXT_BLACK_COLOR,SCREEN_WIDTH/4,SCREEN_HEIGHT/5)

    #draw button on screen and check for interaction
    if level1_button.draw_button(window):
        print("level 1 function needs to be written")
        #TODO level 1 function

    if level2_button.draw_button(window):
        print("level 2 function needs to be written")
        #TODO level 2 function
    if level3_button.draw_button(window):
        print("level 3 function needs to be written")
        #TODO level 3 function
    if exit_button.draw_button(window):
        run = False

    #eventhandler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #key press events
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                run = False

    pygame.display.update()


pygame.quit()



