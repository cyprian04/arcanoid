import pygame

class Paddle():
    def __init__(self, screen, pos_x, pos_y, width, height):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.paddle_color = (0,255,0)
        self.draw()

    def draw(self):
        pygame.draw.rect(self.screen, self.paddle_color, (self.pos_x, self.pos_y, self.width, self.height))

    def move(self, x_pos):
        if self.pos_x + x_pos <= 0:
            self.pos_x = 0;

        elif self.pos_x + self.width + x_pos >= 700:
            self.pos_x = 700- self.width;

        elif self.pos_x + x_pos > 0 and x_pos < 0:
            self.pos_x += x_pos  

        elif self.pos_x + self.width + x_pos < 700 and x_pos > 0:
            self.pos_x += x_pos 