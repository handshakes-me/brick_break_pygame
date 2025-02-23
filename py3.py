import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# Ball properties
ball_radius = 10
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [random.choice([3, -3]), -3]

# Paddle properties
paddle_width = 100
paddle_height = 15
paddle_pos = [WIDTH // 2 - paddle_width // 2, HEIGHT - paddle_height - 10]
paddle_speed = 10

# Brick properties
brick_width = 75
brick_height = 20
brick_rows = 5
brick_cols = 10
bricks = []

for i in range(brick_rows):
    row = []
    for j in range(brick_cols):
        brick_x = j * (brick_width + 5) + 35
        brick_y = i * (brick_height + 5) + 35
        row.append(pygame.Rect(brick_x, brick_y, brick_width, brick_height))
    bricks.append(row)

# Power-up properties
power_up_size = 20
power_up_speed = 5
power_ups = []

# Clock to control frame rate
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_pos[0] < WIDTH - paddle_width:
        paddle_pos[0] += paddle_speed

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Ball collision with walls
    if ball_pos[0] <= ball_radius or ball_pos[0] >= WIDTH - ball_radius:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] <= ball_radius:
        ball_vel[1] = -ball_vel[1]

    # Ball collision with paddle
    if (paddle_pos[0] < ball_pos[0] < paddle_pos[0] + paddle_width and
            paddle_pos[1] < ball_pos[1] + ball_radius < paddle_pos[1] + paddle_height):
        ball_vel[1] = -ball_vel[1]

    # Ball collision with bricks
    for row in bricks:
        for brick in row:
            if brick.collidepoint(ball_pos[0], ball_pos[1]):
                ball_vel[1] = -ball_vel[1]
                row.remove(brick)

                # Add power-up with a probability
                if random.random() < 0.2:
                    power_ups.append(pygame.Rect(brick.x + brick_width // 2, brick.y, power_up_size, power_up_size))

    # Update power-ups
    for power_up in power_ups:
        power_up.y += power_up_speed
        if power_up.colliderect(pygame.Rect(paddle_pos[0], paddle_pos[1], paddle_width, paddle_height)):
            power_ups.remove(power_up)
            # Add a power-up effect (e.g., increase paddle size)
            paddle_width += 20

    # Check if ball hits the bottom
    if ball_pos[1] > HEIGHT:
        ball_pos = [WIDTH // 2, HEIGHT // 2]
        ball_vel = [random.choice([3, -3]), -3]

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)
    pygame.draw.rect(screen, WHITE, (paddle_pos[0], paddle_pos[1], paddle_width, paddle_height))
    for row in bricks:
        for brick in row:
            pygame.draw.rect(screen, RED, brick)
    for power_up in power_ups:
        pygame.draw.rect(screen, YELLOW, power_up)
    pygame.display.flip()

    # Control the frame rate
    clock.tick(FPS)

pygame.quit()
