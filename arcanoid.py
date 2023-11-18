import pygame
import sys
from _Paddle import Paddle

pygame.init()
width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cyprian's Arkanoid")

paddle = Paddle(screen,300,450, 40, 10)
paddle_speed = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0,0,0))
    keys = pygame.key.get_pressed() 
    paddle.draw()

    if keys[pygame.K_RIGHT]:
        paddle.move(5)
    elif keys[pygame.K_LEFT]:
        paddle.move(-5)

    pygame.display.update()
    clock.tick(60)
    

    