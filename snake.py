import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

# Game screen dimensions
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Snake Game')

# Snake properties
block_size = 20
snake_speed = 15

# Font and clock
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
clock = pygame.time.Clock()

# Function to display score
def show_score(score):
    value = score_font.render("Score: " + str(score), True, black)
    screen.blit(value, [0, 0])

# Game loop
def game_loop():
    game_over = False
    game_close = False

    x = screen_width / 2
    y = screen_height / 2

    x_change = 0
    y_change = 0

    snake_length = 1
    snake_list = []

    apple_x = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
    apple_y = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0

    while not game_over:
        if snake_length - 1 >= 5:
            game_close = True

        while game_close:
            screen.fill(white)
            message = font_style.render("Game Over! Press C to play again or Q to quit.", True, red)
            screen.blit(message, [screen_width / 6, screen_height / 3])
            show_score(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x_change == 0:
                    x_change = -block_size
                    y_change = 0
                elif event.key == pygame.K_RIGHT and x_change == 0:
                    x_change = block_size
                    y_change = 0
                elif event.key == pygame.K_UP and y_change == 0:
                    y_change = -block_size
                    x_change = 0
                elif event.key == pygame.K_DOWN and y_change == 0:
                    y_change = block_size
                    x_change = 0

        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_close = True

        x += x_change
        y += y_change
        screen.fill(white)
        pygame.draw.rect(screen, green, [apple_x, apple_y, block_size, block_size])

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True
                break

        for segment in snake_list:
            pygame.draw.rect(screen, black, [segment[0], segment[1], block_size, block_size])

        show_score(snake_length - 1)
        pygame.display.update()

        if x == apple_x and y == apple_y:
            apple_x = round(random.randrange(0, screen_width - block_size) / 20.0) * 20.0
            apple_y = round(random.randrange(0, screen_height - block_size) / 20.0) * 20.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Start the game
game_loop()
