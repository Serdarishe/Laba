import pygame as pg
import sys , random , time


pg.init()
W,H = 600,800 #razmer okna
SPEED = 5 #Skorost monet
enSPEED = 8 #Skorost enemi

napravo = -20 #na skolko gradusov povarachivat
nalevo = 20

global kpressed
frsttime = True
hp = pg.image.load('lab8/hp.png')
hp = pg.transform.scale(hp,(40,40))

carr = pg.image.load('lab8/car.png')


road_y = 0 #dlya animacii fona



#fonovie zvuki
pg.mixer.Sound('lab8/nachalo.mp3').play()
pg.mixer.music.load('lab8/fonovaya.mp3')

CARSPEED = 10 #skorost mashini
screen = pg.display.set_mode((W,H)) #okno


clock = pg.time.Clock() #dlya fps

game_over = False #chtobi ostanovit igru

#cveta
blackcol = (0,0,0)
redcol = (255,0,0)
grencol = (0,255,0)
blucol = (0,0,255)
whitecol = (255,255,255)

#doroga
road = pg.image.load('lab8/road.jpg')
road = pg.transform.scale(road,(600,800))

#shrift i zagalovok
font = pg.font.Font('lab7/lishnee/MICKEY.TTF',60)
small_font = pg.font.Font('lab7/lishnee/MICKEY.TTF',30)
# win = font.render("YOU WIN!",True,blackcol)
pg.display.set_caption("Igra")

#shitaem monetki
cnt = 0



