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
    
    def check_paddle_collision(self, paddle_x, paddle_y, paddle_width, paddle_height):
        prev_pos_x = self.pos_x - self.vel_x
        prev_pos_y = self.pos_y - self.vel_y

        x_collision = (
            paddle_x < self.pos_x + self.radius < paddle_x + paddle_width
            or paddle_x < prev_pos_x - self.radius < paddle_x + paddle_width
        )
        y_collision = (
            paddle_y < self.pos_y + self.radius < paddle_y + paddle_height
            or paddle_y < prev_pos_y - self.radius < paddle_y + paddle_height
        )

        if x_collision and y_collision:
            self.vel_y = -self.vel_y

    def check_wall_collision(self, width, height):
        if self.pos_x - self.radius < 0 or self.pos_x + self.radius > width:
            self.vel_x = -self.vel_x

        if self.pos_y - self.radius < 0 or self.pos_y + self.radius > height:
            self.vel_y = -self.vel_y

        self.move(self.vel_x, self.vel_y)