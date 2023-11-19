import pygame

class Ball():
    def __init__(self, screen, pos_x, pos_y, radius):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.ball_color = (200,0,100)
        self.draw()

    def draw(self):
        pygame.draw.circle(self.screen, self.ball_color, (self.pos_x, self.pos_y), self.radius)