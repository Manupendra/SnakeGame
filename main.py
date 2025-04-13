import pygame
import time
import random

# Initialize pygame
pygame.init()

# Define window size
WIDTH = 600
HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

# Snake block size
BLOCK_SIZE = 10
SPEED = 15

# Initialize game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Font for messages
font = pygame.font.SysFont("bahnschrift", 25)


# Function to display the score
def display_score(score):
    value = font.render(f"Score: {score}", True, WHITE)
    screen.blit(value, [10, 10])


# Function to draw the snake
def draw_snake(block_size, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], block_size, block_size])


# Main game function
def game_loop():
    game_over = False
    game_close = False

    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0

    snake_list = []
    length_of_snake = 1

    food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
    food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)

    clock = pygame.time.Clock()

    while not game_over:
        while game_close:
            screen.fill(BLACK)
            message = font.render("Game Over! Press Q-Quit or C-Continue", True, RED)
            screen.blit(message, [WIDTH // 6, HEIGHT // 3])
            display_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = BLOCK_SIZE
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -BLOCK_SIZE
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = BLOCK_SIZE
                    dx = 0

        x += dx
        y += dy

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, [food_x, food_y, BLOCK_SIZE, BLOCK_SIZE])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        draw_snake(BLOCK_SIZE, snake_list)
        display_score(length_of_snake - 1)

        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = random.randrange(0, WIDTH - BLOCK_SIZE, BLOCK_SIZE)
            food_y = random.randrange(0, HEIGHT - BLOCK_SIZE, BLOCK_SIZE)
            length_of_snake += 1

        clock.tick(SPEED)

    pygame.quit()
    quit()


# Start the game
game_loop()
