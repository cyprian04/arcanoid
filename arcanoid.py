import pygame
import sys
from _Paddle import Paddle
from _Ball import Ball
from _Bricks import Brick

pygame.init()
window_width, window_height = 700, 500
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Cyprian's Arkanoid")
clock = pygame.time.Clock()

paddle = Paddle(screen,300,450, 70, 10)
ball = Ball(screen, 350,250, 8, 5, 5)

bricks = []
for x in range(6):
    for y in range(3): 
        bricks.append(Brick(screen, 90 * (x+1), 50* (y+1), 50, 20))

unbreakable_bricks = []
for x in range(6): unbreakable_bricks.append(Brick(screen, 90 * (x+1), 200, 50, 20, (100,100,100)))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    ball.check_wall_collision(window_width, window_height)
    ball.check_paddle_collision(paddle.pos_x, paddle.pos_y, paddle.width, paddle.height)
    ball.check_brick_collision(bricks)
    ball.check_brick_collision(unbreakable_bricks, "unbreakable")

    ball.move()
    paddle.move(pygame.key.get_pressed())

    paddle.draw()
    ball.draw()
    for brick in bricks: brick.draw()
    for u_brick in unbreakable_bricks: u_brick.draw()

    pygame.display.update()
    clock.tick(60)
    

    