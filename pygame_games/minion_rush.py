import pygame

# import os
from random import randint
from random import choice

pygame.font.init()
# pygame.mixer.init()

fps = 60
width = 400
height = 500
minion_size = 40
road_color = (128, 128, 128)
border_color = (0, 0, 0)
road_width = 50
minion_sped = road_width + 5
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Minion Rush")
# soundtrack = pygame.mixer.Sound("pygame_stuff/minion_soundtrack.mp3")
font = pygame.font.Font("freesansbold.ttf", 15)
end_font = pygame.font.Font("freesansbold.ttf", 25)


def main_loop():
    score = 0
    obj_speed = 4
    frames = 0
    start = False
    minion = pygame.Rect(
        (width / 2) - (minion_size / 2),
        (height / 2) - (minion_size / 2) + 180,
        minion_size,
        minion_size,
    )
    obj1 = pygame.Rect(130, -randint(400, 700), minion_size - 10, minion_size - 10)
    obj2 = pygame.Rect(185, -randint(400, 700), minion_size - 10, minion_size - 10)
    obj3 = pygame.Rect(240, -randint(400, 700), minion_size - 10, minion_size - 10)
    obj4 = pygame.Rect(130, -randint(400, 700), minion_size - 10, minion_size - 10)
    obj_list = [obj1, obj2, obj3, obj4]
    coin1 = pygame.Rect(130, -randint(400, 700), minion_size - 10, minion_size - 10)
    coin2 = pygame.Rect(185, -randint(400, 700), minion_size - 10, minion_size - 10)
    coin3 = pygame.Rect(240, -randint(400, 700), minion_size - 10, minion_size - 10)
    coin4 = pygame.Rect(130, -randint(400, 700), minion_size - 10, minion_size - 10)
    lanes=(130,185,240)
    diamond_lane_choice=choice(lanes)
    diamond = pygame.Rect(diamond_lane_choice, -randint(400, 3000), minion_size - 10, minion_size - 10)
    coin_list=[coin1, coin2, coin3, coin4]
    road1 = pygame.Rect((width / 2) - 80, 0, road_width, height * 2)
    road2 = pygame.Rect((width / 2) - (road_width / 2), 0, road_width, height * 2)
    road3 = pygame.Rect((width / 2) + 30, 0, road_width, height * 2)
    road_base = pygame.Rect((width / 2) - 85, 0, (road_width * 3) + 20, height * 2)
    run = True

    # counter to slow down execution & screen refresh
    clock = pygame.time.Clock()
    while run:
        clock.tick(fps)
        current_score = font.render(str(score), True, (0, 0, 0), (255, 255, 255))
        scorerect = current_score.get_rect()
        scorerect.center = (50, 15)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                minion_movements(event, minion, road_base)

        # slow down execution & screen refresh for every thousanth execution
        # counter += 1
        # if counter == 1000:
        #     counter = 0
        run = detect_for_collision(minion, obj_list)
        score = send_objects(obj_list, obj_speed, score)
        score = send_coins(coin_list, obj_speed, score,minion,obj_list)
        score = send_diamond(minion,score, obj_speed,diamond)
        draw_screen(
            minion, road1, road2, road3, road_base, obj_list, scorerect, current_score, coin_list,diamond
        )

        # if start == False:
        #     start = ask_to_start()
            # if start == True:
            # soundtrack.play()

        frames += 1
        if frames == 9000:
            frames -= 9000
            # obj_speed += 1
        if run == False:
            finish_game(score)


def draw_screen(
    minion, road1, road2, road3, road_base, obj_list, scorerect, current_score, coin_list, diamond
):
    window.fill((255, 255, 255))
    window.blit(current_score, scorerect)
    pygame.draw.rect(window, (0, 0, 0), road_base)
    pygame.draw.rect(window, road_color, road1)
    pygame.draw.rect(window, road_color, road2)
    pygame.draw.rect(window, road_color, road3)
    pygame.draw.rect(window, (255, 255, 0), minion)
    [draw_objects(obj, (0,0,0)) for obj in obj_list]
    [draw_objects(coin,(255,255,0)) for coin in coin_list]
    pygame.draw.rect(window, (0, 255, 255), diamond)
    pygame.display.update()


def draw_objects(obj,color):
    pygame.draw.rect(window, color, obj)


def ask_to_start():
    continue_or_not = True
    print("Controls are right and left arrow keys")
    while continue_or_not:
        output = input("To start the game please press enter.")
        if output == "":
            print("Good Luck!")
            start = True
            pygame.time.delay(2500)
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


def send_objects(obj_list, obj_speed, score):
    for obj in obj_list:
        score = send_obj(obj, obj_speed, score)
    obj1, obj2, obj3, obj4 = obj_list
    if abs(obj2.y - obj3.y) <= 150 and (
        abs(obj2.y - obj1.y) <= 150 or abs(obj2.y - obj4.y) <= 150
    ):
        obj2.y -= 250
    return score


def send_coins(coin_list, obj_speed, score,minion,obj_list):
    for coin in coin_list:
        score = send_coin(coin, obj_speed, score, minion)
        obj1,ojb2,obj3,obj4=obj_list
        if abs(coin.y - obj3.y) <= 150 and (
           abs(coin.y - obj1.y) <= 150 or abs(coin.y - obj4.y) <= 150
      ):
            coin.y -= 250
    return score


def send_diamond(minion,score, obj_speed,diamond):
    if diamond.y < height:
        diamond.y += obj_speed 
    elif diamond.y >height:
        diamond.y = -randint(100, 2000)
    if diamond.colliderect(minion):
        diamond.y = -randint(100, 2000)
        score += 1000
    return score



def send_obj(obj, obj_speed, score):
    if obj.y < -200:
        obj.y += obj_speed 
    elif obj.y <= height and obj.y >= -200:
        obj.y += obj_speed
    elif obj.y > height:
        obj.y = -randint(100, 1000)
        score += 100
    return score

def send_coin(coin, obj_speed, score,minion):
    if coin.y < height:
        coin.y += obj_speed 
    elif coin.y >height:
        coin.y = -randint(100, 400)
    if coin.colliderect(minion):
        coin.y = -randint(100, 400)
        score += 100
    return score


def detect_for_collision(minion, obj_list):
    keep_running = True
    for obj in obj_list:
        if minion.colliderect(obj):
            keep_running = False
    return keep_running


def finish_game(score):
    window.fill((255, 255, 255))
    end_message = "Your final score was " + str(score)
    final_time = end_font.render(end_message, True, (0, 0, 0), (255, 255, 255))
    textrect = final_time.get_rect()
    textrect.center = (width / 2, height / 2)
    window.blit(final_time, textrect)
    if score >= 15000:
        well_done_text = font.render("Well done!", False, (0, 0, 0), (255, 255, 255))
        well_done = well_done_text.get_rect()
        well_done.center = (width / 2, (height / 2) + 140)
        window.blit(well_done_text, well_done)
    pygame.display.update()
    pygame.time.delay(4500)


main_loop()