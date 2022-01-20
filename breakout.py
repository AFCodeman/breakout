import pygame, sys
from pygame.locals import *

import ball
import brick

# Constants that will be used in the program
import paddle

APPLICATION_WIDTH = 400
APPLICATION_HEIGHT = 600
PADDLE_Y_OFFSET = 30
BRICKS_PER_ROW = 10
BRICK_SEP = 4  # The space between each brick
BRICK_Y_OFFSET = 70
BRICK_WIDTH = int((APPLICATION_WIDTH - (BRICKS_PER_ROW * BRICK_SEP)) / BRICKS_PER_ROW)
BRICK_HEIGHT = 8
PADDLE_WIDTH = 60
PADDLE_HEIGHT = 10
RADIUS_OF_BALL = 10
NUM_TURNS = 3

# Sets up the colors
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN =(0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
mainsurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
pygame.display.set_caption("Breakout")
mainsurface.fill((0, 0, 0))

# Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
# the screen (BRICK_Y_OFFSET)
bricks = pygame.sprite.Group()
paddles = pygame.sprite.Group()
x_pos = BRICK_SEP
y_pos = BRICK_Y_OFFSET
COLORS = [RED, ORANGE, YELLOW, GREEN, CYAN]
for COLOR in COLORS:
    for x in range(2):
        for x in range(BRICKS_PER_ROW):
            b = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, COLOR)
            bricks.add(b)
            b.rect.x = x_pos
            b.rect.y = y_pos
            mainsurface.blit(b.image, b.rect)
            x_pos += BRICK_WIDTH + BRICK_SEP
        x_pos = BRICK_SEP
        y_pos += BRICK_HEIGHT + BRICK_SEP

p = paddle.Paddle(PADDLE_WIDTH, PADDLE_HEIGHT, WHITE)
paddles.add(p)
p.rect.x = APPLICATION_WIDTH / 2
p.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
mainsurface.blit(p.image, p.rect)

bl = ball.Ball(WHITE, APPLICATION_WIDTH , APPLICATION_HEIGHT , 10)
bl.rect.x = APPLICATION_WIDTH / 2
bl.rect.y = APPLICATION_HEIGHT / 2
mainsurface.blit(bl.image, bl.rect)



while True:
    mainsurface.fill(BLACK)
    for brick in bricks:
        mainsurface.blit(brick.image, brick.rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            p.move(pygame.mouse.get_pos())
    mainsurface.blit(p.image, p.rect)
    mainsurface.blit(bl.image, bl.rect)
    bl.move()
    mainsurface.blit(bl.image, bl.rect)
    bl.collide_bricks(bricks)
    bl.collide_paddle(paddles)
    pygame.display.update()
