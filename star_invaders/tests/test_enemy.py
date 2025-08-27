import unittest
import pygame

from star_invaders.entity.enemy import Enemy


class TestEnemy(unittest.TestCase):

    # checks if enemy is within the screens boundaries and not offscreen
    def test_enemy_constraints(self):

        pygame.init()
        window_width = 800
        window_height = 600
        window = pygame.display.set_mode((window_width, window_height))
        enemy = Enemy((0, 0), window_width, window_height)

        enemy.rect.left = -10
        enemy.check_constraint()
        self.assertEqual(enemy.rect.left, 0)

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
