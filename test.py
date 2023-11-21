import pygame
import time
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 10
GRID_SIZE = 20
SNAKE_SIZE = 20

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

# Snake initialization
snake = [(WIDTH // 2, HEIGHT // 2)]
snake_dir = (GRID_SIZE, 0)

# Food initialization
food = (random.randint(0, (WIDTH - SNAKE_SIZE) // GRID_SIZE) * GRID_SIZE,
        random.randint(0, (HEIGHT - SNAKE_SIZE) // GRID_SIZE) * GRID_SIZE)

# Main game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, GRID_SIZE):
                snake_dir = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -GRID_SIZE):
                snake_dir = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (GRID_SIZE, 0):
                snake_dir = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-GRID_SIZE, 0):
                snake_dir = (GRID_SIZE, 0)

    # Move the snake
    x, y = snake[0]
    x += snake_dir[0]
    y += snake_dir[1]
    snake.insert(0, (x, y))

    # Check for collisions
    if x == food[0] and y == food[1]:
        food = (random.randint(0, (WIDTH - SNAKE_SIZE) // GRID_SIZE) * GRID_SIZE,
                random.randint(0, (HEIGHT - SNAKE_SIZE) // GRID_SIZE) * GRID_SIZE)
    else:
        snake.pop()

    # Check for collisions with walls or self
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or (x, y) in snake[1:]:
        game_over = True

    # Draw everything
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (food[0], food[1], SNAKE_SIZE, SNAKE_SIZE))

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
