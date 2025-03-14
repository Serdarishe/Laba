import pygame as pg

pg.init()
W = 700
H = 700
screens = (W,H)
screen = pg.display.set_mode(screens)
done = False
is_blue = True
x = 350
y = 350
redcolor = (255,0,0)
blackcol = (0,0,0)
clock = pg.time.Clock()
lsst = [x,y]
radius = 30-5
# maze = pg.image.load('lab7/mazee.png')
# maze = pg.transform.scale(maze,(700,700))
nasos = pg.image.load('lab7/nasos.png')
nasos = pg.transform.scale(nasos,(70,70))
winner = pg.image.load('lab7/winner.jpg')
winner = pg.transform.scale(winner,screens)
winner_rect = nasos.get_rect(topleft = (310,625))
# def is_wall(position):
#     x, y = position
#     if 0 <= x < 700 and 0 <= y < 700:
#         return screen.get_at((x, y))[:3] == (0, 0, 0)
#     return False

while not done:
        safe_position = lsst[:]
        
        for event in pg.event.get():
                if event.type == pg.QUIT:
                        done = True
        
        pressed = pg.key.get_pressed()
        if pressed[pg.K_w]: lsst[1] -= 20
        if pressed[pg.K_s]: lsst[1] += 20
        if pressed[pg.K_a]: lsst[0] -= 20
        if pressed[pg.K_d]: lsst[0] += 20
        screen.fill((255,255,255))
        
        # screen.blit(maze,(0,0))
        screen.blit(nasos,(310,625))


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
        # if is_wall(lsst):
        #     lsst = safe_position[:]
        
        if circle_rect.colliderect(winner_rect):
              screen.blit(winner,(0,0))
              
        
        pg.display.flip()
        clock.tick(60)