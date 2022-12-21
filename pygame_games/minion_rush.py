import pygame
import os
from random import randint

pygame.font.init()
pygame.mixer.init()

fps = 1
width = 400
height = 500
minion_size = 40
road_color = (128, 128, 128)
border_color = (0, 0, 0)
road_width = 50
minion_sped = road_width + 5
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minion Rush")
# soundtrack = pygame.mixer.Sound(os.path.join("pygame_stuff", "minion_soundtrack.mp3"))


def main_loop():
    start = False
    minion = pygame.Rect(
        (width / 2) - (minion_size / 2),
        (height / 2) - (minion_size / 2) + 180,
        minion_size,
        minion_size,
    )
    road1 = pygame.Rect((width / 2) - 80, 0, road_width, height * 2)
    road2 = pygame.Rect((width / 2) - (road_width / 2), 0, road_width, height * 2)
    road3 = pygame.Rect((width / 2) + 30, 0, road_width, height * 2)
    road_base = pygame.Rect((width / 2) - 85, 0, (road_width * 3) + 20, height * 2)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                # keys_pressed = pygame.key.get_pressed()
                minion_movements(event, minion, road_base)
        draw_screen(minion, road1, road2, road3, road_base)
        if start == False:
            start = True
            start = ask_to_start()


def draw_screen(minion, road1, road2, road3, road_base):
    window.fill((255, 255, 255))
    pygame.draw.rect(window, (0, 0, 0), road_base)
    pygame.draw.rect(window, road_color, road1)
    pygame.draw.rect(window, road_color, road2)
    pygame.draw.rect(window, road_color, road3)
    pygame.draw.rect(window, (255, 255, 0), minion)

    pygame.display.update()


def ask_to_start():
    continue_or_not = True
    print("Controls are right and left arrow keys")
    while continue_or_not:
        output = input("To start the game please press enter.")
        if output == "":
            print("Good Luck!")
            start = True
            return start
        else:
            start = False
            print("Sorry, that was an invalid input, please press enter to try again.")


def minion_movements(event, minion, road_base):
    if event.key == pygame.K_LEFT and minion.x - minion_sped > road_base.x:
        minion.x -= minion_sped
    if (
        event.key == pygame.K_RIGHT
        and minion.x + minion_sped < road_base.x + road_base.width
    ):
        minion.x += minion_sped


def send_objects():
    obj1 = pygame.Rect(125, 50, minion_size, minion_size)
    obj2 = pygame.Rect(180, 50, minion_size, minion_size)
    obj3 = pygame.Rect(235, 50, minion_size, minion_size)
    obj4 = pygame.Rect(125, 150, minion_size, minion_size)
    obj5 = pygame.Rect(180, 150, minion_size, minion_size)
    obj6 = pygame.Rect(235, 150, minion_size, minion_size)


main_loop()