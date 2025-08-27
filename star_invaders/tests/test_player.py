import unittest
import pygame

from star_invaders.entity.player import Player


class TestPlayer(unittest.TestCase):

    # test for player can't move offscreen
    def test_player_constraints(self):

        pygame.init()
        window_width = 800
        window_height = 600
        window = pygame.display.set_mode((window_width, window_height))
        player = Player((0, 0), window_width, window_height, 10)

        player.rect.x = -10
        player.check_constraint()
        self.assertEqual(player.rect.x, 0, 0)

        player.rect.y = window.get_height() - window.get_height()/3 - 10
        player.check_constraint()
        self.assertEqual(player.rect.y, window.get_height() - window.get_height()/3)

        player.rect.right = window_width + 10
        player.check_constraint()
        self.assertEqual(player.rect.right, window_width)

        player.rect.bottom = window_height + 10
        player.check_constraint()
        self.assertEqual(player.rect.bottom, window_height)

        pygame.quit()

    # tests players ability to shoot with a cooldown
    def test_player_shoot(self):

        pygame.init()

        window = pygame.display.set_mode((800, 600))
        player = Player((0, 0), window.get_width(), window.get_height(), 10)

        player.ready = False
        player.recharge()  # simulating a shot, it has a 100 tick cooldown
        player.recharge()  # checks if 100 ticks passed since the shot
        self.assertTrue(player.ready)
