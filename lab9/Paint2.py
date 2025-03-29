import pygame as pg,sys,math


pg.init()
colors = [pg.Color('white'),pg.Color('red'),pg.Color('blue'),pg.Color('green'),pg.Color('cyan'),pg.Color('pink'),pg.Color('yellow'),pg.Color('black'),]

W,H = 800,600
b_size = 1
collist = pg.image.load('lab9/Collist.png')
collist = pg.transform.scale(collist,(200,603))


clock = pg.time.Clock()

objects = []
draw_circle_mod = False
draw_rect_mod = True
mode = "Rectangle"
draw_erase_mode = False
draw_romb_mod = False
draw_rtriangle_mod = False
draw_etriangle_mod = False
draw_square_mod = False
col = "Yellow"


font = pg.font.Font('lab7/lishnee/DS-DIGIT.TTF',20)
risuiu = False

cur_col = colors[6]
bord_col = colors[7]

# def drawromb(center,size,color,bordersize):
#     points = [
#         (center[0],center[1] - size),
#         (center[0] + size, center[1]),
#         (center[0],center[1] + size),
#         (center[0] - size , center[1])
#     ]
#     pg.draw.polygon(screen,color,points,bordersize)

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
        elif obj[0] == "romb":
            _, points,color,size = obj
            pg.draw.polygon(screen,color,points,size)
        elif obj[0] == "etri":
            _, points, color,size = obj
            pg.draw.polygon(screen,color,points,size)
        elif obj[0] == "rtri":
            _, points, color,size = obj
            pg.draw.polygon(screen,color,points,size)
        elif obj[0] == "square":
            _, points, lenght,color,size = obj
            pg.draw.rect(screen,color,(points,(lenght,lenght)),size)

    if pressed[pg.K_c]:
        mode = "Circle"
        draw_circle_mod = True
        draw_rect_mod = False
        draw_erase_mode =False
        draw_romb_mod = False
        draw_rtriangle_mod = False
        draw_etriangle_mod = False
        draw_square_mod = False

    if pressed[pg.K_r]:
        mode = "Rectangle"
        draw_circle_mod = False
        draw_rect_mod = True
        draw_erase_mode = False
        draw_romb_mod = False
        draw_rtriangle_mod = False
        draw_etriangle_mod = False
        draw_square_mod = False


    if pressed[pg.K_u]:
        mode = "Rhomb"
        draw_circle_mod = False
        draw_rect_mod = False
        draw_erase_mode = False
        draw_romb_mod = True
        draw_rtriangle_mod = False
        draw_etriangle_mod = False
        draw_square_mod = False


    if pressed[pg.K_y]:
        mode = "Right triangle"
        draw_circle_mod = False
        draw_rect_mod = False
        draw_erase_mode = False
        draw_romb_mod = False
        draw_rtriangle_mod = False
        draw_etriangle_mod = True
        draw_square_mod = False

    if pressed[pg.K_t]:
        draw_circle_mod = False
        draw_rect_mod = False
        draw_erase_mode = False
        draw_romb_mod = False
        draw_rtriangle_mod = True
        draw_etriangle_mod = False
        draw_square_mod = False
        mode = "Equilateral triangle"
    if pressed[pg.K_s]:
        mode = "Square"
        draw_circle_mod = False
        draw_rect_mod = False
        draw_erase_mode = False
        draw_romb_mod = False
        draw_rtriangle_mod = False
        draw_etriangle_mod = False
        draw_square_mod = True

    if draw_square_mod:
        if cursor[0] and not risuiu :
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
            end_pos = curssor
            x1, y1 = start_pos
            x2, y2 = end_pos
            lenght = max(abs(x2 - x1),abs(y2-y1))
            left = x1 if x2 >= x1 else x1 - lenght
            top = y1 if y2 >= y1 else y1 - lenght
            

            objects.append(("square", (left, top), lenght, cur_col, b_size))
            # width = curssor[0] - start_pos[0]
            # height = curssor[1] - start_pos[1]

            
            risuiu = False

        
        
        

        if risuiu:
            x1, y1 = start_pos
            x2, y2 = curssor
            lenght = max(abs(x2 - x1),abs(y2-y1))
            left = x1 if x2 >= x1 else x1 - lenght
            top = y1 if y2 >= y1 else y1 - lenght
            # width = abs(x2 - x1)
            
            pg.draw.rect(screen, cur_col, (left, top, lenght, lenght), b_size)


    if draw_rtriangle_mod:
        if cursor[0] and not  risuiu:
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
            end_pos = curssor
            x1, y1 = start_pos
            x2,y2 = end_pos
            points = [
                ((x1+x2)//2,y1),
                (x2,y2),
                (x1,y2)
            ]
            objects.append(("rtri", points,cur_col,b_size))
            risuiu = False
        if risuiu:
            x1,y1 = start_pos
            end_pos = curssor
            x2, y2 = end_pos
            points = [
                ((x1+x2)//2,y1),
                (x2,y2),
                (x1,y2)
            ]
            pg.draw.polygon(screen,cur_col,points,b_size)
    
    if draw_etriangle_mod:
        if cursor[0] and not  risuiu:
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
            end_pos = curssor
            x1, y1 = start_pos
            x2,y2 = end_pos
            points = [
                (x1,y1),
                (x2,y2),
                (x1,y2)
            ]
            objects.append(("etri", points,cur_col,b_size))
            risuiu = False
        if risuiu:
            x1,y1 = start_pos
            end_pos = curssor
            x2, y2 = end_pos
            points = [
                (x1,y1),
                (x2,y2),
                (x1,y2)
            ]
            pg.draw.polygon(screen,cur_col,points,b_size)



    if draw_romb_mod:
        if cursor[0] and not risuiu:
            risuiu = True
            start_pos = curssor
        elif not cursor[0] and risuiu:
            end_pos = curssor
            x1,y1 = start_pos
            x2,y2 = end_pos
            size = min(abs(x2 - x1), abs(y2 - y1)) // 2
            points = [
                (x1, y1 - size), 
                (x1 + size, y1),
                (x1, y1 + size), 
                (x1 - size, y1)
            ]
            
            objects.append(("romb",points,cur_col,b_size))
            risuiu = False

        if risuiu:
            
            x1, y1 = start_pos
            end_pos = curssor
            x2, y2 = end_pos
            size = min(abs(x2 - x1), abs(y2 - y1)) // 2  # Размер ромба
            points = [
                (x1, y1 - size), 
                (x1 + size, y1),
                (x1, y1 + size), 
                (x1 - size, y1)
            ]

            pg.draw.polygon(screen,cur_col,points,b_size)


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
            # width = curssor[0] - start_pos[0]
            # height = curssor[1] - start_pos[1]

            
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

    
            pg.draw.circle(screen, colors[7], now_pos, b_size)
    if pressed[pg.K_KP_PLUS] and b_size < 100:
        b_size += 1
        
    if pressed[pg.K_KP_MINUS] and b_size > 1:
        b_size -= 1
    pg.draw.circle(screen,bord_col,curssor,b_size+2)
    pg.draw.circle(screen,cur_col,curssor,b_size)

    
    if pressed[pg.K_KP_1] or pressed[pg.K_1]:
        col = "White"
        cur_col = colors[0]
        bord_col = colors[7]
    if pressed[pg.K_KP_2] or pressed[pg.K_2]:
        col = "Red"
        cur_col = colors[1]
        bord_col = colors[7]
    if pressed[pg.K_KP_3] or pressed[pg.K_3]:
        col = "Blue"
        cur_col = colors[2]
        bord_col = colors[7]
    if pressed[pg.K_KP_4] or pressed[pg.K_4]:
        col = "Green"
        cur_col = colors[3]
        bord_col = colors[7]
    if pressed[pg.K_KP_5] or pressed[pg.K_5]:
        col = "Cyan"
        cur_col = colors[4]
        bord_col = colors[7]
    if pressed[pg.K_KP_6] or pressed[pg.K_6]:
        col = "Pink"
        cur_col = colors[5]
        bord_col = colors[7]
    if pressed[pg.K_KP_7] or pressed[pg.K_7]:
        col = "Yellow"
        cur_col = colors[6]
        bord_col = colors[7]
    if pressed[pg.K_KP_0] or pressed[pg.K_0]:
        col = "Black"
        draw_erase_mode = True
        draw_circle_mod = False
        draw_rect_mod = False
        draw_romb_mod = False
        draw_rtriangle_mod = False
        draw_etriangle_mod = False
        draw_square_mod = False
        mode = "Eraser"
        bord_col = colors[0]
        cur_col = colors[7]
    collor = font.render(f"Color: {col}",True,(0,255,0))
    modee = font.render(f"Mode: {mode}",True,(0,255,0))
    screen.blit(collor,(400,20))
    screen.blit(modee,(20,20))
    screen.blit(collist,(600,-2))
    clock.tick(200)
    pg.display.update()