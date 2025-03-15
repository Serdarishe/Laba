import pygame as pg
import sys

pg.init()
W, H = 600, 600
screen = pg.display.set_mode((W, H))
screen.fill((255,255,255))
logo = pg.image.load('lishnee/startscreen.png')
logo = pg.transform.scale(logo,(400,400))
screen.blit(logo , (100,50))
mus_list = ['lishnee/Baiqa.mp3','lishnee/My_Universe.mp3','lishnee/bonde_do_brunao.mp3','lishnee/Astalavista.mp3','lishnee/Ankaranin_baglari.mp3','lishnee/Dudu.mp3']
cov_list = [pg.image.load('lishnee/qairosh.png'),pg.image.load('lishnee/qairosh1.png'),pg.image.load('lishnee/bruno.png'),pg.image.load('lishnee/entrasta.png'),pg.image.load('lishnee/ankara.png'),pg.image.load('lishnee/Tarkan.png')]


pg.display.set_caption('Musica')

play_rect = pg.Rect(255,490,75,75)
back_rect = pg.Rect(145,490,52,52)
next_rect = pg.Rect(400,490,52,52)

current_index = 0
def play_music(index):
    if 0 <= index < len(mus_list):
        pg.mixer.music.load(mus_list[index])
        pg.mixer.music.play()
        cur_cov = pg.transform.scale(cov_list[index],(400,400))
        screen.blit(cur_cov,(100,50))



while True:
    pressed = pg.key.get_pressed()
    mouspressed = pg.mouse.get_pressed()
    mouse_pos = pg.mouse.get_pos()
    for event in pg.event.get():
        if (event.type == pg.QUIT) or pressed[pg.K_ESCAPE]:
            pg.quit()
            sys.exit()
        if pressed[pg.K_SPACE]:
            if pg.mixer.music.get_busy():
                pg.mixer.music.pause()
            else:
                pg.mixer.music.unpause()    
        if pressed[pg.K_RIGHT]:
            current_index = (current_index + 1)%len(mus_list)
            play_music(current_index)
        if pressed[pg.K_LEFT]:
            current_index = (current_index - 1)%len(mus_list)
            play_music(current_index)

            
        for i in range(10):
            if pressed[pg.K_0 + i]:
                if i == 1:
                    current_index = 0
                    play_music(0)
                if i == 2:
                    current_index = 1
                    play_music(1)
                if i == 3:
                    current_index = 2
                    play_music(2)
                if i == 4:
                    current_index = 3
                    play_music(3)
                if i == 5:
                    current_index = 4
                    play_music(4)
                if i == 6:
                    current_index = 5
                    play_music(5)

        if mouspressed[0]:
            if play_rect.collidepoint(mouse_pos):
                if pg.mixer.music.get_busy():
                    pg.mixer.music.pause()
                else:
                    pg.mixer.music.unpause()  
        if mouspressed[0]:
            if back_rect.collidepoint(mouse_pos):
                current_index = (current_index - 1)%len(mus_list)
                play_music(current_index)
        if mouspressed[0]:
            if next_rect.collidepoint(mouse_pos):
                current_index = (current_index + 1)%len(mus_list)
                play_music(current_index)
    
    coverinterface = pg.image.load('lishnee/interfacee.png')
    coverinterface = pg.transform.scale(coverinterface,(600,600))
    screen.blit(coverinterface,(0,0))
    


    pg.display.update()
    