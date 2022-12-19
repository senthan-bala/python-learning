import pygame
import os

# import turtle

pygame.font.init()
width = 900
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Two Player Pacman")
square_size = 15
square_speed = 2
# myfont = pygame.font.SysFont("comicsans", 40)
# t = turtle.Turtle()
# t.shape("turtle")
# t.pensize(3)
# t.speed(15)
# t.penup()
# t.hideturtle()


def main_loop():
    # frames = 0
    # seconds = 0
    # minutes = 0
    red = pygame.Rect(100, 100, square_size, square_size)
    blue = pygame.Rect(500, 100, square_size, square_size)
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys_pressed = pygame.key.get_pressed()
        # if frames > 60:
        #     seconds += 1
        #     frames -= 60
        # if seconds > 60:
        #     minutes += 1
        #     seconds -= 60
        # timex = minutes, ":", seconds
        # t.goto(300, 300)
        # t.write(timex)
        # # timelabel = myfont.render(, 1, (0, 0, 0))
        # # window.blit(timelabel, (200, 100))
        handle_square_movements(blue, red, keys_pressed)
        display(red, blue)
        # frames += 1


# def did_squares_collide():
#     if red.colliderect(blue):
#         final()

# def final


def display(red, blue):
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (255, 0, 0), red)
    pygame.draw.rect(window, (0, 0, 255), blue)
    pygame.display.update()


def handle_square_movements(blue, red, keys_pressed):
    # BLUE
    if keys_pressed[pygame.K_LEFT]:
        blue.x -= square_speed
    if keys_pressed[pygame.K_RIGHT]:
        blue.x += square_speed
    if keys_pressed[pygame.K_UP]:
        blue.y -= square_speed
    if keys_pressed[pygame.K_DOWN]:
        blue.y += square_speed
    # RED
    if keys_pressed[pygame.K_a]:
        red.x -= square_speed
    if keys_pressed[pygame.K_d]:
        red.x += square_speed
    if keys_pressed[pygame.K_w]:
        red.y -= square_speed
    if keys_pressed[pygame.K_s]:
        red.y += square_speed


main_loop()