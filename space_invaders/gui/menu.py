import pygame

import button
import text

# text color
black_color = (0, 0, 0)
gray_color = (40,43,48)

#level window parameters
level_window_height = 600
level_window_width = 800

#favicon path
favicon_path = '../../assets/images/favicon.png'


def start_menu():
    pygame.init()

    #clock
    clock = pygame.time.Clock()

    # window size
    screen_width, screen_height = 700, 500

    # window creation and title
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space Invaders Menu')

    # favicon
    favicon = pygame.image.load(favicon_path)
    pygame.display.set_icon(favicon)

    custom_font = pygame.font.Font('../../assets/font/Starjedi.ttf', 24)

    # button images
    start_image = pygame.image.load('../../assets/images/buttonimages/start.png')
    exit_image = pygame.image.load('../../assets/images/buttonimages/exitbutton.png').convert_alpha()

    # buttons
    start_button = button.Button(265,200,start_image,0.4)
    exit_button = button.Button(265, 325, exit_image, 0.4)

    # game loop
    while True:

        # background color of menu
        window.fill((220, 141, 30))

        # text draw on screen
        text.draw_text(window, 'welcome to space invaders!', custom_font, black_color, 140, screen_height / 5)

        # draw button on screen and check for interaction
        if start_button.draw_button(window):
            start_game()
            pygame.quit()
            return

        if exit_button.draw_button(window):
            pygame.quit()
            return

        # eventhandler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # key press events
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        pygame.display.update()
        clock.tick(60)


def start_game():
    pygame.init()

    # clock
    clock = pygame.time.Clock()

    # window creation and title
    window = pygame.display.set_mode((level_window_width, level_window_height))
    pygame.display.set_caption('Space Invaders Level 1')

    background = pygame.image.load("../../assets/images/background.png")
    background = pygame.transform.scale(background,(level_window_width,level_window_height))

    player_image = pygame.image.load("../../assets/images/ship/xwing.png")
    player_image = pygame.transform.scale(player_image,(50,50))

    enemy_image = pygame.image.load("../../assets/images/ship/tiefighter.png")
    enemy_image = pygame.transform.scale(enemy_image,(50,50))


    # favicon
    favicon = pygame.image.load(favicon_path)
    pygame.display.set_icon(favicon)

    # game loop
    while True:

        #window.fill(gray_color)
        window.blit(background,(0,0))

        window.blit(enemy_image,(350,0))
        window.blit(player_image,(350,level_window_height-player_image.get_height()))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # key press events
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        pygame.display.update()
        clock.tick(60)


if __name__ == "__menu__":
    start_menu()
