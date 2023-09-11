import pygame
import os
pygame.mixer.init()

fps=60
width=900
height=500
window=pygame.display.set_mode((width,height))
# Blue_ghost=pygame.transform.flip(window,True,False)
ghost_height=125
ghost_width=100
ghost_sped=5
redx=1.5*ghost_width
redy=height-ghost_height
bluex=width-2.5*ghost_width
bluey=height-ghost_height
red_hit=pygame.USEREVENT+1
blue_hit=pygame.USEREVENT+2
pygame.display.set_caption("Ghost Fighting")
Red_ghost=pygame.image.load(os.path.join('pygame_stuff','Red_fighter.png'))
Blue_ghost=pygame.image.load(os.path.join('pygame_stuff','Blue_fighter.png'))
incorrect_sound=pygame.mixer.Sound(os.path.join("pygame_stuff","incorrect_sound.mp3"))
Red_ghost=pygame.transform.flip(Red_ghost,True,False)
Red_ghost=pygame.transform.scale(Red_ghost,(ghost_width,ghost_height))
Blue_ghost=pygame.transform.scale(Blue_ghost,(ghost_width,ghost_height))
jump_sound=pygame.mixer.Sound("jumping.wav")
punch_sound=pygame.mixer.Sound("punch.wav")
red=pygame.Rect(redx,redy,ghost_width,ghost_height)
blue=pygame.Rect(bluex,bluey,ghost_width,ghost_height)


def draw(red,blue,flip,Red_ghost,Blue_ghost,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist):
    if red.x>blue.x and flip==0:
        Red_ghost=pygame.transform.flip(Red_ghost,True,False)
        Blue_ghost=pygame.transform.flip(Blue_ghost,True,False) 
        flip=1
        return flip
    elif blue.x>red.x and flip==1:
        Red_ghost=pygame.transform.flip(Red_ghost,True,False)
        Blue_ghost=pygame.transform.flip(Blue_ghost,True,False)
        flip=0
        return flip
    window.fill((135,206,235))
    pygame.draw.circle(window,(255,255,0),(100,75),50)
    pygame.draw.polygon(window,(200,200,200),((0,300),(0,500),(150,500),(150,450)))
    pygame.draw.polygon(window,(200,200,200),((900,300),(900,500),(750,500),(750,450)))
    window.blit(Red_ghost,(red.x,red.y))
    window.blit(Blue_ghost,(blue.x,blue.y))
    if onion>-1:
        pygame.draw.polygon(window,(250,160,0),Bpunch_location)
        pygame.draw.rect(window,(0,171,255),Bhand)
        pygame.draw.rect(window,(250,160,0),Bfist)
    if cookie>-1:
        pygame.draw.polygon(window,(250,160,0),Rpunch_location)
        pygame.draw.rect(window,(255,0,0),Rhand)
        pygame.draw.rect(window,(250,160,0),Rfist)
    pygame.display.update()
    # return flip
    return flip

def ghost_moving_backup(red,blue,keys,ghost_w,rev_col,potato,banana):
    if banana <=ghost_height and potato==True:
        banana+=1
    elif banana>ghost_height:
        banana-=1
        potato=False
    if keys[pygame.K_LEFT] and blue.x-1>0:
        blue.x-=1
    if keys[pygame.K_RIGHT] and blue.x+ghost_w+1<width:
        blue.x+=1
    if keys[pygame.K_a]and red.x-1>0:
        red.x-=1
    if keys[pygame.K_d] and red.x+ghost_w+1<width:
        red.x+=1
    if rev_col==red:
        if keys[pygame.K_w]:
            if banana<=ghost_height and potato==True:
                red.y-=1
            elif banana> ghost_height:
                red.y+=2
    elif rev_col==blue:
        if keys[pygame.K_UP]:
            if banana<=ghost_height and potato==True:
                blue.y-=1
            elif banana> ghost_height:
                blue.y+=2
    return banana


def ghost_moving(red,blue,keys,ghost_w,ghost_s,flip,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist):
    potato=True
    if keys[pygame.K_UP]:
        rev_col=red
        banana=0
        pygame.mixer.Sound.play(jump_sound)
        for i in range(ghost_height):
            delay=round(i/25)
            blue.y-=1
            pygame.time.delay(delay)
            banana=ghost_moving_backup(red,blue,keys,ghost_w,rev_col,potato,banana)
            flip=draw(red,blue,flip,Red_ghost,Blue_ghost,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist)
            flip=draw(red,blue,flip,Red_ghost,Blue_ghost,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist)
        for i in range(ghost_height):
            delay=5-round(i/25)
            blue.y+=1
            pygame.time.delay(delay)
            banana=ghost_moving_backup(red,blue,keys,ghost_w,rev_col,potato,banana)
            flip=draw(red,blue,flip,Red_ghost,Blue_ghost,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist)
            flip=draw(red,blue,flip,Red_ghost,Blue_ghost,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist)
    if keys[pygame.K_LEFT] and blue.x-ghost_s>0:
        blue.x-=ghost_s
    if keys[pygame.K_RIGHT] and blue.x+ghost_w+ghost_s<width:
        blue.x+=ghost_s
    if keys[pygame.K_w]:
        rev_col=blue
        banana=0
        pygame.mixer.Sound.play(jump_sound)
        for i in range(ghost_height):
            delay=round(i/25)
            red.y-=1
            pygame.time.delay(delay)
            banana=ghost_moving_backup(red,blue,keys,ghost_w,rev_col,potato,banana)
            flip=draw(red,blue,flip,Red_ghost,Blue_ghost,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist)
            flip=draw(red,blue,flip,Red_ghost,Blue_ghost,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist)
        for i in range(ghost_height):
            delay=5-round(i/25)
            red.y+=1
            pygame.time.delay(delay)
            banana=ghost_moving_backup(red,blue,keys,ghost_w,rev_col,potato,banana)
            flip=draw(red,blue,flip,Red_ghost,Blue_ghost,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist)
            flip=draw(red,blue,flip,Red_ghost,Blue_ghost,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist)
    if keys[pygame.K_a]and red.x-ghost_s>0:
        red.x-=ghost_s
    if keys[pygame.K_d] and red.x+ghost_w+ghost_s<width:
        red.x+=ghost_s

