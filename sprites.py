from settings import *

VEC = pygame.math.Vector2

# set up assets folders
game_folder = os.path.dirname(__file__) # game directory so will run on any computer
img_folder = os.path.join(game_folder, "assets") # joins game folder and assets folder so that images will load

k_list = []

class Cloud(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(os.path.join(img_folder, "cloud1.png")).convert() #creates sprite image / for free use images go to opengameart.org / also check out kenney
        self.image.set_colorkey(BLACK)
        #self.image.fill(GREEN) # fills image with color
        self.rect = self.image.get_rect() # Pygame figures out what rectangle to use
        
        self.rect.center = (WIDTH / 2, 40) # puts center of sprite rectangle in the middle of the screen
        self.pos = VEC(WIDTH / 2, 40)
        self.vel = VEC(0, 0)
        self.acc = VEC(0, 0)

    def bolt(self):
        strike = Lightning(self.rect.centerx,self.rect.centery)
        self.game.l_strikes.add(strike)

    def update(self):
        self.acc = VEC(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -CLOUD_ACC
        if keys[pygame.K_RIGHT]:
            self.acc.x = CLOUD_ACC

        self.acc += self.vel * CLOUD_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        self.rect.center = self.pos

        strike_hits = pygame.sprite.groupcollide(self.game.l_strikes, self.game.obstacles, True, True)
        for hit in strike_hits:
            TOTAL_HITS.append(hit)
            print(len(TOTAL_HITS))




class Lightning(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = L_BOLT1
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.centerx = x
        self.pos = VEC(self.rect.centerx, self.rect.bottom)
        self.bolt_speed = 10

    def update(self):
        self.pos.y += self.bolt_speed
        #self.rect.y += self.bolt_speed
        self.pos.y = self.rect.y
        if self.pos.y <= 590:
            #k_list.append(self)
            self.kill()
            #print(k_list)
        


class Chaser(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.image.load(os.path.join(img_folder, "alien_chaser.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = 25
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.midbottom = (20, 570)
        self.pos = VEC(20 , 570)
        self.vel = VEC(0, 0)
        self.acc = VEC(0, 0)

    def jump(self):
        #jump only if standing on platform
        self.rect.y += 1
        hits = pygame.sprite.spritecollide(self, self.game.all_floors, False)
        self.rect.y -= 1
        if hits:
            self.vel.y = -10


    def update(self):
        self.acc = VEC(0, CHASER_GRAVITY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.acc.x = -CHASER_ACC
        if keys[pygame.K_d]:
            self.acc.x = CHASER_ACC

        self.acc.x += self.vel.x * CHASER_FRICTION
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > 300:
            self.pos.x = 300
        if self.pos.x < 40:
            self.pos.x = 40
        self.rect.midbottom = self.pos

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, "floor1.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Background_one(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets', 'first_background.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.pos = VEC(0, 0)

    def update(self):
        self.pos.x -= SPEED
        if self.pos.x < (BG.get_width() * -1):
            self.pos.x = BG.get_width()
        self.rect.topleft = self.pos


class Background_two(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join('assets', 'first_background.png')).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = (WIDTH, 0)
        self.pos = VEC(WIDTH, 0)

    def update(self):
        self.pos.x -= SPEED
        if self.pos.x < (BG.get_width() * -1):
            self.pos.x = BG.get_width()
        self.rect.topleft = self.pos

class Obstacles(pygame.sprite.Sprite):
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = random.choice(obs)  # chooses obstacle image at random
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.height / 2.5)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        
        self.rect.bottomleft = (WIDTH + random.randrange(1, 880), 570)
        self.pos = VEC(WIDTH + random.randrange(1, 880), 570)

    def update(self):
        self.pos.x -= SPEED
        
        if self.pos.x < -200:  # removes obstacle after it leaves the screen
            self.kill()
            #SPEED + 0.5 # not yet working

            #print(SPEED)
        self.rect.bottomleft = self.pos
        



