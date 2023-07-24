import pygame,random
pygame.init()
window=(400,600)

#board:
board_height=10
board_width=100
board_x=200
board_y=window[1]-board_height

#score
points=0
#boll:
boll_x=random.randrange(0,window[0])
boll_y=random.randrange(0,window[1]//2)
boll_size=15

#colors:
powder_blue=(176,224,230)
red=(255,0,0)

#directions:
boll_x_veloxity=0
boll_y_velocity=3
right=False
left=False

def game_over(points,window,screen):
    text0 = game_font.render("GAME OVER",True,(0, 0, 0))
    text = game_font.render(f'POINTS:{points}', True, (0, 0, 0))
    pygame.draw.rect(screen,(176,224,230),(50,130,300,100))
    screen.blit(text0,(150,150))
    screen.blit(text,(150,200))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

#screen setup
screen=pygame.display.set_mode(window)
pygame.display.set_caption('Boll Saving')
clock=pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                right=True
            if event.key==pygame.K_LEFT:
                left=True
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_RIGHT:
                right=False
            if event.key==pygame.K_LEFT:
                left=False
        if event.type==pygame.QUIT:
            pygame.quit()
    if board_x<0:
        left=False
    if board_x+board_width>window[0]:
        right=False
    if right:
        board_x+=2
    if left:
        board_x-=2
    boll_x+=boll_x_veloxity
    boll_y+=boll_y_velocity
    if boll_x>=window[0]:
        boll_x_veloxity=-3
    if boll_x<=0:
        boll_x_veloxity=3
    if boll_y<=2:
        boll_y_velocity=-boll_y_velocity
    if boll_y>window[1]:
        game_over(points,window,screen)
    if pygame.Rect(board_x,board_y,board_width,board_height).colliderect(pygame.Rect(boll_x,boll_y,boll_size,boll_size)):
        points+=1
        boll_y_velocity=-boll_y_velocity
        shuf=[-3,3,0]
        random.shuffle(shuf)
        boll_x_veloxity=random.choice(shuf)
    screen.fill((0,0,0))
    game_font=pygame.font.SysFont('Arial',14)
    text=game_font.render(f'POINTS:{points}',True,(255,255,255))
    screen.blit(text,(300,30))
    pygame.draw.rect(screen,red,(boll_x,boll_y,boll_size,boll_size),border_radius=10)
    pygame.draw.rect(screen,powder_blue,(board_x,board_y,board_width,board_height),border_radius=5)
    pygame.display.flip()
    clock.tick(80)
