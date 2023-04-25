import unittest
import pygame

from space_invaders.gui.game import Game


class TestGui(unittest.TestCase):

    def test_init(self):
        game = Game(800, 600, 25)

        self.assertEqual(len(game.enemies),0)

        game.start_menu()
        game.generate_enemy(game.enemies,5,10)
        self.assertGreaterEqual(len(game.enemies),5)






