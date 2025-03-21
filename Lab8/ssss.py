import pygame as pg
import sys
import random


pg.init()

# Размеры окна
W, H = 600, 600
GRID_SIZE = 20  #razmer odnoi kletki

#colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  
RED = (255, 0, 0)  
BLACK = (0, 0, 0)  

# nash ekran
screen = pg.display.set_mode((W, H))
pg.display.set_caption("Zmeyka")

# Shrift
font = pg.font.Font('lab7/lishnee/MICKEY.TTF', 30)

# directions
UP = (0, -GRID_SIZE)
DOWN = (0, GRID_SIZE)
LEFT = (-GRID_SIZE, 0)
RIGHT = (GRID_SIZE, 0)

# eda
def get_random_food():
    return (
        random.randint(0, (W - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
        random.randint(0, (H - GRID_SIZE) // GRID_SIZE) * GRID_SIZE,
    )

# nivaya igra
def reset_game():
    global snake, direction, food, score, game_over
    snake = [
        (W // 2, H // 2),
        ((W // 2)-GRID_SIZE, H // 2),
        ((W // 2)-2*GRID_SIZE, H // 2),
        ]  
    direction = RIGHT
    food = get_random_food() 
    score = 0  
    game_over = False  


reset_game()
clock = pg.time.Clock()

running = True
while running:
    colors = [(10,10,10),(0,0,0)]
    for i in range(H//2):
        for j in range(W//2):
            pg.draw.rect(screen, colors[(i+j)%2], (i*GRID_SIZE, j*GRID_SIZE, GRID_SIZE, GRID_SIZE))
    

    pressed = pg.key.get_pressed()
    for event in pg.event.get():
        if event.type == pg.QUIT or pressed[pg.K_ESCAPE]:
            running = False
        if event.type == pg.KEYDOWN:
            if (event.key == pg.K_w or event.key == pg.K_UP) and direction != DOWN:
                direction = UP
            if (event.key == pg.K_s or event.key == pg.K_DOWN) and direction != UP:
                direction = DOWN
            if (event.key == pg.K_a or event.key == pg.K_LEFT) and direction != RIGHT:
                direction = LEFT
            if (event.key == pg.K_d or event.key == pg.K_RIGHT) and direction != LEFT:
                direction = RIGHT
            if event.key == pg.K_r and game_over:  # reset with r
                reset_game()

    if not game_over:  
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)  # novi segment

        
        if (
            new_head[0] < 0
            or new_head[0] >= W
            or new_head[1] < 0
            or new_head[1] >= H
            or new_head in snake[1:]
        ):
            game_over = True  #konec igri

        
        if new_head == food:
            score += 1
            food = get_random_food()
        else:
            snake.pop()  # esli eda ne syedena hvost ne udlinyaetsya

    # eda
    pg.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE),0,20)

    # Nasha zmeya
    for segment in snake:
        pg.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE),0,5)

    # shet
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    # restart
    if game_over:
        game_over_text = font.render("GAME OVER! Press R to Restart", True, WHITE)
        screen.blit(game_over_text, (W // 2 - 300, H // 2))

    pg.display.update()
    clock.tick(5 + score)  # fps = skorost


pg.quit()
sys.exit()
