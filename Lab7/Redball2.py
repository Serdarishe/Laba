import pygame as pg
import random

pg.init()
W = 1530
H = 860
screens = (W,H)
screen = pg.display.set_mode(screens)
done = False
x = W/2
y = H/2

win = "YOU WIN!"

#random ball
rb_radius = 15
rb_x = random.randint(rb_radius, W - rb_radius)
rb_y = random.randint(rb_radius, H - rb_radius)


cntpoint = 0


font = pg.font.Font('lishnee/MICKEY.TTF',50)
font2 = pg.font.Font('lishnee/MICKEY.TTF',100) 




redcolor = (255,0,0)
blackcol = (0,0,0)

clock = pg.time.Clock()
lsst = [x,y]
radius = 30-5
# maze = pg.image.load('lishnee/mazee.png')
# maze = pg.transform.scale(maze,(700,700))
# nasos = pg.image.load('lishnee/nasos.png')
# nasos = pg.transform.scale(nasos,(70,70))
# winner = pg.image.load('lishnee/winner.jpg')
# winner = pg.transform.scale(winner,screens)
# winner_rect = winner.get_rect(topleft = (310,625))
# def is_wall(position):
#     x, y = position
#     if 0 <= x < 700 and 0 <= y < 700:
#         return screen.get_at((x, y))[:3] == (0, 0, 0)
#     return False

while not done:
        # safe_position = lsst[:]
    pressed = pg.key.get_pressed()
    for event in pg.event.get():
            if pressed[pg.K_ESCAPE] or event.type == pg.QUIT:
                    done = True


    
            
    speed = 10
    if pressed[pg.K_SPACE]:speed = 20
    if pressed[pg.K_w] or pressed[pg.K_UP]: lsst[1] -= speed
    if pressed[pg.K_s] or pressed[pg.K_DOWN]: lsst[1] += speed
    if pressed[pg.K_a] or pressed[pg.K_LEFT]: lsst[0] -= speed
    if pressed[pg.K_d] or pressed[pg.K_RIGHT]: lsst[0] += speed
    screen.fill((255,255,255))
    
    # screen.blit(maze,(0,0))
    # screen.blit(nasos,(310,625))



    if lsst[1] < radius:
        lsst[1] = radius
    if lsst[1] > H - radius:
        lsst[1] = H - radius
    if lsst[0] < radius:
        lsst[0] = radius
    if lsst[0] > W - radius:
        lsst[0] = W - radius

    # pg.draw.rect(screen,blackcol,(310,625,70,70))
            
    pg.draw.circle(screen, (0,0,0), list(lsst),radius)
    pg.draw.circle(screen, redcolor, list(lsst),25-5)
    circle_rect = pg.Rect(lsst[0] - radius, lsst[1] - radius, radius*2 ,radius*2)


    rcircle_rect = pg.Rect(rb_x - rb_radius, rb_y - rb_radius, rb_radius*2 ,rb_radius*2)
    pg.draw.circle(screen,(0,255,50),(rb_x,rb_y),rb_radius)

    if rcircle_rect.colliderect(circle_rect):
        cntpoint += 100
        rb_x = random.randint(rb_radius,W-rb_radius)
        rb_y = random.randint(rb_radius,H-rb_radius)

    countgo = font.render(str(cntpoint),True,blackcol)
    countgo_rect = countgo.get_rect(topright = (1500,50))
    screen.blit(countgo,countgo_rect)

    if cntpoint >= 1000:
            winner = font2.render(win,True,blackcol)
            winner_rect = winner.get_rect(topright = (1050,400))
            screen.blit(winner,winner_rect)
    if cntpoint >= 2000:
            winner = font.render(("That`s enought dude"),True,blackcol)
            winner_rect = winner.get_rect(topright = (1050,600))
            screen.blit(winner,winner_rect)
    # if is_wall(lsst):
    #     lsst = safe_position[:]
    
    # if circle_rect.colliderect(winner_rect):
        #   screen.blit(winner,(0,0))
            
    
    pg.display.flip()
    clock.tick(60)