#daem class monetam
class Coin(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        if not game_over:

            self.image = pg.image.load('lab8/coin.png') #zagruzhaem ego risunok
            self.coinsize = random.choice([40,50,60,70,80])
            self.image = pg.transform.scale(self.image,(self.coinsize,self.coinsize)) #menyaem ego na podhodyashi nam razmer
            self.rect = self.image.get_rect() #hitbox
            self.rect.center = (random.randint(50,W - 50),-50)#nachalnaya posicia
           

    def move(self):
        if not game_over:
            self.rect.move_ip(0,SPEED)#nashi monety letyat vniz 
            if (self.rect.bottom > H):#obratno naverh
                self.rect.top = 0
                self.rect.center = (random.randint(50,550),-50)#gde nibud

    def draw(self, surface):
        surface.blit(self.image, self.rect)#vyvodinm ih

class Enemy(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        if not game_over:
            self.orig_image = pg.image.load('lab9/car.png') #risunok zlyh mashin
            self.image = self.orig_image
            self.image = pg.transform.rotate(self.image,180) #oni prosto smotreli naverh

            self.rect = self.image.get_rect()#ih hitboxes
            self.rect.center = (random.randint(60,W-60),-120) #gde oni poyavlyayutsya

    def move(self):
        if not game_over:
            self.rect.move_ip(0,enSPEED) #dvizhutsya po y i x
            if self.rect.top > W+240:
                self.rect.bottom = -60
                self.rect.center = (random.randint(60,W-60),-120)

    def draw(self,surface):
        surface.blit(self.image,self.rect)#vyvesti na ekran

#daem class mashinke
class Car(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.orig_image = pg.image.load('lab8/carr.png')#zagruzhaem
        self.image = self.orig_image
        
        
        self.rect = self.image.get_rect()#ego hitbox
        self.rect.center = (160,650)#gde my poyavlyaemsya
        self.left_sound_played = False#eto dlya stolknvenya s borderom
        self.right_sound_played = False 

        self.rotation_speed = 5 #na skolko gradusov povorachivat
        self.return_speed = 2 #obratno na mesto gradus
        self.cnthp = 5 #hitpoints

        self.angle = 0 #nachalniy gradus

    def rotate(self,nav):#menyat gradus
        self.angle += nav 
        self.angle = max(-20,min(20,self.angle))
        self.image = pg.transform.rotate(self.orig_image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
    def move(self):
        if not game_over:
        
        
            pressed = pg.key.get_pressed()#chtoby rabotat s klaviaturoi

            if self.rect.left > 32: #srazu granica i dvizhenye
                if pressed[pg.K_LEFT]:        
                    self.rect.move_ip(-CARSPEED,0)
                    self.rotate(self.rotation_speed)
                    
            if self.rect.left > 34:
                self.left_sound_played = False#chtoby zvuk ne tupil

            if self.rect.top > -10:
                if pressed[pg.K_UP]:        
                        self.rect.move_ip(0,-CARSPEED)

            if self.rect.bottom < H+10:
                if pressed[pg.K_DOWN]:        
                        self.rect.move_ip(0,CARSPEED)

            if self.rect.left <= 33 and not self.left_sound_played:#zvuk stolknovenya s borderom
                pg.mixer.Sound('lab8/stukk.mp3').play()
                self.left_sound_played = True
                self.cnthp -= 1
            
                
            if self.rect.right < W-32:
                if pressed[pg.K_RIGHT]:
                    self.rect.move_ip(CARSPEED,0)
                    self.rotate(-self.rotation_speed)

            

            if self.rect.right < W-34:
                self.right_sound_played = False

            if self.rect.right >= W - 33 and not self.right_sound_played:
                pg.mixer.Sound('lab8/stukk.mp3').play()
                self.right_sound_played = True
                self.cnthp -= 1
            else:
                if self.angle > 0:
                    self.rotate(-self.return_speed)
                elif self.angle < 0:
                    self.rotate(self.return_speed)
    def draw(self,surface):
        surface.blit(self.image,self.rect)#vyvodim na ekran

cargo = Car() #sozdaem object kotoriy prinimaet nashi svoistva classa
monety = Coin()
enemi = Enemy()
coins = pg.sprite.Group()#chtoby bylo legche imi upravlyat
coins.add(monety)
enemies = pg.sprite.Group()
enemies.add(enemi)

all_sprites = pg.sprite.Group()
all_sprites.add(monety)
all_sprites.add(cargo)
all_sprites.add(enemi)

scorost = pg.USEREVENT + 1 #dobavlyaem sobytiye
pg.time.set_timer(scorost,1000)#chtobi uvelichit skorost

if not game_over:
    pg.mixer.music.play(-1)
    pg.mixer.music.set_volume(0.1) #zvuk holostogo hoda
    


while True:
    
    pressed = pg.key.get_pressed()
   
    for event in pg.event.get():
        

        if event.type == pg.QUIT or pressed[pg.K_ESCAPE]:#vyhod
            pg.quit()
            sys.exit()

    # cargo.update()
    # monety.move()

    # screen.fill(whitecol)#po suti ne nuzhno
  
    # cargo.draw(screen)
    if not game_over:
        
        road_y += CARSPEED  #skorost fona
        if road_y >= H:
            road_y = 0
    
    
    
    screen.blit(road, (0, road_y))#fon
    screen.blit(road, (0, road_y - H))

    

    for entity in all_sprites:
        screen.blit(entity.image,entity.rect)#rabota s temi gruppami
        entity.move()

    

    sobrannye_monety = pg.sprite.spritecollide(cargo,coins,dokill=True)#checkaem stolknovenye monet i mashiny

    if not game_over:
        if pg.sprite.spritecollideany(cargo,enemies): #stolknoveniye s protivnikom
            
            cargo.cnthp = 0
            
            pg.mixer.Sound('lab9/avaria.mp3').play()
    if frsttime:        
        new_coin = monety
        frsttime = False
    if sobrannye_monety:
        pg.mixer.Sound('lab8/coinsound.mp3').play()#zvuk sbora monet
        if event.type == scorost:
            SPEED += 2  #skorosti mashiny i monet
            CARSPEED += 1
            enSPEED += 2
        #posle dokill u nas propadaut monety nam nuzhny novye
        
        if new_coin.coinsize == 40:
            cnt += 2 #shitalka
        if new_coin.coinsize == 50:
            cnt += 4 #shitalka
        if new_coin.coinsize == 60:
            cnt += 6 #shitalka
        if new_coin.coinsize == 70:
            cnt += 8 #shitalka
        if new_coin.coinsize == 80:
            cnt += 10 #shitalka
        new_coin = Coin()

        coins.add(new_coin)
        all_sprites.add(new_coin)

    
#fon dlya sheta
    pg.draw.rect(screen,blackcol,(W-160,10,120,70),0,20,20,20,100)
    pg.draw.rect(screen,whitecol,(W-150,20,100,50),0,10,10,10,60)
    
    
    scores = small_font.render(str(cnt),True,blackcol)#shet
    screen.blit(scores,(W-120,32))

    if cargo.cnthp == 0 and not game_over: #esli proigral
        
        
        pg.mixer.Sound('lab9/lose.mp3').play()
        game_over = True
    

    if cnt >=  100 and not game_over:
        pg.mixer.Sound('lab8/winnn.mp3').play()#zvuk pobedy
        game_over = True

    if game_over:
        if cnt >= 100:
            pg.draw.rect(screen,blackcol,(W//2 -215,H//2-45-40,450,150),0,50)
            pg.draw.rect(screen,whitecol,(W//2 -190,H//2-20-40,400,100),0,30)#fon vyveski you win
            pg.mixer.music.stop() #ostanovka zvuka mashiny
            win_text = font.render("YOU WIN!", True, (0, 0, 0))#zagruzhaem text
            screen.blit(win_text, (W//2 -170, H//2-40))#vyvod texta
            pg.time.set_timer(scorost, 0)#ostanavlivaem timer
        else:
            
            pg.draw.rect(screen,blackcol,(W//2 -215-10,H//2-45-40,470,150),0,50)
            pg.draw.rect(screen,whitecol,(W//2 -190-10,H//2-20-40,420,100),0,30)
            pg.mixer.music.stop()
            lose_text = font.render("YOU LOSE!", True, (0, 0, 0))#zagruzhaem text
            screen.blit(lose_text, (W//2 -170-10    , H//2-40))
            pg.time.set_timer(scorost, 0)
            

    
        


        
    else:
        all_sprites.update() #po prikolu
        
    screen.blit(hp,(500,100))
    HP = small_font.render(f"{str(cargo.cnthp)}x",True,whitecol)
    screen.blit(HP,(450,105))
    
    clock.tick(60)#fps
    pg.display.update()