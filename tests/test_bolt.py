import unittest
import pygame

from star_invaders.gui.game import Game
from star_invaders.entity.player import Player


class TestBolt(unittest.TestCase):

    # tests if the shoots method bolts get deleted after leaving the screen window
    def test_bolt(self):

        pygame.init()

        game = Game(800, 600, 25)
        window = pygame.display.set_mode((game.game_window_width, game.game_window_height))

        player = Player((game.game_window_width / 2, game.game_window_height), game.game_window_width, game.game_window_height, 10)

        self.assertEqual(len(player.bolts), 0)  # player starts with 0 bolts fired

        player.shoot()

        self.assertEqual(len(player.bolts), 2)  # players shoots 2 bolts

        for bolt in player.bolts:
            bolt.rect.y = -10
            bolt.update()

        self.assertNotEqual(len(player.bolts), 2)

        player.shoot()

        self.assertEqual(len(player.bolts), 2)

        for bolt in player.bolts:
            bolt.speed = 50
            bolt.update()

        self.assertNotEqual(len(player.bolts), 2)
