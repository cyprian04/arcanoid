import pygame
import sys
from _Paddle import Paddle
from _Ball import Ball

pygame.init()
width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cyprian's Arkanoid")
clock = pygame.time.Clock()

paddle = Paddle(screen,300,450, 70, 10)
paddle_speed = 5

ball = Ball(screen, 350,250, 8, 5, 5)


def paddle_movement(keys):
    if keys[pygame.K_RIGHT]:
        paddle.move(5)
    elif keys[pygame.K_LEFT]:
        paddle.move(-5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))

    keys = pygame.key.get_pressed()
    paddle_movement(keys)
    ball.check_collision(700, 500) # for screen walls

    paddle.draw()
    ball.draw()

    pygame.display.update()
    clock.tick(60)
    

    