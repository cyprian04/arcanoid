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
brick = Brick(screen,500,400, 80, 25)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    ball.check_wall_collision(window_width, window_height)
    ball.check_paddle_collision(paddle.pos_x, paddle.pos_y, paddle.width, paddle.height)

    ball.move()
    paddle.move(pygame.key.get_pressed())

    paddle.draw()
    ball.draw()
    brick.draw()

    pygame.display.update()
    clock.tick(60)
    

    