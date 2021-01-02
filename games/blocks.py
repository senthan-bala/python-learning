import pygame
import sys
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 50
BLOCK_COLOR = (255, 0, 0)
ENEMY_COLOR = (0, 0, 255)
BG_COLOR = (0, 0, 0)

player = [WIDTH / 2, HEIGHT - BLOCK_SIZE * 2]

enemy = [random.randint(0, WIDTH - BLOCK_SIZE), 0]

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_over = False

clock = pygame.time.Clock()

while not game_over:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            x = player[0]
            y = player[1]
            if event.key == pygame.K_LEFT:
                x -= BLOCK_SIZE
            elif event.key == pygame.K_RIGHT:
                x += BLOCK_SIZE
            player = [x, y]

    screen.fill(BG_COLOR)
    if enemy[1] >= 0 and enemy[1] < HEIGHT:
        enemy[1] += 15
    else:
        enemy[1] = 1

    pygame.draw.rect(screen, ENEMY_COLOR, (enemy[0], enemy[1], BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(
        screen, BLOCK_COLOR, (player[0], player[1], BLOCK_SIZE, BLOCK_SIZE)
    )
    clock.tick(30)
    pygame.display.update()
