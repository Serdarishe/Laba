import pygame as pg
import sys
import random
import psycopg2 as ps

# Подключение к базе данных
conn = ps.connect(
    dbname="postgres",
    user="postgres",
    password="Dund@r07",
    host="localhost"
)
cur = conn.cursor()

# Создаем таблицу для хранения рекордов, если она еще не существует
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL UNIQUE
    );
""")
cur.execute("""
    CREATE TABLE IF NOT EXISTS user_score (
        id SERIAL PRIMARY KEY,
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
        score INT NOT NULL,
        level INT NOT NULL,
        speed INT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")

conn.commit()

pg.init()

# Настройки экрана и шрифта
W, H = 600, 600
GRID_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
UP = (0, -1) 
DOWN = (0, 1) 
LEFT = (-1, 0) 
RIGHT = (1, 0)
font = pg.font.Font('lab10/Oswald.ttf', 30)
clock = pg.time.Clock()

screen = pg.display.set_mode((W, H))
pg.display.set_caption("Zmeyka 2.0")

# Класс для игры
class Snake:
    def __init__(self):
        self.body = [(W // 2, H // 2), (W // 2 - GRID_SIZE, H // 2), (W // 2 - 2 * GRID_SIZE, H // 2)]
        self.direction = RIGHT
        self.grow = False
        self.direction_changed = False

    def move(self):
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx * GRID_SIZE, head_y + dy * GRID_SIZE)
        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        self.direction_changed = False

    def change_direction(self, new_direction):
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite and not self.direction_changed:
            self.direction = new_direction
            self.direction_changed = True

    def check_collision(self):
        head = self.body[0]
        
        return (
            head[0] < 0 or head[0] >= W or
            head[1] < 0 or head[1] >= H or
            head in self.body[1:]
        )
    

    def draw(self):
        for segment in self.body:
            pg.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE), 0, 5)

