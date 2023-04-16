import pygame

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

#draws text on screen
def draw_text(text,font,text_color,x,y):
    image = font.render(text,True,text_color)
    window.blit(image,(x, y))


#game loop
run = True
while run:

    #temp
    window.fill((220,141,30))

    draw_text('Welcome to Space Invaders!',custom_font,TEXT_BLACK_COLOR,SCREEN_WIDTH/4,SCREEN_HEIGHT/5)

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



