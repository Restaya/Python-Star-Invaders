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
FAVICON = pygame.image.load('../../assets/images/favicon.png')
pygame.display.set_icon(FAVICON)

#fonts
custom_font = pygame.font.Font('../../assets/font/Starjedi.ttf', 24)
default_font = pygame.font.SysFont('arial',24)

#text color
TEXT_BLACK_COLOR = (0,0,0)

#button images
exit_image = pygame.image.load('../../assets/images/buttonimages/exitbutton.png').convert_alpha()
level1_image = pygame.image.load('../../assets/images/buttonimages/level1.png').convert_alpha()
level2_image = pygame.image.load('../../assets/images/buttonimages/level2.png').convert_alpha()
level3_image = pygame.image.load('../../assets/images/buttonimages/level3.png').convert_alpha()

#buttons
level1_button = button.Button(100,200,level1_image,0.4)
level2_button = button.Button(300,200,level2_image,0.4)
level3_button = button.Button(500,200,level3_image,0.4)

exit_button = button.Button(300,325,exit_image,0.4)

#game loop
run = True
while run:

    #background color of menu
    window.fill((220,141,30))

    #text draw on screen
    text.draw_text(window,'welcome to space invaders!',custom_font,TEXT_BLACK_COLOR,175,SCREEN_HEIGHT/5)

    #draw button on screen and check for interaction
    if level1_button.draw_button(window):
        print("level 1 function needs to be written")

    if level2_button.draw_button(window):
        print("level 2 function needs to be written")

    if level3_button.draw_button(window):
        print("level 3 function needs to be written")

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



