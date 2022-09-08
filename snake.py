from email import message
from tkinter import font
import pygame
import random
pygame.init()


blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
black = (0,0,0)


dis_width = 800
dis_height = 600

snake_block = 10
snake_speed = 20

dis = pygame.display.set_mode((dis_width,dis_height))
pygame.display.set_caption("SnakeGame by Masha")

clock = pygame.time.Clock()

def message(msg, color):
    font_style = pygame.font.SysFont(None,50)
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [0 , dis_height/2])

def snake(snake_block , snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_head = []
    snake_len = 1
    
    food_x = round(random.randrange(0, dis_width - snake_block)/10)*10
    food_y = round(random.randrange(0, dis_height - snake_block)/10)*10

    while not game_over:
        while game_close:
            dis.fill(white)
            message("You lost! Press 'q' - quite or 'a' - play again.", red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_q: 
                        game_over = True
                        game_close = False 
                if event.key == pygame.K_a: 
                    gameLoop()    

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                if event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                if event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                if event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change

        dis.fill(white)

        pygame.draw.rect(dis, red, [food_x,food_y,snake_block,snake_block ])
        pygame.draw.rect(dis, blue, [x1,y1,snake_block,snake_block])

        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_len:
            snake_list.pop(0)

       # for i in snake_list[:-1]:
       #     if i == snake_head:
       #         game_close = True

        snake(snake_block, snake_list)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10) * 10
            food_y = round(random.randrange(0, dis_height - snake_block) / 10) * 10
            snake_len += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()