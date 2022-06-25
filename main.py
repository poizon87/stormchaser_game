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
        self.all_sprites = pygame.sprite.Group() # groups all sprites in pygame program
        self.all_floors = pygame.sprite.Group()
        self.bg1 = pygame.sprite.Group()
        self.bg2 = pygame.sprite.Group()
        self.obstacles = pygame.sprite.Group()
        self.background_one = Background_one()
        self.background_two = Background_two()
        self.bg1.add(self.background_one)
        self.bg2.add(self.background_two)
        self.cloud = Cloud()
        self.chaser = Chaser(self)
        self.all_sprites.add(self.cloud)
        self.all_sprites.add(self.chaser)
        for floor in FLOOR_LIST:
            f = Floor(*floor)
            self.all_sprites.add(f)
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
        while len(self.obstacles) < SPAWN_STAGE:
            
            ob = Obstacles()
            self.obstacles.add(ob)

        self.obstacles.update()
        # checks if player hits platform # only if falling
        if self.chaser.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.chaser, self.all_floors, False)
            if hits:
                self.chaser.pos.y = hits[0].rect.top
                self.chaser.vel.y = 0
                self.chaser.rect.midbottom = self.chaser.pos
        
        
    def draw(self):
        # game loop draw
        
        self.bg1.draw(self.WINDOW)
        self.bg2.draw(self.WINDOW)
        self.all_sprites.draw(self.WINDOW) # draws all sprites in group
        self.obstacles.draw(self.WINDOW)
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







    def show_start_screen(self):
        # game start screen
        pass

    def show_game_over(self):
        # game over screen
        pass


g = Game()
g.show_start_screen()
while g.running:
    
    g.new()
    g.show_game_over()

pygame.quit()