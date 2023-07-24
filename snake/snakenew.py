import pygame,random
pygame.init()
window=(600,600)

#colors:
Black=(0,0,0)
Green=(0,255,0)
Red=(255,0,0)

#snake:
snake_size=15
step_size=5
snake_body=[(50,300)]

#directions:
UP=(0,-step_size)
DOWN=(0,step_size)
RIGHT=(step_size,0)
LEFT=(-step_size,0)

#window display:
snake_direction=RIGHT
screen=pygame.display.set_mode(window)
pygame.display.set_caption('SNAKE GAME')
clock=pygame.time.Clock()

def draw_Snake_body(snake_body):
    for snake in snake_body:
        pygame.draw.rect(screen,Green,(snake[0],snake[1],snake_size,snake_size),border_radius=3)
def draw_fruit():
    pygame.draw.circle(screen,Red,food,7)
def generate_food(snake_body):
    while True:
        fruit=(random.randrange(0,window[0],snake_size),random.randrange(0,window[1],snake_size))
        if fruit not in snake_body:
            return fruit
food=generate_food(snake_body)
while True:

    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                snake_direction=UP
            if event.key==pygame.K_DOWN:
                snake_direction=DOWN
            if event.key==pygame.K_LEFT:
                snake_direction=LEFT
            if event.key==pygame.K_RIGHT:
                snake_direction=RIGHT
        if event.type==pygame.QUIT:
            pygame.quit()

    #newposition
    headx,heady=snake_body[-1]
    new_head_x=(headx+snake_direction[0])%window[0]
    new_head_y=(heady+snake_direction[1])%window[1]
    new_head=(new_head_x,new_head_y)
    if new_head in snake_body:
        pygame.quit()
    snake_body.append(new_head)
    if pygame.Rect(new_head[0], new_head[1], snake_size, snake_size).colliderect(pygame.Rect(food[0], food[1], 7, 7)):
        food=generate_food(snake_body)
    else:
        snake_body.pop(0)
    screen.fill(Black)
    draw_fruit()
    draw_Snake_body(snake_body)
    pygame.display.flip()
    clock.tick(60)
