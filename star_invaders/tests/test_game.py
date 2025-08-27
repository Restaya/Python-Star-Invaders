import unittest
import pygame

from star_invaders.gui.game import Game


# tests the game's enemy generation
class TestGui(unittest.TestCase):

    def test_init(self):

        pygame.init()

        window_width = 800
        window_height = 600
        game_window = Game(window_width, window_height, 25)
        window = pygame.display.set_mode((window_width, window_height))

        self.assertEqual(len(game_window.enemies), 0)

        game_window.generate_enemy(game_window.enemies, 5, 10)
        self.assertGreaterEqual(len(game_window.enemies), 5)
        pygame.quit()