class Food:
    def __init__(self):
        self.rect = None
        self.size = None
        self.spawn_time = None
        

    def respawn(self, snake_body,walls):
        self.size = random.choice([10,20,30])
        self.weidth = self.size
        while True:
            x = random.randint(0, (W - GRID_SIZE))
            y = random.randint(0, (H - GRID_SIZE))
            self.rect = pg.Rect(x, y, self.weidth, self.weidth)
            collision = False
            for segment in snake_body:
                segment_rect = pg.Rect(*segment, GRID_SIZE, GRID_SIZE)
                if self.rect.colliderect(segment_rect):
                    collision = True
                    break

            for wall in walls:
                if self.rect.colliderect(wall):
                    collision = True
                    break
            if not collision:
                self.spawn_time = pg.time.get_ticks()
                break

    def draw(self):
        pg.draw.rect(screen, RED, self.rect, 0, 40)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.level = 1
        self.walls = self.get_level_walls(self.level) 
        self.food.respawn(self.snake.body,self.walls)
        self.score = 0
        self.game_over = False
        
        self.speeed = 5
         # Получаем стены для уровня

    def get_level_walls(self, level):
        """Возвращает стены в зависимости от уровня"""
        walls = []
        if level == 1:
            walls = [
                pg.Rect(200, 400, 200, 20),  # Пример стены
                pg.Rect(200, 200, 200, 20)
            ]
        elif level == 2:
            # Стены для уровня 2
            walls = [
                pg.Rect(200, 400, 200, 20),  # Пример стены
                pg.Rect(200, 200, 200, 20),
                pg.Rect(200, 325, 20, 75),  # Пример стены
                pg.Rect(200, 200, 20, 75),
                pg.Rect(400, 325, 20, 95),  # Пример стены
                pg.Rect(400, 200, 20, 75)
            ]
        elif level >= 3:
            # Стены для уровня 3
            walls = [
                pg.Rect(100-20+200-20, 40, 100, 100),
                pg.Rect(100-20, 40, 100, 100),
                pg.Rect(100-20+200-20, 40+200, 100, 100),
                pg.Rect(100-20, 40+200, 100, 100),
                
                pg.Rect(100-20+200-20, 40+400, 100, 100),
                pg.Rect(100-20, 40+400, 100, 100),
                pg.Rect(100-20+180+180, 40+400, 100, 100),
                pg.Rect(100-20+180+180, 40+200, 100, 100),
                pg.Rect(100-20+180+180, 40, 100, 100)
                
                
            ]
        return walls

    def check_wall_collision(self):
        """Проверка столкновения c стенами"""
        for wall in self.walls:
            if pg.Rect(*self.snake.body[0], GRID_SIZE, GRID_SIZE).colliderect(wall):
                self.game_over = True
                self.save_score(username, self.score, self.level, self.speeed)
                break

    def save_score(self, username, score, level, speed):
    # Получаем текущий счёт игрока из базы данных
        cur.execute("SELECT id FROM users WHERE username = %s", (username,))
        user_id = cur.fetchone()  # Возвращает кортеж (id,) или None

        if user_id is None:
            # Если игрока нет в базе данных, добавляем нового
            cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id", (username,))
            user_id = cur.fetchone()[0]  # Получаем id нового пользователя

        # Сохраняем результаты в таблицу user_score
        cur.execute(
            "INSERT INTO user_score (user_id, score, level, speed) VALUES (%s, %s, %s, %s)",
            (user_id, score, level, speed)
        )
        
        conn.commit()

    

    def update(self):
        if not self.game_over:
            self.snake.move()
            if pg.time.get_ticks() - self.food.spawn_time > 7 * 1000:
                self.food.respawn(self.snake.body,self.walls)

            # Проверяем, не столкнулась ли еда со стенами
            # if self.food.rect.collidelist(self.walls):
            #     self.food.respawn(self.snake.body,self.walls)  # Перемещаем еду в новое место

            if pg.Rect(*self.snake.body[0], GRID_SIZE, GRID_SIZE).colliderect(self.food.rect):
                self.snake.grow = True
                
                if self.food.weidth >= 20:
                    self.score += 4
                elif self.food.weidth < 20:
                    self.score += 2
                self.speeed += 2
                self.food.respawn(self.snake.body,self.walls)
                if self.score >= self.level*20 and not self.score >= 58 :
                    self.level += 1
                    self.walls = self.get_level_walls(self.level)  # Обновляем стены на новый уровень
                    self.snake.body[0] = (GRID_SIZE, GRID_SIZE)
                    self.snake.direction = DOWN
                    pg.time.delay(2000)
                    
            if self.snake.check_collision() or self.check_wall_collision():
                self.game_over = True
                self.save_score(username, game.score,game.level,game.speeed)            


    def draw(self):
        colors = [(10, 10, 10), (0, 0, 0)]
        for i in range(H // 2):
            for j in range(W // 2):
                pg.draw.rect(screen, colors[(i + j) % 2], (i * GRID_SIZE, j * GRID_SIZE, GRID_SIZE, GRID_SIZE))
        self.snake.draw()
        self.food.draw()

        # Рисуем стены
        for wall in self.walls:
            pg.draw.rect(screen, (255,100,0), wall)

        score_text = font.render(f"Score: {self.score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        level_text = font.render(f"Level: {self.level}", True, WHITE)
        screen.blit(level_text, (450, 10))
        if self.game_over:
            game_text = font.render("GAME OVER! Press R", True, WHITE)
            
            screen.blit(game_text, (W // 2 - 150, H // 2))
            

            
    def reset(self):
        self.__init__()

    
        

    def display_scorelist(self):
        cur.execute("""
            SELECT users.username, MAX(user_score.score) AS highest_score 
            FROM users 
            LEFT JOIN user_score ON users.id = user_score.user_id 
            GROUP BY users.id 
            ORDER BY highest_score DESC 
            LIMIT 5;
        """)
        rows = cur.fetchall()
        y_offset = 50
        for row in rows:
            score_text = font.render(f"{row[0]}: {row[1]}", True, WHITE)
            screen.blit(score_text, (W // 2 + 145, y_offset))
            y_offset += 30

def get_username():
    # Вводим имя пользователя
    input_box = pg.Rect(W // 4, H // 3, 300, 50)
    color_inactive = pg.Color('darkgreen')
    color_active = pg.Color('lightgreen')
    color = color_inactive
    active = False
    text = ''
    font = pg.font.Font(None, 32)

    
    

    running = True
    while running:
        screen.fill(BLACK)
        txt_surface = font.render(text, True, color)
        width = max(300, txt_surface.get_width()+10)
        input_box.w = width
        screen.blit(txt_surface, (input_box.x+20, input_box.y+15))
        pg.draw.rect(screen, color, input_box, 2,10)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        # Проверка, существует ли имя пользователя
                        return text
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        pg.display.flip()
    

        
        

# Получаем имя пользователя
username = get_username()
screen.fill(BLACK)
txt_surface = font.render(username, True, GREEN)
cur.execute('''
    SELECT MAX(user_score.score) AS highest_score, 
           MAX(user_score.level) AS highest_level
    FROM user_score
    LEFT JOIN users ON user_score.user_id = users.id
    WHERE users.username = %s;
''', (username,))

scorre = cur.fetchone()

if scorre[0] is None:
    screen.blit(txt_surface, (W // 2 - 50, H // 2 - 100))
    txt_np = font.render("New Player!", True, GREEN)
    screen.blit(txt_np, (W // 2 - 70, H // 2 - 50))


else:
# Рендерим текст с наивысшим счетом и уровнем
    txt_score = font.render(f"Highest score: {str(scorre[0])}", True, GREEN)
    txt_level = font.render(f"Highest level: {str(scorre[1])}", True, GREEN)

    # Выводим на экран
    screen.blit(txt_surface, (W // 2 - 50, H // 2 - 100))
    screen.blit(txt_score, (W // 2 - 100, H // 2 - 50))
    screen.blit(txt_level, (W // 2 - 100, H // 2))

pg.display.update()
pg.time.delay(2000)
# Инициализация игры
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
                  # Сохраняем очки
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
    game.display_scorelist()
    clock.tick(game.speeed)
    
      # Показываем рекорды
    pg.display.flip()
    

pg.quit()
sys.exit()
