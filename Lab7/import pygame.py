import pygame

pygame.init()
screen = pygame.display.set_mode((700, 700))
done = False
is_blue = True
x = 345
y = 50
redcolor = (255,0,0)
blackcol = (0,0,0)
clock = pygame.time.Clock()
lsst = [x,y]
radius = 30
# maze = pygame.image.load('lab7/mazee.png')
# maze = pygame.transform.scale(maze,(700,700))
nasos = pygame.image.load('lab7/nasos.png')
nasos = pygame.transform.scale(nasos,(70,70))
winner = pygame.image.load('lab7/winner.jpg')
winner = pygame.transform.scale(winner,(700,700))
winner_rect = nasos.get_rect(topleft = (310,625))
# def is_wall(position):
#     x, y = position
#     if 0 <= x < 700 and 0 <= y < 700:
#         return screen.get_at((x, y))[:3] == (0, 0, 0)
#     return False

while not done:
        safe_position = lsst[:]
        
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w]: lsst[1] -= 10
        if pressed[pygame.K_s]: lsst[1] += 10
        if pressed[pygame.K_a]: lsst[0] -= 10
        if pressed[pygame.K_d]: lsst[0] += 10
        screen.fill((255,255,255))
        
        # screen.blit(maze,(0,0))
        screen.blit(nasos,(310,625))


        if lsst[1] < 30:
            lsst[1] = 30
        if lsst[1] > 670:
            lsst[1] = 670
        if lsst[0] < 30:
            lsst[0] =30
        if lsst[0] > 670:
            lsst[0] = 670

        # pygame.draw.rect(screen,blackcol,(310,625,70,70))
                
        pygame.draw.circle(screen, (0,0,0), list(lsst),30)
        pygame.draw.circle(screen, redcolor, list(lsst),25)
        circle_rect = pygame.Rect(lsst[0] - radius, lsst[1] - radius, radius*2 ,radius*2)
        # if is_wall(lsst):
        #     lsst = safe_position[:]
        
        if circle_rect.colliderect(winner_rect):
              screen.blit(winner,(0,0))
              
        
        pygame.display.flip()
        clock.tick(60)