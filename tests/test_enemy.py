import unittest
import pygame
import os

from space_invaders.entity.enemy import Enemy


class TestEnemy(unittest.TestCase):

    def test_enemy_constraints(self):

        pygame.init()
        window_height = 600
        window_width = 800
        window = pygame.display.set_mode((800, 600))
        enemy = Enemy((0,0),window_width,window_height)

        enemy.rect.left = -10
        enemy.check_constraint()
        self.assertEqual(enemy.rect.left,0)

        enemy.rect.y = -10
        enemy.check_constraint()
        self.assertEqual(enemy.rect.y, 0)

        enemy.rect.right = window_width + 10
        enemy.check_constraint()
        self.assertEqual(enemy.rect.right, window_width)

        enemy.rect.bottom = window_height - window_height/3 + 10
        enemy.check_constraint()
        self.assertEqual(enemy.rect.bottom, window_height - window_height/3)

        pygame.quit()