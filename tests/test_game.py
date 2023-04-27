import unittest
import pygame

from star_invaders.gui.game import Game


class TestGui(unittest.TestCase):

    def test_init(self):

        pygame.init()

        game = Game(800, 600, 25)
        window = pygame.display.set_mode((game.game_window_width, game.game_window_height))

        self.assertEqual(len(game.enemies), 0)

        game.generate_enemy(game.enemies, 5, 10)
        self.assertGreaterEqual(len(game.enemies), 5)
