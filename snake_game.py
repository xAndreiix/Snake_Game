import pygame
import sys
import random

pygame.init()
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)
GRAY  = (128, 128, 128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Multiple Levels")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 24)

class Snake:
    def __init__(self):
        self.positions = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        self.grow = False

    def move(self):
        head_x, head_y = self.positions[0]
        dx, dy = self.direction
        new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)
        if new_head in self.positions:
            return False
        self.positions.insert(0, new_head)
        if not self.grow:
            self.positions.pop()
        else:
            self.grow = False
        return True

    def change_direction(self, new_direction):
        if (new_direction[0] * -1, new_direction[1] * -1) == self.direction:
            return
        self.direction = new_direction

    def draw(self, surface):
        for pos in self.positions:
            rect = pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(surface, GREEN, rect)

class Food:
    def __init__(self, obstacles, snake_positions):
        self.color = RED
        self.obstacles = obstacles
        self.snake_positions = snake_positions
        self.position = (0, 0)
        self.randomize_position()

    def randomize_position(self):
        available = [
            (x, y)
            for x in range(GRID_WIDTH)
            for y in range(GRID_HEIGHT)
            if (x, y) not in self.snake_positions and (x, y) not in self.obstacles
        ]
        if available:
            self.position = random.choice(available)

    def draw(self, surface):
        rect = pygame.Rect(self.position[0] * CELL_SIZE, self.position[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, self.color, rect)

def draw_obstacles(surface, obstacles):
    for pos in obstacles:
        rect = pygame.Rect(pos[0] * CELL_SIZE, pos[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(surface, GRAY, rect)

def generate_obstacles(level):
    obstacles = []
    if level >= 2:
        for x in range(5, GRID_WIDTH - 5):
            obstacles.append((x, GRID_HEIGHT // 2))
    if level >= 3:
        for y in range(3, GRID_HEIGHT - 3):
            obstacles.append((GRID_WIDTH // 2, y))
    if level >= 4:
        for i in range(level * 2):
            obstacles.append((random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1)))
    return obstacles

def main():
    level = 1
    score = 0
    snake = Snake()
    obstacles = generate_obstacles(level)
    food = Food(obstacles, snake.positions)
    speed = 10

    running = True
    while running:
        clock.tick(speed)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.change_direction((0, -1))
                elif event.key == pygame.K_DOWN:
                    snake.change_direction((0, 1))
                elif event.key == pygame.K_LEFT:
                    snake.change_direction((-1, 0))
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction((1, 0))

        if not snake.move():
            running = False
        head = snake.positions[0]
        if head in obstacles:
            running = False

        if head == food.position:
            snake.grow = True
            score += 1
            food = Food(obstacles, snake.positions)
            if score % 5 == 0:
                level += 1
                obstacles = generate_obstacles(level)
                speed += 2

        screen.fill(BLACK)
        snake.draw(screen)
        food.draw(screen)
        draw_obstacles(screen, obstacles)
        score_text = font.render(f"Score: {score}   Level: {level}", True, WHITE)
        screen.blit(score_text, (10, 10))
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()
