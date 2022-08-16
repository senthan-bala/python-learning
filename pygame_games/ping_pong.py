import pygame
from random import randint
pygame.font.init()

fps=60
width=900
height=500
window=pygame.display.set_mode((width,height))
net=pygame.Rect((width/2-2.5,0,5,height))
net_s1=pygame.Rect((width/2-3.5,0,1,height))
net_s2=pygame.Rect((width/2+2.5,0,1,height))
border1=pygame.Rect((width-5,0,5,height))
border2=pygame.Rect((0,0,5,height))
border3=pygame.Rect((0,0,width,5))
border4=pygame.Rect((0,height-5,width,5))
white=(255,255,255)
ball_sped=8
og_racket_sped=8
score_font=pygame.font.SysFont("comicsans",30)
winner_font=pygame.font.SysFont("verdana",50)
dir_list={1:[1,2],2:[1,1],3:[2,2],4:[-1,2],5:[1,-2],6:[-1,-2],7:[-2,-2],8:[2,-2],9:[-2,2],10:[-1,-1],11:[2,1],12:[-2,1],13:[2,-1],14:[-2,-1],15:[-1,1],16:[1,-1]}
pygame.display.set_caption("Ping Pong")



def draw_screen(red_racket,blue_racket,ball,sped,rsped,dir_num,x,y,r_score,b_score):
    window.fill((0,150,110))
    pygame.draw.rect(window,white,net)
    pygame.draw.rect(window,(0,0,0),net_s1)
    pygame.draw.rect(window,(0,0,0),net_s2)
    pygame.draw.rect(window,white,border1)
    pygame.draw.rect(window,white,border2)
    pygame.draw.rect(window,white,border3)
    pygame.draw.rect(window,white,border4)
    pygame.draw.rect(window,(0,0,255),blue_racket)
    pygame.draw.rect(window,(255,0,0),red_racket)


    if ball.x<=-100:
        pygame.time.delay(20)
        ball.x=width/2
        ball.y=height/2
        sped=1
        dir_num=randint(1,12)
        rsped=og_racket_sped+sped
        x=dir_list[dir_num][0]
        y=dir_list[dir_num][1]
        r_score+=1
        if r_score>=11 and r_score-b_score>=2:
            winner="Red"
            win(winner,r_score,b_score)
            r_score=0
            b_score=0
        if b_score>=11 and b_score-r_score>=2:
            winner="Blue"
            win(winner,r_score,b_score)
            r_score=0
            b_score=0
    if ball.x>=width+100:
        dir_num=randint(1,12)
        pygame.time.delay(20)
        ball.x=width/2
        ball.y=height/2
        sped=1
        rsped=og_racket_sped+sped
        x=dir_list[dir_num][0]
        y=dir_list[dir_num][1]
        b_score+=1
        if r_score>=11 and r_score-b_score>=2:
            winner="Red"
            win(winner,r_score,b_score)
            r_score=0
            b_score=0
        if b_score>=11 and b_score-r_score>=2:
            winner="Blue"
            r_score,b_score=win(winner,r_score,b_score)
            r_score=0
            b_score=0
    score=score_font.render(str(b_score)+":"+str(r_score),1,(0,0,0))
    window.blit(score,(width/2-score.get_width()/2,height/20))
    pygame.draw.rect(window,white,ball)
    pygame.display.update()
    return sped,rsped,x,y,r_score,b_score


def win(winner,r_score,b_score):
    winner_text=score_font.render(winner+" wins!",1,(0,0,0))
    window.blit(winner_text,(width/2-winner_text.get_width()/2,height/10))
    score=score_font.render(str(b_score)+":"+str(r_score),1,(0,0,0))
    window.blit(score,(width/2-score.get_width()/2,height/20))
    pygame.display.update()
    pygame.time.delay(2000)

    return r_score,b_score


def racket_movement(red_racket,blue_racket,keys,racket_l,racket_s):
    if keys[pygame.K_UP] and red_racket.y-racket_s>0:
        red_racket.y-=racket_s
    if keys[pygame.K_DOWN] and red_racket.y+racket_l+racket_s<height:
        red_racket.y+=racket_s
    if keys[pygame.K_w]and blue_racket.y-racket_s>0:
        blue_racket.y-=racket_s
    if keys[pygame.K_s] and blue_racket.y+racket_l+racket_s<height:
        blue_racket.y+=racket_s

def handle_balls(red,blue,ball,x,y,sped,racket_sped):
    if ball.colliderect(border3)or ball.colliderect(border4):
        y=-y
    elif ball.colliderect(red) or ball.colliderect(blue):
        sped+=.04
        racket_sped=sped+og_racket_sped
        x=-x*sped
    ball.x+=x
    ball.y+=y
    return x,y,racket_sped,sped


        
    

def main():
    red_score=0
    blue_score=0
    racket_sped=8
    dir_num=randint(1,16)
    x=dir_list[dir_num][0]
    y=dir_list[dir_num][1]
    x*=2
    y*=2
    sped=1
    clock=pygame.time.Clock()
    not_dead=True
    racket_length=70
    blue_racket=pygame.Rect((50,215,7,racket_length))
    red_racket=pygame.Rect((850,215,7,racket_length))
    ball=pygame.Rect((width/2-10,height/2-10,20,20))
    while not_dead:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                not_dead=False
                pygame.quit()
        keys=pygame.key.get_pressed()
        x,y,racket_sped,sped=handle_balls(red_racket,blue_racket,ball,x,y,sped,racket_sped)
        racket_movement(red_racket,blue_racket,keys,racket_length,racket_sped)
        sped,racket_sped,x,y,red_score,blue_score=draw_screen(red_racket,blue_racket,ball,sped,racket_sped,dir_num,x,y,red_score,blue_score)
   

    
if __name__=="__main__":
    main()
