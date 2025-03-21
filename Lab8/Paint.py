import pygame as pg,sys

pg.init()
colors = [pg.Color('white'),pg.Color('red'),pg.Color('blue'),pg.Color('green'),pg.Color('cyan'),pg.Color('pink'),pg.Color('yellow'),pg.Color('black'),]

W,H = 800,600
b_size = 1
collist = pg.image.load('Collist.png')
collist = pg.transform.scale(collist,(200,603))


clock = pg.time.Clock()

objects = []
draw_circle_mod = False
draw_rect_mod = True
draw_erase_mode = False


risuiu = False

cur_col = colors[6]
bord_col = colors[7]

screen = pg.display.set_mode((W,H))

while True:
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
    pressed = pg.key.get_pressed()
    curssor = pg.mouse.get_pos()
    cursor = pg.mouse.get_pressed()
    # tochhka = pg.Surface((10,10))
    # tochhka.fill((255,0,0))
    screen.fill(colors[7])
    

    for obj in objects:
        if obj[0] == "rect":
            _, pos, w, h, color, size = obj
            pg.draw.rect(screen, color, (pos[0], pos[1], w, h), size)
        elif obj[0] == "circle":
            _, center, radius, color, size = obj
            pg.draw.circle(screen, color, center, radius, size)
        elif obj[0] == "erase":
            _, pos, size = obj
            pg.draw.circle(screen, colors[7], pos, size)

    if pressed[pg.K_c]:
        draw_circle_mod = True
        draw_rect_mod = False
        draw_erase_mode =False
    if pressed[pg.K_r]:
        draw_circle_mod = False
        draw_rect_mod = True
        draw_erase_mode = False

    if draw_rect_mod:
        if cursor[0] and not risuiu :
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
            end_pos = curssor
            x1, y1 = start_pos
            x2, y2 = end_pos

            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)

            objects.append(("rect", (left, top), width, height, cur_col, b_size))
            width = curssor[0] - start_pos[0]
            height = curssor[1] - start_pos[1]

            
            risuiu = False

        
        
        

        if risuiu:
            x1, y1 = start_pos
            x2, y2 = curssor
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            pg.draw.rect(screen, cur_col, (left, top, width, height), b_size)
    if draw_circle_mod:
        if cursor[0] and not risuiu :
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
           
            x1, y1 = start_pos
            x2, y2 = curssor
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            center = (left + width // 2, top + height // 2)
            radius = max(width, height) // 2
            pg.draw.circle(screen, cur_col, center, radius, b_size)
            
            objects.append(("circle", center, radius, cur_col, b_size))
            width = curssor[0] - start_pos[0]
            height = curssor[1] - start_pos[1]
                    
            risuiu = False

        
            
        

        if risuiu:
            x1, y1 = start_pos
            x2, y2 = curssor
            left = min(x1, x2)
            top = min(y1, y2)
            width = abs(x2 - x1)
            height = abs(y2 - y1)
            center = (left + width // 2, top + height // 2)
            radius = max(width, height) // 2
            pg.draw.circle(screen, cur_col, center, radius, b_size)
    if draw_erase_mode:
        now_pos = curssor
        
        if cursor[0]:
            


            pg.draw.circle(screen,colors[7],now_pos,b_size)
            objects.append(("erase", now_pos, b_size))

    
            pg.draw.circle(screen, colors[7], pos, size)
    if pressed[pg.K_KP_PLUS] and b_size < 100:
        b_size += 1
        
    if pressed[pg.K_KP_MINUS] and b_size > 1:
        b_size -= 1
    pg.draw.circle(screen,bord_col,curssor,b_size+2)
    pg.draw.circle(screen,cur_col,curssor,b_size)

    
    if pressed[pg.K_KP_1] or pressed[pg.K_1]:
        cur_col = colors[0]
        bord_col = colors[7]
    if pressed[pg.K_KP_2] or pressed[pg.K_2]:
        cur_col = colors[1]
        bord_col = colors[7]
    if pressed[pg.K_KP_3] or pressed[pg.K_3]:
        cur_col = colors[2]
        bord_col = colors[7]
    if pressed[pg.K_KP_4] or pressed[pg.K_4]:
        cur_col = colors[3]
        bord_col = colors[7]
    if pressed[pg.K_KP_5] or pressed[pg.K_5]:
        cur_col = colors[4]
        bord_col = colors[7]
    if pressed[pg.K_KP_6] or pressed[pg.K_6]:
        cur_col = colors[5]
        bord_col = colors[7]
    if pressed[pg.K_KP_7] or pressed[pg.K_7]:
        cur_col = colors[6]
        bord_col = colors[7]
    if pressed[pg.K_KP_0] or pressed[pg.K_0]:
        draw_erase_mode = True
        draw_circle_mod = False
        draw_rect_mod = False
        bord_col = colors[0]
        cur_col = colors[7]
    screen.blit(collist,(600,-2))
    clock.tick(200)
    pg.display.update()