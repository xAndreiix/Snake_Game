import unittest
import pygame
import snake_game
import random

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.snake = snake_game.Snake()
        self.snake.positions = [(10, 10)]
        self.snake.direction = (1, 0)
        self.obstacles = [(5, 5), (10, 11)]
        self.food = snake_game.Food(self.obstacles, self.snake.positions)

    def test_snake_initial_position(self):
        self.assertEqual(len(self.snake.positions), 1)

    def test_snake_move(self):
        initial_head = self.snake.positions[0]
        self.snake.move()
        new_head = self.snake.positions[0]
        self.assertNotEqual(initial_head, new_head)

    def test_snake_grow(self):
        self.snake.grow = True
        initial_length = len(self.snake.positions)
        self.snake.move()
        self.assertEqual(len(self.snake.positions), initial_length + 1)

    def test_snake_self_collision(self):
        self.snake.positions = [(10,10), (11,10), (10,10)]
        self.assertFalse(self.snake.move())

    def test_direction_change_block_reverse(self):
        self.snake.change_direction((-1, 0))
        self.assertEqual(self.snake.direction, (1, 0))

    def test_direction_change_valid(self):
        self.snake.change_direction((0, 1))
        self.assertEqual(self.snake.direction, (0, 1))

    def test_food_not_on_obstacle_or_snake(self):
        self.assertNotIn(self.food.position, self.obstacles)
        self.assertNotIn(self.food.position, self.snake.positions)

    def test_generate_obstacles(self):
        obs = snake_game.generate_obstacles(3)
        self.assertTrue(len(obs) > 0)

if __name__ == "__main__":
    unittest.main()