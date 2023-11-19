import pygame

class Ball():
    def __init__(self, screen, pos_x, pos_y, radius, vel_x, vel_y):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.ball_color = (200,0,100)
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.draw()
        self.move(vel_x, vel_y)

    def draw(self):
        pygame.draw.circle(self.screen, self.ball_color, (self.pos_x, self.pos_y), self.radius)
    
    def move(self, x_vel, y_vel ):
        self.pos_x += x_vel
        self.pos_y += y_vel
    
    def check_collision(self):

        if self.pos_x - self.radius < 0:
            self.vel_x = -self.vel_x
        elif self.pos_x + self.radius > 700:
            self.vel_x = -self.vel_x

        # Check top and bottom walls
        if self.pos_y - self.radius < 0:
            self.vel_y = -self.vel_y
        elif self.pos_y + self.radius > 500:
            self.vel_y = -self.vel_y

        self.move(self.vel_x, self.vel_y)