def handle_punches(blue_punches,red_punches,Rpunch_location,Bpunch_location,onion,cookie,Rhand,Bhand,Rfist,Bfist,flip):
    for punch in blue_punches:
        if onion==-1:
            pygame.draw.polygon(window,(250,160,0),Bpunch_location)
            pygame.draw.rect(window,(0,171,255),Bhand)
            pygame.draw.rect(window,(250,160,0),Bfist)
            blue_punches.remove(punch)
            pygame.display.update()
            onion=8
        else:
            incorrect_sound.play()
            pygame.time.delay(500)
    if onion>=0:
        onion-=1
    for punch in red_punches:
        if cookie==-1:
            pygame.draw.polygon(window,(250,160,0),Rpunch_location)
            pygame.draw.rect(window,(255,0,0),Rhand)
            pygame.draw.rect(window,(250,160,0),Rfist)
            red_punches.remove(punch)
            pygame.display.update()
            cookie=8
    if cookie>-1:
        cookie-=1
    if flip==0:
        if cookie>-1:
            if Rpunch_location[1]<
        if onion>-1:
    if flip==1:
        if cookie>-1:
        if onion>-1:
        
    return onion,cookie


def main(fps,Red_ghost,Blue_ghost,red,blue):
    clock=pygame.time.Clock()
    onion=-1
    cookie=-1
    flip=0
    Red_punches=[]
    Blue_punches=[]
    while fps==60:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fps=61
                pygame.quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_q and len(Red_punches)==0 and cookie ==-1:
                    punch=12
                    Red_punches.append(punch)
                    pygame.mixer.Sound.play(punch_sound)
                if event.key==pygame.K_RCTRL and len(Blue_punches)==0 and onion ==-1:
                    punch=12
                    Blue_punches.append(punch)
                    pygame.mixer.Sound.play(punch_sound)
        keys=pygame.key.get_pressed()
        if flip==0:
            Rpunch_location=((red.x+110,red.y+55),(red.x+110,red.y+62),(red.x+125,red.y+62),(red.x+125,red.y+67),(red.x+145,red.y+67),(red.x+145,red.y+50),(red.x+125,red.y+50),(red.x+125,red.y+55))
            Bpunch_location=((blue.x-10,blue.y+55),(blue.x-10,blue.y+62),(blue.x-25,blue.y+62),(blue.x-25,blue.y+67),(blue.x-45,blue.y+67),(blue.x-45,blue.y+50),(blue.x-25,blue.y+50),(blue.x-25,blue.y+55))
            Bx=blue.x-24
            By=blue.y+55
            Bhand=pygame.Rect(Bx,By,15,8)
            Bx=blue.x-34
            By=blue.y+46
            Bfist=pygame.Rect(Bx,By,10,4)
            Rx=red.x+110
            Ry=red.y+55
            Rhand=pygame.Rect(Rx,Ry,15,8)
            Rx=red.x+125
            Ry=red.y+46
            Rfist=pygame.Rect(Rx,Ry,10,4)
        elif flip ==1:
            Rpunch_location=((red.x-16,red.y+55),(red.x-16,red.y+62),(red.x-31,red.y+62),(red.x-31,red.y+67),(red.x-51,red.y+67),(red.x-51,red.y+50),(red.x-31,red.y+50),(red.x-31,red.y+55))
            Bpunch_location=((blue.x+116,blue.y+55),(blue.x+116,blue.y+62),(blue.x+131,blue.y+62),(blue.x+131,blue.y+67),(blue.x+151,blue.y+67),(blue.x+151,blue.y+50),(blue.x+131,blue.y+50),(blue.x+131,blue.y+55))
            Bx=blue.x+16+ghost_width
            By=blue.y+55
            Bhand=pygame.Rect(Bx,By,15,8)
            Bx=blue.x+31+ghost_width
            By=blue.y+46
            Bfist=pygame.Rect(Bx,By,10,4)
            Rx=red.x-30#+ghost_width
            Ry=red.y+55
            Rhand=pygame.Rect(Rx,Ry,15,8)
            Rx=red.x-40#+ghost_width
            Ry=red.y+46
            Rfist=pygame.Rect(Rx,Ry,10,4)
        
        onion,cookie=handle_punches(Blue_punches,Red_punches,Rpunch_location,Bpunch_location,onion,cookie,Rhand,Bhand,Rfist,Bfist,flip)
        ghost_moving(red,blue,keys,ghost_width,ghost_sped,flip,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist)
        flip=draw(red,blue,flip,Red_ghost,Blue_ghost,onion,cookie,Rpunch_location,Bpunch_location,Rhand,Bhand,Rfist,Bfist)


if __name__=="__main__":
    main(fps,Red_ghost,Blue_ghost,red,blue)
