import pygame

# import os
from random import randint

pygame.font.init()
# pygame.mixer.init()

fps = 60
width = 900
height = 500
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Two Player Pacman")
square_size = 20
square_speed = 2
black = (0, 0, 0)
# blue_surface = pygame.transform.scale(
#     pygame.image.load(os.path.join("pygame_stuff", "blue_square.jpg")),
#     (square_size, square_size),
# )
# red_surface = pygame.transform.scale(
#     pygame.image.load(os.path.join("pygame_stuff", "red_square.jpg")),
#     (square_size, square_size),
# )
font = pygame.font.Font("freesansbold.ttf", 15)
end_font = pygame.font.Font("freesansbold.ttf", 70)
well_done_font = pygame.font.Font("freesansbold.ttf", 35)

text = font.render("sampletext", True, (0, 0, 0), (255, 255, 255))
textRect = text.get_rect()
textRect.center = (50, 15)


def draw_screen(
    red,
    blue,
    text,
    textrect,
    one,
    two,
    three,
    four,
    five,
    six,
    seven,
    eight,
    nine,
    ten,
    eleven,
    twelve,
):
    window.fill((255, 255, 255))
    window.blit(text, textrect)
    pygame.draw.rect(window, (255, 0, 0), red)
    pygame.draw.rect(window, (0, 0, 255), blue)
    # obstacles
    pygame.draw.rect(window, black, one)
    pygame.draw.rect(window, black, two)
    pygame.draw.rect(window, black, three)
    pygame.draw.rect(window, black, four)
    pygame.draw.rect(window, black, five)
    pygame.draw.rect(window, black, six)
    pygame.draw.rect(window, black, seven)
    pygame.draw.rect(window, black, eight)
    pygame.draw.rect(window, black, nine)
    pygame.draw.rect(window, black, ten)
    pygame.draw.rect(window, black, eleven)
    pygame.draw.rect(window, black, twelve)
    pygame.display.update()


def main_loop():
    (
        one,
        two,
        three,
        four,
        five,
        six,
        seven,
        eight,
        nine,
        ten,
        eleven,
        twelve,
    ) = create_obstacles()
    frames = 0
    seconds = 0
    minutes = 0
    red = pygame.Rect(100, 100, square_size, square_size)
    blue = pygame.Rect(500, 100, square_size, square_size)
    clock = pygame.time.Clock()
    run = True
    while run:
        stopwatch_time = turn_time_into_text(minutes, seconds)
        current_time = font.render(stopwatch_time, True, (0, 0, 0), (255, 255, 255))
        textrect = current_time.get_rect()
        textrect.center = (50, 15)
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        if frames > 60:
            seconds += 1
            frames -= 60
        if seconds > 60:
            minutes += 1
            seconds -= 60
        keys_pressed = pygame.key.get_pressed()
        square_movements(red, blue, keys_pressed)
        collide = check_for_square_collision(red, blue)
        draw_screen(
            red,
            blue,
            current_time,
            textrect,
            one,
            two,
            three,
            four,
            five,
            six,
            seven,
            eight,
            nine,
            ten,
            eleven,
            twelve,
        )
        frames += 1
        if collide == True:
            finish_game(minutes, seconds)
            run = False


def square_movements(red, blue, keys):
    # TODO - do not pass through obstacles
    # for red
    if keys[pygame.K_UP] and red.y - square_speed > 0:
        red.y -= square_speed
    if keys[pygame.K_DOWN] and red.y + square_speed + square_size < height:
        red.y += square_speed
    if keys[pygame.K_LEFT] and red.x - square_speed > 0:
        red.x -= square_speed
    if keys[pygame.K_RIGHT] and red.x + square_speed + square_size < width:
        red.x += square_speed
    # for blue
    if keys[pygame.K_w] and blue.y - square_speed > 0:
        blue.y -= square_speed
    if keys[pygame.K_s] and blue.y + square_speed + square_size < height:
        blue.y += square_speed
    if keys[pygame.K_a] and blue.x - square_speed > 0:
        blue.x -= square_speed
    if keys[pygame.K_d] and blue.x + square_speed + square_size < width:
        blue.x += square_speed


def turn_time_into_text(mins, secs):
    min_amt = str(mins)
    sec_amt = str(secs)
    if secs >= 10 and mins >= 10:
        tim = min_amt + ":" + sec_amt
    if secs < 10 and mins < 10:
        tim = "0" + min_amt + ":0" + sec_amt
    if secs >= 10 and mins < 10:
        tim = "0" + min_amt + ":" + sec_amt
    if secs < 10 and mins >= 10:
        tim = min_amt + ":0" + sec_amt
    return tim


def check_for_square_collision(red, blue):
    collide = False
    if blue.colliderect(red):
        collide = True
    return collide


def finish_game(minutes, seconds):
    window.fill((255, 255, 255))
    stopwatch_time = turn_time_into_text(minutes, seconds)
    end_message = "Your final time was " + stopwatch_time
    final_time = end_font.render(end_message, True, (0, 0, 0), (255, 255, 255))
    textrect = final_time.get_rect()
    textrect.center = (width / 2, height / 2)
    window.blit(final_time, textrect)
    if minutes >= 2:
        well_done_text = well_done_font.render(
            "Well done!", False, (0, 0, 0), (255, 255, 255)
        )
        well_done = well_done_text.get_rect()
        well_done.center = (width / 2, (height / 2) + 140)
        window.blit(well_done_text, well_done)
    pygame.display.update()
    pygame.time.delay(4500)


def create_obstacles():
    # TODO - change to list
    one = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    two = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    three = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    four = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    five = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    six = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    seven = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    eight = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    nine = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    ten = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    eleven = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    twelve = pygame.Rect(
        randint(100, 850), randint(100, 450), randint(20, 100), randint(20, 100)
    )
    return one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve


main_loop()