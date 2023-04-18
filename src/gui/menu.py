import pygame

import button
import text

# text color
black_text = (0, 0, 0)

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
    screen_width, screen_height = 800, 500

    # window creation and title
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Space Invaders Menu')

    # favicon
    favicon = pygame.image.load(favicon_path)
    pygame.display.set_icon(favicon)

    custom_font = pygame.font.Font('../../assets/font/Starjedi.ttf', 24)
    default_font = pygame.font.SysFont('arial', 24)

    # button images
    exit_image = pygame.image.load('../../assets/images/buttonimages/exitbutton.png').convert_alpha()
    level1_image = pygame.image.load('../../assets/images/buttonimages/level1.png').convert_alpha()
    level2_image = pygame.image.load('../../assets/images/buttonimages/level2.png').convert_alpha()
    level3_image = pygame.image.load('../../assets/images/buttonimages/level3.png').convert_alpha()

    # buttons
    level1_button = button.Button(100, 200, level1_image, 0.4)
    level2_button = button.Button(300, 200, level2_image, 0.4)
    level3_button = button.Button(500, 200, level3_image, 0.4)

    exit_button = button.Button(300, 325, exit_image, 0.4)

    # game loop
    while True:

        # background color of menu
        window.fill((220, 141, 30))

        # text draw on screen
        text.draw_text(window, 'welcome to space invaders!', custom_font, black_text, 175, screen_height / 5)

        # draw button on screen and check for interaction
        if level1_button.draw_button(window):
            start_level1()
            pygame.quit()
            return

        if level2_button.draw_button(window):
            start_level2()
            pygame.quit()
            return

        if level3_button.draw_button(window):
            start_level3()
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


def start_level1():
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



def start_level2():
    pygame.init()

    # clock
    clock = pygame.time.Clock()

    # window creation and title
    window = pygame.display.set_mode((level_window_width, level_window_height))
    pygame.display.set_caption('Space Invaders Level 2')

    # favicon
    favicon = pygame.image.load(favicon_path)
    pygame.display.set_icon(favicon)

    # game loop
    while True:

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

def start_level3():
    pygame.init()

    # clock
    clock = pygame.time.Clock()

    # window creation and title
    window = pygame.display.set_mode((level_window_width, level_window_height))
    pygame.display.set_caption('Space Invaders Level 3')

    # favicon
    favicon = pygame.image.load(favicon_path)
    pygame.display.set_icon(favicon)

    # game loop
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            # key press events
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        pygame.display.update()
        clock.tick(60)



if __name__ == "__main__":
    start_menu()
