import pygame
import sys, os
import random

# redirect pygame output to null device
sys.stdout = open(os.devnull, "w")

# Define some constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
SNAKE_BLOCK_SIZE = 10

# Initialize Pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pygame.display.set_caption("Snake")

# Set up the clock
clock = pygame.time.Clock()


# Define the Snake class
class Snake:
    def __init__(self):
        self.blocks = [(50, 50), (40, 50), (30, 50)]
        self.direction = "right"

    def move(self):
        x, y = self.blocks[0]

        if self.direction == "up":
            y -= SNAKE_BLOCK_SIZE
        elif self.direction == "down":
            y += SNAKE_BLOCK_SIZE
        elif self.direction == "left":
            x -= SNAKE_BLOCK_SIZE
        elif self.direction == "right":
            x += SNAKE_BLOCK_SIZE

        self.blocks.insert(0, (x, y))
        self.blocks.pop()

    def draw(self):
        for block in self.blocks:
            pygame.draw.rect(
                screen, GREEN, [block[0], block[1], SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE]
            )

    def change_direction(self, direction):
        if (
            direction == "up"
            and self.direction != "down"
            or direction == "down"
            and self.direction != "up"
            or direction == "left"
            and self.direction != "right"
            or direction == "right"
            and self.direction != "left"
        ):
            self.direction = direction

    def get_head_position(self):
        return self.blocks[0]

    def get_body_position(self):
        return self.blocks[1:]

    def grow(self):
        self.blocks.append(self.blocks[-1])


# Define the Food class
class Food:
    def __init__(self):
        self.position = self.generate_position()

    def generate_position(self):
        x = random.randint(0, WINDOW_WIDTH - SNAKE_BLOCK_SIZE)
        y = random.randint(0, WINDOW_HEIGHT - SNAKE_BLOCK_SIZE)
        return (
            x // SNAKE_BLOCK_SIZE * SNAKE_BLOCK_SIZE,
            y // SNAKE_BLOCK_SIZE * SNAKE_BLOCK_SIZE,
        )

    def draw(self):
        pygame.draw.rect(
            screen,
            RED,
            [self.position[0], self.position[1], SNAKE_BLOCK_SIZE, SNAKE_BLOCK_SIZE],
        )


# A function to display the current score on the screen
def show_score(score):
    font = pygame.font.Font(None, 30)
    score_text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(score_text, [10, 10])


# A function to display the "Game Over" message on the screen
def show_game_over():
    font = pygame.font.Font(None, 50)
    game_over_text = font.render("Game Over", True, WHITE)
    screen.blit(game_over_text, [WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2 - 25])


# A function to check if two rectangles are colliding with each other
def is_collision(rect1, rect2):
    return (
        rect1[0] < rect2[0] + SNAKE_BLOCK_SIZE
        and rect1[0] + SNAKE_BLOCK_SIZE > rect2[0]
        and rect1[1] < rect2[1] + SNAKE_BLOCK_SIZE
        and rect1[1] + SNAKE_BLOCK_SIZE > rect2[1]
    )


# Create the snake and food objects
snake = Snake()
food = Food()

# Set up the initial score
score = 0

# Set up the initial game state
game_over = False

# Start the game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("up")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("down")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("left")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("right")

    # Move the snake
    snake.move()

    # Check for collisions with the food
    if is_collision(snake.get_head_position(), food.position):
        food.position = food.generate_position()
        snake.grow()
        score += 1

    # Check for collisions with the walls or the snake's own body
    if (
        snake.get_head_position()[0] < 0
        or snake.get_head_position()[0] >= WINDOW_WIDTH
        or snake.get_head_position()[1] < 0
        or snake.get_head_position()[1] >= WINDOW_HEIGHT
        or any(
            is_collision(snake.get_head_position(), block)
            for block in snake.get_body_position()
        )
    ):
        game_over = True

    # Draw the screen
    screen.fill(BLACK)
    snake.draw()
    food.draw()
    show_score(score)
    if game_over:
        show_game_over()
    pygame.display.flip()

    # Set the frame rate
    clock.tick(15)

# Quit Pygame
pygame.quit()
