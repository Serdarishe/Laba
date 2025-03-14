import pygame as pg

pg.init()
screen = pg.display.set_mode((600,600))
mickey = pg.image.load('lab7/clock.png')
mickey = pg.transform.scale(mickey,(600,600))
done = False
clock = pg.time.Clock()
def blitRotate(surf,image,pos,OriginPos,angle):
    image_rect = image.get_rect(topleft = (pos[0] - OriginPos[0], pos[1] - OriginPos[1]))
while not done:
    for event in pg.event.get():

        screen.blit(mickey,(0,0))
        

        
        if event.type == pg.QUIT:
            done = True

        pg.display.flip()

