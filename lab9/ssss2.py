import pygame as pg
import sys
import random

pg.init()

W, H = 600, 600

GRID_SIZE = 20 #razmer kletok doski

#cveta
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLACK = (0, 0, 0)

#napravlenya
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

screen = pg.display.set_mode((W, H))
pg.display.set_caption("Zmeyka 2.0")
font = pg.font.Font("lab7/lishnee/MICKEY.TTF", 30)

class Snake:
    def __init__(self):
        self.body = [#pervie 3 chasti zmeyki
            (W // 2, H // 2),
            (W // 2 - GRID_SIZE, H // 2),
            (W // 2 - 2 * GRID_SIZE, H // 2)
        ]
        self.direction = RIGHT #nachalnoe napravlenye
         #flazhki
        self.grow = False
        self.direction_changed = False

    def move(self):
        head_x, head_y = self.body[0] #golova pervye elementy lista body
        dx, dy = self.direction #napravlenya
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop() #if grow false, hvost ubiraiut
        else:
            self.grow = False
        self.direction_changed = False

    def change_direction(self, new_direction):
        opposite = (-self.direction[0], -self.direction[1]) #chtobi bistro ne povorachivatsya
        if new_direction != opposite and not self.direction_changed:
            self.direction = new_direction
            self.direction_changed = True

    def check_collision(self):
        head = self.body[0] #proverka stolknovenya s krayami and hvostom
        return (
            head[0] < 0 or head[0] >= W or
            head[1] < 0 or head[1] >= H or
            head in self.body[1:]
        )

    def draw(self):#vyvesti zmeyu
        for segment in self.body:
            pg.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE), 0, 5)

class Food:#eda
    def __init__(self):
        self.rect = None
        self.size = None
        self.spawn_time = None

    def respawn(self, snake_body):#poyavlenye
        self.size = random.randint(10, 30) #razmer edy
        while True:
            x = random.randint(0, (W - GRID_SIZE)) #coordinaty
            y = random.randint(0, (H - GRID_SIZE)) 
            self.rect = pg.Rect(x, y, self.size, self.size) #hitbox
            collision = False #flazhok chtoby eda ne poyavlyalas na hvoste
            for segment in snake_body:
                segment_rect = pg.Rect(*segment, GRID_SIZE, GRID_SIZE)
                if self.rect.colliderect(segment_rect):
                    collision = True
                    break
            if not collision:
                self.spawn_time = pg.time.get_ticks()#chtoby eda propadala cherez kakoe to vremya
                break

    def draw(self):#vyvesti edu
        pg.draw.rect(screen, RED, self.rect, 0, 40)

class Game:
    def __init__(self):#zgruzhaem nashi classy
        self.snake = Snake()
        self.food = Food()
        self.food.respawn(self.snake.body)
        self.score = 0 #shet
        self.game_over = False #flazhok

    def reset(self):
        self.__init__() #proishodit vse chto bylo v inite

    def update(self):
        if not self.game_over:
            self.snake.move()
            if pg.time.get_ticks() - self.food.spawn_time > 7*1000:
                self.food.respawn(self.snake.body) #esli za eto vremya ne syest edu to ona propadet
            if pg.Rect(*self.snake.body[0], GRID_SIZE, GRID_SIZE).colliderect(self.food.rect):
                self.snake.grow = True
                self.food.respawn(self.snake.body)#esli syest edu to eda vozobnovlyaetsya
                self.score += 1
            if self.snake.check_collision():
                self.game_over = True #esli vrezatsya

    def draw(self):
        colors = [(10,10,10),(0,0,0)]
        for i in range(H//2):
            for j in range(W//2): #doska
                pg.draw.rect(screen, colors[(i+j)%2], (i*GRID_SIZE, j*GRID_SIZE, GRID_SIZE, GRID_SIZE))
        self.snake.draw()
        self.food.draw()
        score_text = font.render(f"Score: {self.score}", True, WHITE)#shet
        screen.blit(score_text, (10, 10))
        if self.game_over:
            game_text = font.render("GAME OVER! Press R", True, WHITE)
            screen.blit(game_text, (W // 2 - 150, H // 2))

clock = pg.time.Clock()
game = Game()
running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
            if event.key == pg.K_r and game.game_over:
                game.reset()
            if event.key in [pg.K_w, pg.K_UP]:
                game.snake.change_direction(UP)
            if event.key in [pg.K_s, pg.K_DOWN]:
                game.snake.change_direction(DOWN)
            if event.key in [pg.K_a, pg.K_LEFT]:
                game.snake.change_direction(LEFT)
            if event.key in [pg.K_d, pg.K_RIGHT]:
                game.snake.change_direction(RIGHT)
    game.update()
    game.draw()
    pg.display.flip()
    clock.tick(5 + game.score)#FPS

pg.quit()
sys.exit()
