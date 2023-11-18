import pygame
import sys
from _Paddle import Paddle

pygame.init()
width, height = 700, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cyprian's Arkanoid")

sprites = pygame.sprite.Group()
paddle = Paddle(300,450)
sprites.add(paddle)
screen.fill((0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
            sys.exit()

    pygame.display.flip()
    sprites.draw(screen)
    

    