import pygame
import random

import space_invaders.gui.button as button
import space_invaders.gui.text as text
from space_invaders.entity.player import Player
from space_invaders.entity.enemy import Enemy

# text color
black_color = (0, 0, 0)
gray_color = (40,43,48)

#game window parameters
game_window_height = 600
game_window_width = 800

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
    favicon = pygame.image.load('../../assets/images/favicon.png')
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

#generates enemies on screen
def generate_enemy(enemies,min,max):

    number_of_enemies = random.randint(min,max)

    while len(enemies) != number_of_enemies:

        enemy_pos_x = random.randint(50,game_window_width-50)
        enemy_pos_y = random.randint(50,int(game_window_height - game_window_height/3)-50)

        enemy = Enemy((enemy_pos_x, enemy_pos_y), game_window_width, game_window_height)
        enemies.add(enemy)

        if len(enemies) > 0:
            for current_enemy in enemies:
                if current_enemy == enemy:
                    break
                if pygame.sprite.collide_rect(enemy,current_enemy):
                    enemy.kill()
                    break

        print(len(enemies))



def start_game():
    pygame.init()

    # makes sure it runs on a fixed fps
    clock = pygame.time.Clock()

    # window creation and title
    window = pygame.display.set_mode((game_window_width, game_window_height))
    pygame.display.set_caption('Space Invaders')

    #loads background
    background = pygame.image.load("../../assets/images/background.png")
    background = pygame.transform.scale(background,(game_window_width,game_window_height))

    #player initialized
    player_sprite = Player((game_window_width/2, game_window_height),game_window_width,game_window_height,20,10)
    player = pygame.sprite.GroupSingle(player_sprite)

    #enemies initialized
    enemies = pygame.sprite.Group()
    generate_enemy(enemies,5,10)

    # favicon
    favicon = pygame.image.load('../../assets/images/favicon.png')
    pygame.display.set_icon(favicon)

    # game loop
    while True:

        #window.fill(gray_color)
        window.blit(background,(0,0))

        #draws player on screen
        player.draw(window)

        #draws all the bolts on screen
        player.sprite.bolts.draw(window)

        #draws enemies on the screen
        enemies.draw(window)

        #generates the inital enemies
        generate_enemy(enemies, 5, 10)

        #updates the bolts on screen
        player.sprite.bolts.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            # key press events
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_f:
                    enemies.empty()
                    generate_enemy(enemies,5,10)

                #checks for keyboard input from the player
                player.update()


                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return

        pygame.display.update()
        clock.tick(60)


