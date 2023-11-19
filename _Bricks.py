import pygame
class Brick():
    def __init__(self, screen, pos_x, pos_y, width, height, color=(255, 255, 255)):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.color = color
        self.is_visible = True
    
    def draw(self):
        if self.is_visible:
            pygame.draw.rect(self.screen, self.color, (self.pos_x, self.pos_y, self.width, self.height))

    def hide(self):
        self.is_visible = False