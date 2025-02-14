import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 400
PLAYER_SIZE = 30
PLAYER_SPEED = 5
ENEMY_SPEED = 2
GAME_DURATION = 10 * 60 * 1000  # 10 minutes in milliseconds

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chase Game")

# Load images
player1_img = pygame.image.load("https://github.com/chirumamilla798/mygame/blob/main/ca1.png")
player1_img = pygame.transform.scale(player1_img, (PLAYER_SIZE, PLAYER_SIZE))
player2_img = pygame.image.load("https://github.com/chirumamilla798/mygame/blob/main/ca2.png")
player2_img = pygame.transform.scale(player2_img, (PLAYER_SIZE, PLAYER_SIZE))

# Player and enemy positions
player1 = pygame.Rect(50, 50, PLAYER_SIZE, PLAYER_SIZE)
player2 = pygame.Rect(300, 200, PLAYER_SIZE, PLAYER_SIZE)

# Score and timer
score = 0
start_time = pygame.time.get_ticks()
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(WHITE)
    elapsed_time = pygame.time.get_ticks() - start_time
    
    # Check if game time is up
    if elapsed_time >= GAME_DURATION:
        print(f"Game Over! Final Score: {score}")
        running = False
        break
    
    # Handle events
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player1.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        player1.y += PLAYER_SPEED
    if keys[pygame.K_LEFT]:
        player1.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        player1.x += PLAYER_SPEED
    
    # Keep player within bounds
    player1.x = max(0, min(WIDTH - PLAYER_SIZE, player1.x))
    player1.y = max(0, min(HEIGHT - PLAYER_SIZE, player1.y))
    
    # Move Player 2 towards Player 1
    if player2.x < player1.x:
        player2.x += ENEMY_SPEED
    elif player2.x > player1.x:
        player2.x -= ENEMY_SPEED
    if player2.y < player1.y:
        player2.y += ENEMY_SPEED
    elif player2.y > player1.y:
        player2.y -= ENEMY_SPEED
    
    # Check for collision
    if player1.colliderect(player2):
        score += 1
        player2.x = random.randint(0, WIDTH - PLAYER_SIZE)
        player2.y = random.randint(0, HEIGHT - PLAYER_SIZE)
    
    # Draw players
    screen.blit(player1_img, (player1.x, player1.y))
    screen.blit(player2_img, (player2.x, player2.y))
    
    # Draw score
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))
    
    # Update display
    pygame.display.flip()
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(30)

pygame.quit()
