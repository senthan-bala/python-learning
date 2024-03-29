import pygame
import os

pygame.font.init()
pygame.mixer.init()

FPS = 60
WIDTH = 900
HEIGHT = 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
SHIP_WIDTH = 60
SHIP_HEIGHT = 40
YSHIP_WIDTH = (WIDTH / 4) - (SHIP_HEIGHT / 2)
YSHIP_HEIGHT = (HEIGHT / 2) - (SHIP_WIDTH / 2)
RSHIP_WIDTH = (3 * WIDTH / 4) - (SHIP_HEIGHT / 2)
RSHIP_HEIGHT = (HEIGHT / 2) - (SHIP_WIDTH / 2)
SHIP_SPED = 10
BORDER = pygame.Rect((WIDTH / 2) - 2.5, 0, 5, HEIGHT)
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join("pygame_stuff", "Grenade+1.mp3"))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join("pygame_stuff", "Gun+Silencer.mp3"))
HEALTH_FONT = pygame.font.SysFont("comicsans", 30)
WINNER_FONT = pygame.font.SysFont("verdana", 50)
BORDER_COLOR = (255, 255, 255)
BULLET_SPED = 10
MAX_BULLETS = 10
BULLET_COLOR = (255, 0, 0)
BG = pygame.transform.scale(
    pygame.image.load(os.path.join("pygame_stuff", "space.png")), (WIDTH, HEIGHT)
)


YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2


pygame.display.set_caption("Space laser game")
Yellow_spaceship = pygame.image.load(
    os.path.join("pygame_stuff", "spaceship_yellow.png")
)
Red_spaceship = pygame.image.load(os.path.join("pygame_stuff", "spaceship_red.png"))
Yellow_spaceship = pygame.transform.rotate(
    pygame.transform.scale(Yellow_spaceship, (SHIP_WIDTH, SHIP_HEIGHT)), 270
)
Red_spaceship = pygame.transform.rotate(
    pygame.transform.scale(Red_spaceship, (SHIP_WIDTH, SHIP_HEIGHT)), 90
)


def draw_screen(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, BORDER_COLOR, BORDER)
    red_health_text = HEALTH_FONT.render(
        "Health:" + str(red_health), 1, (255, 255, 255)
    )
    yellow_health_text = HEALTH_FONT.render(
        "Health:" + str(yellow_health), 1, (255, 255, 255)
    )
    WIN.blit(yellow_health_text, (WIDTH - yellow_health_text.get_width() - 15, 15))
    WIN.blit(red_health_text, (15, 15))
    WIN.blit(Yellow_spaceship, (yellow.x, yellow.y))
    WIN.blit(Red_spaceship, (red.x, red.y))
    for bullet in red_bullets:
        pygame.draw.rect(WIN, BULLET_COLOR, bullet)
    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, BULLET_COLOR, bullet)

    pygame.display.update()


def red_sped(keys_pressed, red):
    if keys_pressed[pygame.K_a] and red.x - SHIP_SPED + 6 > 0:  # left
        red.x -= SHIP_SPED
    if (
        keys_pressed[pygame.K_d] and red.x + SHIP_SPED + red.width - 20 < BORDER.x
    ):  # right
        red.x += SHIP_SPED
    if keys_pressed[pygame.K_w] and red.y - SHIP_SPED + 7 > 0:  # up
        red.y -= SHIP_SPED
    if (
        keys_pressed[pygame.K_s] and red.y + SHIP_SPED + red.height + 10 < HEIGHT
    ):  # down
        red.y += SHIP_SPED


def yellow_sped(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT] and yellow.x + SHIP_SPED - 18 > BORDER.x:  # left
        yellow.x -= SHIP_SPED
    if (
        keys_pressed[pygame.K_RIGHT]
        and yellow.x + SHIP_SPED + yellow.width - 25 < WIDTH
    ):  # right
        yellow.x += SHIP_SPED
    if keys_pressed[pygame.K_UP] and yellow.y - SHIP_SPED + 10 > 0:  # up
        yellow.y -= SHIP_SPED
    if (
        keys_pressed[pygame.K_DOWN]
        and yellow.y + SHIP_SPED + yellow.height + 10 < HEIGHT
    ):  # down
        yellow.y += SHIP_SPED


def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x -= BULLET_SPED
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x < 0:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x += BULLET_SPED
        if yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            red_bullets.remove(bullet)


def win(text):
    draw_text = WINNER_FONT.render(text, 1, (255, 255, 255))
    WIN.blit(
        draw_text,
        (
            WIDTH / 2 - draw_text.get_width() / 2,
            HEIGHT / 2 - draw_text.get_height() / 2,
        ),
    )
    pygame.display.update()
    pygame.time.delay(2500)


def main_loop():
    yellow_health = 5
    red_health = 5
    red = pygame.Rect(YSHIP_WIDTH, YSHIP_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT)
    yellow = pygame.Rect(RSHIP_WIDTH, RSHIP_HEIGHT, SHIP_WIDTH, SHIP_HEIGHT)
    red_bullets = []
    yellow_bullets = []
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        red.x + red.width - 10, red.y + (red.height / 2) - 2, 10, 4
                    )
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(
                        yellow.x, yellow.y + (yellow.height / 2) - 2, 10, 4
                    )
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()
        winner_text = ""
        if red_health <= 0:
            winner_text = "Yellow wins!"
        if yellow_health <= 0:
            winner_text = "Red wins!"
        if winner_text != "":
            win(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        # wasd
        red_sped(keys_pressed, red)
        # arrow keys
        yellow_sped(keys_pressed, yellow)
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_screen(red, yellow, red_bullets, yellow_bullets, red_health, yellow_health)
    main_loop()


if __name__ == "__main__":
    main_loop()
