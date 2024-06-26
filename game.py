import pygame
import time
import random

pygame.init()

#colors of the game
color1=(100,255,0)
color2=(100,200,200)
color3=(0,255,0)
color4=(213,200,80)
color5=(255,0,0)
color6 =(0,0,0)
#game window
box_len = 900
box_height = 600
#start game window
add_caption = pygame.display.set_mode((box_len, box_height))
pygame.display.set_caption('Snek Vs Py')
#game frame rate
timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10
#font style/size
display_style= pygame.font.SysFont('arial', 30, 'bold')
score_font= pygame.font.SysFont('arial', 45, 'bold')
#display final score
def final_score(score):
    value = score_font.render('Score : ' + str(score), True, color2)
    add_caption.blit(value, [0,0])
#draws snake
def make_snake(snake_block, list_snake):
    for x in list_snake:
        pygame.draw.rect(add_caption, color3, [x[0], x[1], snake_block, snake_block])
#display message on screen
def display_msg(msg, color):
    mssg = display_style.render(msg, True, color)
    add_caption.blit(mssg, [box_len/6 , box_height/3])
#starts the game
def game_start():
    game_over = False
    game_close = False
#sets inital position of snake
    value_x1 = box_len / 2
    value_y1 = box_height / 2
    new_x1 = 0
    new_y1 = 0

#sets inital length of snake
    list_snake = []
    snake_len = 1
#intial position of food
    foodx_pos = round(random.randrange(0, box_len - snake_block) / 10.0) * 10.0
    foody_pos = round(random.randrange(0, box_height - snake_block) / 10.0) * 10.0
#game over state of game
    while not game_over:
#game_close controls losing and message dispay to start over or quit
        while game_close == True:
            add_caption.fill(color6)
            display_msg('You lost! Want to play Again Press C otherwise press Q', color4)
            final_score(snake_len - 1)
            pygame.display.update()
#sets q key to that the game is over and not to show the message again to close game
#sets c key to continue the game and game_start()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_start()
#if game is quit, game over is true, changes state of game
#sets up the up, down, left, right keys to move snake
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x1 = -snake_block
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = snake_block
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -snake_block
                    new_x1 = 0
                elif event.key == pygame.K_DOWN:
                    new_y1 = snake_block
                    new_x1 = 0
#updates snake's postion based on what key is pressed
        value_x1 += new_x1
        value_y1 += new_y1
#checks if snake hits the sides of the window and triggers game_close and message
        if value_x1 >= box_len or value_x1 < 0 or value_y1 >= box_height or value_y1 < 0:
            game_close = True
#background color
        add_caption.fill(color6)
#draw food        
        pygame.draw.rect(add_caption, color5, [foodx_pos, foody_pos, snake_block, snake_block])
#update snakes position        
        snake_head = [value_x1, value_y1]
        list_snake.append(snake_head)
        if len(list_snake) > snake_len:
            del list_snake[0]
        for x in list_snake[:-1]:
            if x == snake_head:
                game_close = True
#draw the snake        
        make_snake(snake_block, list_snake)
#display score        
        final_score(snake_len-1)

        pygame.display.update()
#if snake eats food make snake longer
        if value_x1 == foodx_pos and value_y1 == foody_pos:
            foodx_pos = round(random.randrange(0, box_len - snake_block) / 10.0) * 10.0
            foody_pos = round(random.randrange(0, box_height - snake_block) / 10.0) * 10.0
            snake_len += 1
#frame rate is snake_speed
        timer.tick(snake_speed)
#quit the game
    pygame.quit()
    quit()
#start the game
game_start()
