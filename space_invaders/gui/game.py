import pygame
import random

import space_invaders.gui.button as button
import space_invaders.gui.text as text
from space_invaders.entity.player import Player
from space_invaders.entity.enemy import Enemy

# text color
black_color = (0, 0, 0)
gray_color = (40,43,48)


class Game:

    def __init__(self,game_window_width,game_window_height):
        self.game_window_width = game_window_width
        self.game_window_height = game_window_height
        self.title = "Space Invaders"

        pygame.init()
        self.font = pygame.font.Font('../../assets/font/Starjedi.ttf', 24)
        self.favicon = pygame.image.load('../../assets/images/favicon.png')
        self.score = 0


    def start_menu(self):
        pygame.init()

        # clock
        clock = pygame.time.Clock()

        # window size
        screen_width, screen_height = 700, 500

        # window creation and title
        window = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(self.title + " Menu")

        # favicon
        pygame.display.set_icon(self.favicon)

        # button images
        start_image = pygame.image.load('../../assets/images/buttonimages/start.png')
        exit_image = pygame.image.load('../../assets/images/buttonimages/exitbutton.png').convert_alpha()

        # buttons
        start_button = button.Button(265, 200, start_image, 0.4)
        exit_button = button.Button(265, 325, exit_image, 0.4)

        # game loop
        while True:

            # background color of menu
            window.fill((220, 141, 30))

            # text draw on screen
            text.draw_text(window, 'welcome to space invaders!', self.font, black_color, 140, screen_height / 5)

            # draw button on screen and check for interaction
            if start_button.draw_button(window):
                self.start_game()
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

    # generates enemies on screen
    def generate_enemy(self,enemies, min, max):

        number_of_enemies = random.randint(min, max)

        while len(enemies) != number_of_enemies:

            enemy_pos_x = random.randint(25, self.game_window_width - 25)
            enemy_pos_y = random.randint(25, int(self.game_window_height - self.game_window_height / 2) - 25)

            enemy = Enemy((enemy_pos_x, enemy_pos_y), self.game_window_width, self.game_window_height)
            enemies.add(enemy)

            if len(enemies) > 1:
                for current_enemy in enemies:
                    if current_enemy == enemy:
                        break
                    if pygame.sprite.collide_rect(enemy, current_enemy):
                        enemy.kill()
                        break

        print("Enemies initialized successfuly\n" + "Generated " + str(number_of_enemies) + " enemies")

    def start_game(self):
        pygame.init()

        # makes sure it runs on a fixed fps
        clock = pygame.time.Clock()

        # window creation and title
        window = pygame.display.set_mode((self.game_window_width, self.game_window_height))
        pygame.display.set_caption(self.title)

        # loads background
        background = pygame.image.load("../../assets/images/background.png")
        background = pygame.transform.scale(background, (self.game_window_width, self.game_window_height))

        # player initialized
        player_sprite = Player((self.game_window_width / 2, self.game_window_height), self.game_window_width, self.game_window_height, 20,
                               10)
        player = pygame.sprite.GroupSingle(player_sprite)

        # enemies initialized
        enemies = pygame.sprite.Group()
        self.generate_enemy(enemies, 5, 10)

        # score text
        text.draw_text(window, "Score: " + str(self.score), self.font, (0, 0, 255), 0, 0)

        # favicon
        pygame.display.set_icon(self.favicon)

        # game loop
        while True:

            # window.fill(gray_color)
            window.blit(background, (0, 0))

            # draws player on screen
            player.draw(window)

            # draws all the bolts on screen
            player.sprite.bolts.draw(window)

            # draws enemies on the screen
            enemies.draw(window)

            # updates the bolts on screen
            player.sprite.bolts.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                # key press events
                if event.type == pygame.KEYDOWN:

                    # test for enemy collision
                    # if event.key == pygame.K_f:
                    #     enemies.empty()
                    #     generate_enemy(enemies,5,10)

                    # checks for keyboard input from the player
                    player.update()

                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        return

            pygame.display.update()
            clock.tick(60)




