import pygame
import os
import random
# settings
WIDTH, HEIGHT = 960, 720
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CHASER_WIDTH, CHASER_HEIGHT = 80, 80
CLOUD_WIDTH, CLOUD_HEIGHT = 160, 120
FLOOR_HEIGHT = 580
MIDNIGHT = 12, 6, 40

BG = pygame.image.load(os.path.join('assets', 'first_background.png'))



FPS = 60
VEL = 5
SPEED = 2
SPAWN_STAGE = 2 * SPEED




CLOUD_ACC = 1
CLOUD_FRICTION = -0.08
CHASER_ACC = 0.5
CHASER_FRICTION = -0.12
CHASER_GRAVITY = 0.5

FLOOR = pygame.image.load(os.path.join('assets', 'floor1.png'))
FLOOR_BORDER = pygame.transform.scale(FLOOR,(WIDTH, HEIGHT - FLOOR_HEIGHT))
WINDOW = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Stormchaser")

FLOOR_LIST = [(0, 570, WIDTH, HEIGHT - 570),(WIDTH + 1, 570, WIDTH, HEIGHT - 570)]

obs = [pygame.image.load(os.path.join('assets', 'cow1.png')).convert(), pygame.image.load(os.path.join('assets', 'tree_obstacle1.png')).convert(), pygame.image.load(os.path.join('assets', 'rock_obstacle1.png')).convert(), pygame.image.load(os.path.join('assets', 't_stone_obstacle.png')).convert()]

L_BOLT1 = pygame.image.load(os.path.join('assets', 'lightningbolt_1.png')).convert()

PLAYER_CHASER = pygame.image.load(os.path.join('assets', 'alien_chaser.png'))
CHASER = pygame.transform.scale(PLAYER_CHASER, (CHASER_WIDTH, CHASER_HEIGHT))
PLAYER_CLOUD = pygame.image.load(os.path.join('assets', 'cloud1.png'))
CLOUD = pygame.transform.scale(PLAYER_CLOUD, (CLOUD_WIDTH, CLOUD_HEIGHT))
pchaser = pygame.Rect(90, 500, CHASER_WIDTH, CHASER_HEIGHT)
pcloud = pygame.Rect(410, 15, CLOUD_WIDTH, CLOUD_HEIGHT)

