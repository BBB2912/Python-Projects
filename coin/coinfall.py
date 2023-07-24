import pygame,random
class Rainfall:
    def __init__(self):
        pygame.init()
        self.points=0
        self.load_images()
        self.no_of=random.randrange(3 ,15)
        window_height = 640
        window_width = 480
        self.robo_x=10
        self.coinpositions=self.coinposition()
        self.image=self.imag(self.no_of)
        self.galaxy=pygame.image.load('galaxy.jpg')
        self.right,self.left=False,False
        self.clock=pygame.time.Clock()
        self.window=pygame.display.set_mode((window_width,window_height))
        pygame.display.set_caption("CoinRainfall")
        self.dashboard()
    def dashboard(self):
        self.window.blit(self.galaxy, (0, 0))
        pygame.draw.rect(self.window,(255,255,0),(100,220,200,100))
        dashbord_text=pygame.font.SysFont('Arial',18)
        dash_text=dashbord_text.render('Press F2 -- New game',True,(0,0,0))
        dash_text1 = dashbord_text.render('Press x -- Exit game', True, (0, 0, 0))
        self.window.blit(dash_text,(130,240))
        self.window.blit(dash_text1, (130, 270))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F2:
                        self.new_game()
                    if event.key == pygame.K_x:
                        exit()
                if event.type==pygame.QUIT:
                    exit()
    def score_board(self):
        self.window.blit(self.galaxy, (0, 0))
        pygame.draw.rect(self.window,(255, 255, 0), (100, 220, 200, 100))
        dashbord_text = pygame.font.SysFont('Arial', 18)
        score_text = dashbord_text.render('Press r -- Resume ', True, (0, 0, 0))
        score_text0=dashbord_text.render(f'YOUR SCORE::{self.points}',True,(150,24,0))
        score_text1 = dashbord_text.render('Press e -- Exit game', True, (0, 0, 0))
        self.window.blit(score_text0,(130,240))
        self.window.blit(score_text, (130, 260))
        self.window.blit(score_text1, (130, 280))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key==pygame.K_r:
                        self.main_loop()
                    if event.key==pygame.K_e:
                        self.dashboard()
                if event.type==pygame.QUIT:
                    exit()
    def load_images(self):
        self.images = []
        for name in ['robot','coin','monster']:
            self.images.append(pygame.image.load(name+'.png'))
    def imag(self,no_of):
        return [random.choice([1,2]) for i in range(no_of)]
    def coinposition(self):
        return [(random.randrange(0,480),random.randrange(-200,0))for i in range(self.no_of)]
    def new_game(self):
        self.points=0
        self.coinpositions = self.coinposition()
        self.main_loop()
    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
            pygame.time.Clock().tick(0)
    def check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    self.left = True
                if event.key==pygame.K_RIGHT:
                    self.right=True
                if event.key==pygame.K_ESCAPE:
                    return self.score_board()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    self.left=False
                if event.key==pygame.K_RIGHT:
                    self.right=False
            if event.type == pygame.QUIT:
                exit()
        if self.robo_x  < 0:
            self.left = False
        if self.robo_x + self.images[0].get_width() > 480:
            self.right = False
        if self.right:
            self.robo_x+=1
        if self.left:
            self.robo_x-=1
    def draw_window(self):
        self.window.fill((25,25,0))
        self.window.blit(self.galaxy,(0,0))
        game_font = pygame.font.SysFont('Arial', 15)
        text = game_font.render(f'Points->{self.points}', True, (255, 255, 255))
        self.window.blit(text, (400, 100))
        self.window.blit(self.images[0],(self.robo_x,640-self.images[0].get_height()))
        for j,i in enumerate(self.coinpositions):
            self.window.blit(self.images[self.image[j]],(i[0],i[1]))
        self.colid()
        self.updatecoins()
        pygame.display.flip()
    def updatecoins(self):
        self.coinpositions=[(random.randrange(0,450),random.randrange(-200,0)) if i[1]>=640 else  (i[0],i[1]+1) for i in self.coinpositions]
    def colid(self):
        for j,i in enumerate(self.coinpositions):
            if self.image[j]==2 and (i[0] in [k for k in range(self.robo_x-25,self.robo_x+25)] and i[1] in [l for l in range(640-self.images[0].get_height(),630)]):
                return self.score_board()
            if self.image[j]==1 and (i[0] in [k for k in range(self.robo_x-25,self.robo_x+25)] and i[1] in [l for l in range(640-self.images[0].get_height(),630)]):
                self.points+=1
                x=self.coinpositions.index(i)
                self.coinpositions[x]=(random.randrange(0,450),random.randrange(-200,0))
if __name__=='__main__':
    Rainfall()
