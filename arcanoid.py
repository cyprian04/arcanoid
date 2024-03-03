import pygame
import random
import sys
from _Paddle import Paddle
from _Ball import Ball
from _Bricks import Brick

pygame.init()
window_width, window_height = 700, 500
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Cyprian's Arkanoid")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def draw_text(text, font, color, x, y, surface):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)


def create_button(rect, color, hover_color, text, text_color):
    button_surface = pygame.Surface((rect.width, rect.height))
    button_surface.fill(color)
    pygame.draw.rect(button_surface, (0, 0, 0), rect, 2)

    mouse_pos = pygame.mouse.get_pos()
    is_hover = rect.collidepoint(mouse_pos)

    if is_hover:
        button_surface.fill(hover_color)

    draw_text(text, font, text_color, rect.width // 2, rect.height // 2, button_surface)

    return button_surface, is_hover


def main_menu(screen, WIDTH, HEIGHT):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    game_loop(screen)
                elif quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        # Draw background
        screen.fill((100,100,100))

        # Create buttons
        play_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
        quit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 50)

        play_button, play_hover = create_button(play_button_rect, (0, 128, 255), (0, 100, 200), "Play", (255,255,255))
        quit_button, quit_hover = create_button(quit_button_rect, (255, 0, 0), (200, 0, 0), "Quit", (255,255,255))

        # Draw buttons on the screen
        screen.blit(play_button, play_button_rect.topleft)
        screen.blit(quit_button, quit_button_rect.topleft)

        # Update display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(60)

def is_game_over(screen, lifes):
    if len(lifes) == 0:
        screen.fill((0,0,0))
        game_over_text = font.render("Game Over!", True, (255, 255, 255))
        screen.blit(game_over_text, (window_width // 2 - game_over_text.get_width() // 2, window_height // 2 - game_over_text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(2000)
        return True
    return False

def game_loop(screen):

    paddle = Paddle(screen,250,450, 70, 10)

    while True:
        start_ball_vel_x = random.randint(-5,5)
        start_ball_vel_y = random.randint(-5,5)
        if start_ball_vel_x and start_ball_vel_y != 0:
            break

    ball = Ball(screen, 350,250, 8, start_ball_vel_x, start_ball_vel_y)

    bricks = []
    for x in range(6):
        for y in range(3): 
            bricks.append(Brick(screen, 90 * (x+1), 50* (y+1), 50, 20))

    lifes = []
    radius = 8
    gap = 10
    for x in range(3):
        xpos = window_width - (x + 1) * (radius * 2 + gap)
        ypos = window_height - radius - gap
        lifes.append(Ball(screen, xpos, ypos, radius, 0,0, (255,0,0)))

    unbreakable_bricks = []
    for x in range(6): unbreakable_bricks.append(Brick(screen, 90 * (x+1), 200, 50, 20, (100,100,100)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if is_game_over(screen, lifes): break

        screen.fill((0,0,0))

        ball.check_wall_collision(window_width, window_height, lifes)
        ball.check_paddle_collision(paddle.pos_x, paddle.pos_y, paddle.width, paddle.height)
        ball.check_brick_collision(bricks)
        ball.check_brick_collision(unbreakable_bricks, "unbreakable")

        ball.move()
        paddle.move(pygame.key.get_pressed())

        paddle.draw()
        ball.draw()
        for life in lifes: life.draw()
        for brick in bricks: brick.draw()
        for u_brick in unbreakable_bricks: u_brick.draw()

        pygame.display.update()
        clock.tick(60)
    
if __name__ == "__main__":
    main_menu(screen,window_width, window_height)

    