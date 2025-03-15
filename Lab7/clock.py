import pygame as pg
import datetime as dt
import sys
pg.init()
W = 600
H = 600
clock = pg.time.Clock()
screen = pg.display.set_mode((W,H))
mickey = pg.image.load('lishnee/clock.png')
minhand = pg.image.load('lishnee/min_hand.png')
sechand = pg.image.load('lishnee/sec_hand.png')
clocksec = pg.image.load('lishnee/strelka.png')
clocksec = pg.transform.scale(clocksec,(500,80))

font = pg.font.Font('lishnee/DS-DIGIT.TTF',40)
font2 = pg.font.Font('lishnee/MICKEY.TTF',70)
colorforbg = (30,30,30)
colorfortext = (0,255,0)

def rotate(surf, img, times, angle):
    rot_img = pg.transform.rotate(img, -(times % 60) * 6 + angle)
    new_img = rot_img.get_rect(center = (300, 300))
    surf.blit(rot_img, new_img)
    
pg.display.set_caption('Clock')

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
                
                pg.quit()
                sys.exit()
    screen.blit(mickey,(0,0))
    pg.draw.rect(screen,(0,0,0),(10,10,200,50))#fon cifrovih chasov

    

    noww = dt.datetime.now()
    #lishnee cifrovoy
    current_time = noww.strftime("%H:%M:%S")
    text_surface = font.render(current_time, True, colorfortext)
    text_rect = text_surface.get_rect(center=(110, 35))
    screen.blit(text_surface, text_rect)
    #lishnee 12 chasovoy
    # current_time1 = noww.strftime("%I %p")
    # text_surface1 = font2.render(current_time1, True, (0,0,0))
    # text_rect1 = text_surface1.get_rect(center=(300, 300))
    # screen.blit(text_surface1, text_rect1)
    
    minutess = noww.minute
    hourss = noww.hour
    secundes = noww.second
    rotate(screen, clocksec, secundes,90 )
    rotate(screen, sechand, minutess,57 )
    rotate(screen, minhand, hourss * 5 + minutess/12,-52 )

    print(int(hourss*5+minutess/12))
    print(minutess)
   

    pg.display.update()


        
        
        
        

        
    pg.display.flip()
    clock.tick(60)

