import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Geometry Dash")

# Player properties
player_size = 50
player_x = 100
player_y = HEIGHT - player_size
player_velocity = 0
gravity = 1
jump_strength = -15
is_jumping = False

# Obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacles = []
obstacle_speed = 5
obstacle_frequency = 1500  # milliseconds

# Game loop control
clock = pygame.time.Clock()
running = True

# Function to create obstacles
def create_obstacle():
    x = WIDTH
    y = HEIGHT - obstacle_height
    obstacles.append(pygame.Rect(x, y, obstacle_width, obstacle_height))

# Create an obstacle at intervals
pygame.time.set_timer(pygame.USEREVENT, obstacle_frequency)

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            create_obstacle()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and not is_jumping:
        player_velocity = jump_strength
        is_jumping = True

    if is_jumping:
        player_velocity += gravity
        player_y += player_velocity

        if player_y >= HEIGHT - player_size:
            player_y = HEIGHT - player_size
            is_jumping = False

    # Draw player
    pygame.draw.rect(screen, BLACK, (player_x, player_y, player_size, player_size))

    # Move and draw obstacles
    for obstacle in obstacles:
        obstacle.x -= obstacle_speed
        pygame.draw.rect(screen, BLACK, obstacle)
        if obstacle.x < -obstacle_width:
            obstacles.remove(obstacle)

        # Check collision
        if obstacle.colliderect(pygame.Rect(player_x, player_y, player_size, player_size)):
            print("Game Over!")
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
