import pygame

# import os
from random import randint

pygame.font.init()
# pygame.mixer.init()

# main variables
fps = 60
width = 900
height = 500
square_size = 20
square_speed = 2
obstacle_count = 25
obstacle_kills = False
black = (0, 0, 0)

# blue_surface = pygame.transform.scale(
#     pygame.image.load(os.path.join("pygame_stuff", "blue_square.jpg")),
#     (square_size, square_size),
# )
# red_surface = pygame.transform.scale(
#     pygame.image.load(os.path.join("pygame_stuff", "red_square.jpg")),
#     (square_size, square_size),
# )

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Two Player Pacman")

font = pygame.font.Font("freesansbold.ttf", 15)
end_font = pygame.font.Font("freesansbold.ttf", 70)
well_done_font = pygame.font.Font("freesansbold.ttf", 35)

# text = font.render("sampletext", True, (0, 0, 0), (255, 255, 255))
# textRect = text.get_rect()
# textRect.center = (50, 15)


def main_loop():
    obstacles = create_obstacles()
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
        # TODO - handle movement only for the object for which key pressed
        square_movements(red, blue, keys_pressed, obstacles)
        players_collide = check_for_collision(red, blue)
        draw_screen(
            red,
            blue,
            current_time,
            textrect,
            obstacles,
        )
        frames += 1
        if players_collide == True:
            finish_game(minutes, seconds)
            run = False


def square_movements(red, blue, keys, obstacles):
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


def check_for_collision(obj1, obj2):
    collide = False
    if obj1.colliderect(obj2):
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
    if minutes >= 1:
        well_done_text = well_done_font.render(
            "Well done!", False, (0, 0, 0), (255, 255, 255)
        )
        well_done = well_done_text.get_rect()
        well_done.center = (width / 2, (height / 2) + 140)
        window.blit(well_done_text, well_done)
    pygame.display.update()
    pygame.time.delay(4500)


def create_obstacles():
    obs_position = (10, 850, 10, 450)
    obs_dimension = (20, 125, 20, 125)
    return [create_obstacle(obs_position, obs_dimension) for i in range(obstacle_count)]


def create_obstacle(obs_position, obs_dimension):
    (x_min, x_max, y_min, y_max) = obs_position
    (w_min, w_max, h_min, h_max) = obs_dimension
    return pygame.Rect(
        randint(x_min, x_max),
        randint(y_min, y_max),
        randint(w_min, w_max),
        randint(h_min, h_max),
    )


def draw_screen(
    red,
    blue,
    text,
    textrect,
    obstacles,
):
    window.fill((255, 255, 255))
    window.blit(text, textrect)
    pygame.draw.rect(window, (255, 0, 0), red)
    pygame.draw.rect(window, (0, 0, 255), blue)
    # obstacles
    [draw_rect(obstacle) for obstacle in obstacles]
    pygame.display.update()


def draw_rect(obstacle):
    pygame.draw.rect(window, black, obstacle)


main_loop()