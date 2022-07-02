from settings import *
from sprites import *

BG = pygame.image.load(os.path.join('assets', 'first_background.png')).convert()
BG2 = pygame.image.load(os.path.join('assets', 'first_background.png')).convert()



class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init() # initializes pygame
        pygame.mixer.init() # handles sound
        self.WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Stormchaser")
        self.clock = pygame.time.Clock()
        self.running = True
        

    def new(self):
        # start new game
        self.prev_score = 0
        self.all_sprites = pygame.sprite.Group() # groups all sprites in pygame program
        self.all_floors = pygame.sprite.Group()
        self.bg1 = pygame.sprite.Group()
        self.bg2 = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.l_strikes = pygame.sprite.Group()
        
        self.background_one = Background_one(self)
        self.background_two = Background_two(self)
        
        
        self.bg1.add(self.background_one)
        self.bg2.add(self.background_two)
        self.cloud = Cloud(self)
        self.chaser = Chaser(self)
        self.all_sprites.add(self.cloud)
        self.all_sprites.add(self.chaser)
        for floor in FLOOR_LIST:
            f = Floor(*floor)
            #self.all_sprites.add(f)
            self.all_floors.add(f)
        
        self.run()



    def run(self):
        
        # game loop
        
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)

            self.events()
            self.draw()
            self.update()



    def update(self):
        # game loop update
        self.all_sprites.update() # updates all sprites in group
        self.all_floors.update()
        self.background_one.update()
        self.background_two.update()
        self.l_strikes.update()
        while len(self.obstacles) < SPAWN_STAGE:  # spawns limited number of obstacles 
            ob = Obstacles(self)
            self.obstacles.add(ob)
        self.obstacles.update()
        
        # checks if player hits platform # only if falling
        if self.chaser.vel.y > 0:
            floor_hits = pygame.sprite.spritecollide(self.chaser, self.all_floors, False)
            if floor_hits:
                self.chaser.pos.y = floor_hits[0].rect.top
                self.chaser.vel.y = 0
                self.chaser.rect.midbottom = self.chaser.pos
        
        # checks if player collides with obstacles and ends game if true
        ob_hits = pygame.sprite.spritecollide(self.chaser, self.obstacles, False, pygame.sprite.collide_circle)
        if ob_hits:
            self.playing = False
            self.running = False
        
        
    def draw(self):
        # game loop draw
        
        self.bg1.draw(self.WINDOW)
        self.bg2.draw(self.WINDOW)
        self.all_sprites.draw(self.WINDOW) # draws all sprites in group
        self.obstacles.draw(self.WINDOW)
        self.l_strikes.draw(self.WINDOW)
        scoreboard(WINDOW, F"{'Score: ' + str(self.cloud.score)}", 25, 50, 680)
        pygame.display.flip() # double buffering / after drawing everything


    def events(self):

        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.chaser.jump()
                if event.key == pygame.K_DOWN:
                    self.cloud.bolt()
                    self.cloud.score -= 10 # removes 10 points for each lightning bolt
                    #self.prev_score -= 10







    def show_start_screen(self):
        # game start screen
        self.start = pygame.sprite.Group()
        self.s_screen = Start()
        self.start.add(self.s_screen)
        self.start.draw(self.WINDOW)
        #self.draw_text("A and D move player SPACE to jump\nArrows move cloud DOWN to shoot lightning", 22, WHITE, WIDTH / 2, HEIGHT / 2)
        #self.draw_text("Press a key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()


    def show_game_over(self):
        # game over screen
        #if self.running == False:
            #return
        self.over = pygame.sprite.Group()
        self.g_o = Over()
        self.over.add(self.g_o)
        self.over.draw(self.WINDOW)
        scoreboard(WINDOW, F"{'Score: ' + str(self.cloud.score)}", 42, WIDTH / 2 - 80, 220)
        pygame.display.flip()
        self.wait_for_key()
        
        


    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
                    self.running = True


g = Game()
g.show_start_screen()
while g.running:
    
    g.new()
    g.show_game_over()


pygame.quit()