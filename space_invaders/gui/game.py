import pygame
import random

import space_invaders.gui.button as button
from space_invaders.entity.player import Player
from space_invaders.entity.enemy import Enemy
from space_invaders.entity.bolt import Bolt


# draws text on given surface
def draw_text(surface, text, font, text_color, x, y):
    image = font.render(text, True, text_color)
    surface.blit(image, (x, y))


class Game:

    def __init__(self, game_window_width, game_window_height, score_to_win):
        self.game_window_width = game_window_width
        self.game_window_height = game_window_height
        self.title = "Space Invaders"

        pygame.init()
        self.font = pygame.font.Font('space_invaders/assets/font/Starjedi.ttf', 24)
        self.favicon = pygame.image.load('space_invaders/assets/images/favicon.png')
        self.score = 0

        self.score_to_win = score_to_win

        self.enemies = pygame.sprite.Group()
        self.enemy_bolts = pygame.sprite.Group()

        self.frequency = 250

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
        start_image = pygame.image.load('space_invaders/assets/images/buttonimages/start.png')
        exit_image = pygame.image.load('space_invaders/assets/images/buttonimages/exitbutton.png').convert_alpha()

        # buttons
        start_button = button.Button(265, 200, start_image, 0.4)
        exit_button = button.Button(265, 325, exit_image, 0.4)

        # game loop
        while True:

            # background color of menu
            window.fill((220, 141, 30))

            # text draw on screen
            draw_text(window, 'welcome to space invaders!', self.font, (0, 0, 0), 140, screen_height / 5)

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
    def generate_enemy(self, enemies, min_enemy, max_enemy):

        number_of_enemies = random.randint(min_enemy, max_enemy)

        while len(enemies) != number_of_enemies:

            enemy_hp = random.randint(1, 3)
            enemy_pos_x = random.randint(0, self.game_window_width)
            enemy_pos_y = random.randint(0, int(self.game_window_height - self.game_window_height / 2) - 0)

            enemy = Enemy((enemy_pos_x, enemy_pos_y), self.game_window_width, self.game_window_height, enemy_hp)
            enemy.check_constraint()
            enemies.add(enemy)

            if len(enemies) > 1:
                for current_enemy in enemies:
                    if current_enemy == enemy:
                        break
                    if pygame.sprite.collide_rect(enemy, current_enemy):
                        enemy.kill()
                        break

    # a random enemy shoots a blaster bolt
    def enemy_shoot(self):
        if self.enemies.sprites():
            random_enemy = random.choice(self.enemies.sprites())
            enemy_bolt = Bolt(random_enemy.rect.center, "green", self.game_window_height, 10)
            self.enemy_bolts.add(enemy_bolt)

    # checks for collisions, both from the player and the enemies
    def check_collision(self, player):

        # checks if player hit an enemy
        if player.sprite.bolts:
            for bolt in player.sprite.bolts:
                enemies_hit = pygame.sprite.spritecollide(bolt, self.enemies, False)
                if enemies_hit:
                    for enemy in enemies_hit:
                        bolt.kill()
                        enemy.hp -= 1
                        if enemy.hp == 0:
                            self.score += enemy.score_value
                            enemy.kill()

        # checks if an enemy hit the player
        if self.enemy_bolts.sprites():
            for bolt in self.enemy_bolts:
                if pygame.sprite.spritecollide(bolt, player, False):
                    bolt.kill()
                    player.sprite.hp -= 1

    def message(self, surface, message, color):
        message_surface = self.font.render(message, False, color)
        message_rect = message_surface.get_rect(center=(self.game_window_width/2, self.game_window_height/2))
        surface.blit(message_surface, message_rect)

    # draws text on given surface

    def start_game(self):
        pygame.init()

        # makes sure it runs on a fixed fps
        clock = pygame.time.Clock()

        # window creation and title
        window = pygame.display.set_mode((self.game_window_width, self.game_window_height))
        pygame.display.set_caption(self.title)

        # loads background
        background = pygame.image.load("space_invaders/assets/images/background.png")
        background = pygame.transform.scale(background, (self.game_window_width, self.game_window_height))

        # player initialized
        player_sprite = Player((self.game_window_width / 2, self.game_window_height), self.game_window_width, self.game_window_height, 10)
        player = pygame.sprite.GroupSingle(player_sprite)

        # favicon
        pygame.display.set_icon(self.favicon)

        # enemies timer of shooting
        enemy_bolt_frequency = pygame.USEREVENT + 1
        pygame.time.set_timer(enemy_bolt_frequency, self.frequency)

        # game loop
        while True:

            # window.fill(gray_color)
            window.blit(background, (0, 0))

            # draws player on screen
            player.draw(window)

            # draws all the bolts on screen
            player.sprite.bolts.draw(window)

            # generates random number of enemies and generates again if there are no more enemies
            if len(self.enemies) == 0 and player.sprite.is_alive() and self.score <= self.score_to_win:
                player.sprite.bolts.empty()
                self.enemy_bolts.empty()
                self.generate_enemy(self.enemies, 5, 10)

            # if there's less than two enemies, shooting frequency gets halved, so it's not unfair
            if len(self.enemies) <= 2:
                self.frequency = 500

            # if there's more enemy than two, shooting frequency goes back to normal
            if len(self.enemies) > 2:
                self.frequency = 250

            # checks for collisions
            self.check_collision(player)

            # enemies move randomly on screen
            for enemy in self.enemies.sprites():
                enemy.movement()

            # draws enemies on the screen
            self.enemies.draw(window)

            # enemy shoots at random times
            self.enemy_bolts.draw(window)
            self.enemy_bolts.update()

            # updates the bolts on screen
            player.sprite.bolts.update()

            # score text
            draw_text(window, f"Score: {self.score}", self.font, (255, 232, 31), 10, 0)

            # lives text
            draw_text(window, f"Lives: {player.sprite.hp}", self.font, (255,232,31), self.game_window_width-125, 0)

            # checks if player won
            if self.score >= self.score_to_win:
                self.message(window, f"You have defeated the Empire!", (255, 232, 31))
                pygame.display.update()
                pygame.time.wait(4000)
                break

            # checks if player still alive
            if not player.sprite.is_alive():
                self.message(window, f"You were the chosen one!", (255, 0, 0))
                pygame.display.update()
                pygame.time.wait(4000)
                break

            keys = pygame.key.get_pressed()
            if keys[pygame.K_w] or keys[pygame.K_a] or keys[pygame.K_d] or keys[pygame.K_s] or keys[pygame.K_SPACE]:
                player.update()

            if keys[pygame.K_ESCAPE]:
                break

            for event in pygame.event.get():

                if event.type == enemy_bolt_frequency:
                    self.enemy_shoot()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

            pygame.display.update()
            clock.tick(60)

        pygame.quit()