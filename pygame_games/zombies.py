import pygame
from random import randint


fps=60
width=900
height=500
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("Zombies Attack")
player_width=75
player_speed=10
bullet_speed=15
zombie_speed=1
zombie_list=[]
max_bullets=5
bullet_width=4
bullet_height=10

for n in range(60):
    # inserted_zombie=pygame.Rect((randint(0,width),randint(0, height),player_width,player_width))
    r = randint(200, 400)
    f = randint(200, 400)
    inserted_zombie=pygame.Rect((r, f, player_width,player_width))
    zombie_list.append(inserted_zombie)


def main(zombie_list):
    clock=pygame.time.Clock()
    dead=False
    player=pygame.Rect((50,215,player_width,player_width))
    bullets=[]
    while not dead:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                dead=True
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q and len(bullets)<max_bullets:
                    bullet=pygame.Rect(player.x,player.y,bullet_width,bullet_height)
                    bullets.append(bullet)
        
        keys=pygame.key.get_pressed()
        player,zombie_list,bullets=display(player,zombie_list,bullets)
        player=player_movement(player,keys,player_width,player_speed)
        zombie_list,dead=zombie_movement(zombie_list,player,dead)
        bullets,zombie_list=handle_bullets(bullets,zombie_list)


def display(player,zombie_list,bullets):
    window.fill((75,75,75))
    pygame.draw.rect(window,(0,0,255),player)
    for zombie in zombie_list:
        pygame.draw.rect(window,(90,140,90),zombie)
    for bullet in bullets:
        pygame.draw.rect(window,(255,0,0),bullet)
    pygame.display.update()
    return player,zombie_list,bullets


def player_movement(player,keys,p_width,p_speed):
    if keys[pygame.K_w] and player.y-p_speed>0:
        player.y-=p_speed
    if keys[pygame.K_s] and player.y+p_width+p_speed<height:
        player.y+=p_speed
    if keys[pygame.K_a]and player.x-p_speed>0:
        player.x-=p_speed
    if keys[pygame.K_d] and player.x+p_width+p_speed<width:
        player.x+=p_speed
    return player


# def create_bullets():


def zombie_movement(zombie_list,player,dead):
    for zombie in zombie_list:
        zombie.y+=zombie_speed
        if player.colliderect(zombie):
            dead=True
    return zombie_list,dead

def handle_bullets(bullets,zombie_list):
    for bullet in bullets:
        bullet.y-=bullet_speed

        zombie_hit = check_zombie_hit(zombie_list, bullet)

        if zombie_hit or bullet.y < 0:
            bullets.remove(bullet)
        
    return bullets,zombie_list
            
def check_zombie_hit(zombie_list,bullet):
    for zombie in zombie_list:
        if zombie.colliderect(bullet):
            zombie.y=(0-player_width)
            zombie.x=randint(0,width)
            return True
    return False    




if __name__=="__main__":
    main(zombie_list)