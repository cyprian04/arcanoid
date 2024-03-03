import pygame
import random

class Ball():
    def __init__(self, screen, pos_x, pos_y, radius, vel_x=0, vel_y=0, color=(50,100,250)):
        self.screen = screen
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.ball_color = color
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.draw()
        self.move()

    def draw(self):
        """
        Function which draws ball on the screen
        """
        pygame.draw.circle(self.screen, self.ball_color, (self.pos_x, self.pos_y), self.radius)
    
    def move(self):
        """
        Function which updates the ball velocity
        """
        self.pos_x += self.vel_x
        self.pos_y += self.vel_y
    
    def check_wall_collision(self, width, height, lifes):
        """
        Function which checks if ball touches the wall, and if so, then reverse the ball velocity so it bounce off
        """
        if self.pos_x - self.radius < 0 or self.pos_x + self.radius > width:
            self.vel_x = -self.vel_x

        if self.pos_y - self.radius < 0:
            self.vel_y = -self.vel_y

        if  self.pos_y + self.radius > height:
            self.vel_y = -self.vel_y
            lifes.pop()

    def check_paddle_collision(self, paddle_x, paddle_y, paddle_width, paddle_height):
        """
        Function which checks if ball touches the paddle topsite, if so, 
        then returns and reverse its velocity, otherwise return false
        """
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

        if x_collision and y_collision and self.vel_y > 0:
            self.vel_y = -self.vel_y
            return True;
        return False;

    def check_brick_collision(self, bricks, type="breakable"):
        """
        Function which checks if ball touches the brick, if so, then returns TRUE and overrides the velocity
        with random generated (reversed) velocity in specified range, otherwise returns False
        """
        for brick in bricks:
            if (
                brick.is_visible
                and self.pos_y + self.radius >= brick.pos_y
                and self.pos_y - self.radius <= brick.pos_y + brick.height
                and self.pos_x + self.radius >= brick.pos_x
                and self.pos_x - self.radius <= brick.pos_x + brick.width
            ):
                left_side  = self.pos_x <= brick.pos_x
                right_side = self.pos_x >= brick.pos_x + brick.width
                top_side   = self.pos_y <= brick.pos_y
                bottom_side= self.pos_y >= brick.pos_y + brick.height

                if left_side:
                    self.vel_x = random.randint(-5,-2)
                if right_side:
                    self.vel_x = random.randint(2,5)
                if top_side:
                    self.vel_y = random.randint(-5,-2)
                if bottom_side:
                    self.vel_y = random.randint(2,5)
                if type == "breakable": brick.hide()
                return True
        return False