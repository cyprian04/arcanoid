import pygame
import random
import sys
import vlc
import os
from _Paddle import Paddle
from _Ball import Ball
from _Bricks import Brick

pygame.init()
window_width, window_height = 700, 500
screen = pygame.display.set_mode((window_width, window_height))
script_dir = os.path.dirname(os.path.abspath(__file__))
sounds_dir = os.path.join(script_dir, "sounds")
images_dir = os.path.join(script_dir, "images")
background_image = pygame.image.load(images_dir + "\menuBackground.png")
background_image = pygame.transform.scale(background_image, (window_width, window_height))
game_background_image = pygame.image.load(images_dir + "\gameBackground.jpg")
game_background_image = pygame.transform.scale(game_background_image, (window_width, window_height))
pygame.display.set_caption("Cyprian's Arkanoid")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

vlc_instance = vlc.Instance("--no-xlib")

def play_sound(file_path):
    """
    Function Responsible for playing sound from passed file_path as parameter via vlc module
    """
    player = vlc_instance.media_player_new()
    media = vlc_instance.media_new(file_path)
    player.set_media(media)
    player.play()
    return player

def draw_text(text, font, color, x, y, surface):
    """
    Function which draws text on a certian surface with specified parameters
    """
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def create_button(rect, color, hover_color, text, text_color):
    """
    Function responsible for creating buttons in specified position, surface and  with specified color and text
    """
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
    """
    Function which creates whole start menu in game and is responsible for running game loop
    """
    menu_song_player = play_sound(sounds_dir +"\menuSong.mp3")
    while True:
        if menu_song_player.is_playing() == False:
            menu_song_player.play()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(pygame.mouse.get_pos()):
                    menu_song_player.stop()
                    game_loop(screen)
                elif quit_button_rect.collidepoint(pygame.mouse.get_pos()):
                    menu_song_player.stop()
                    pygame.quit()
                    sys.exit()

        screen.blit(background_image, (0, 0))

        play_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50)
        quit_button_rect = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 + 20, 200, 50)

        play_button, play_hover = create_button(play_button_rect, (0, 128, 255), (0, 100, 200), "Play", (255,255,255))
        quit_button, quit_hover = create_button(quit_button_rect, (255, 0, 0), (200, 0, 0), "Quit", (255,255,255))

        screen.blit(play_button, play_button_rect.topleft)
        screen.blit(quit_button, quit_button_rect.topleft)

        pygame.display.flip()

        clock.tick(60)

def get_ready(screen):
    """
    Function which tells player to get ready by displaying text and changing screen background
    """
    screen.fill((0,0,0))
    draw_text("Get Ready!",font, (200, 100, 155), window_width // 2, window_height // 2 ,screen)
    pygame.display.update()
    pygame.time.delay(2000)

def game_is_won():
    """
    Function which is executed when a player has broken all the bricks so he won
    """
    screen.fill((0,0,0))
    draw_text("WIINNN!",font, (55, 155, 100), window_width // 2, window_height // 2 ,screen)
    pygame.display.update()
    play_sound(sounds_dir + "\winSound.wav")
    pygame.time.delay(2000)

def is_game_over(screen, lifes):
    """
    Function which checks if player lost the game by losing all the remaining lives
    """
    if len(lifes) == 0:
        screen.fill((0,0,0))
        draw_text("Game Over!",font, (255, 255, 255), window_width // 2, window_height // 2 ,screen)
        pygame.display.update()
        play_sound(sounds_dir + "\gameOverSound.wav")
        pygame.time.delay(2000)
        return True
    return False

def game_loop(screen):
    """
    Function responsible for creating all in game objects 
    and game loop in which all the logic is executed from other files as well 
    """
    get_ready(screen)

    paddle = Paddle(screen,250,450, 70, 10)

    while True:
        start_ball_vel_x = random.randint(-5,5)
        start_ball_vel_y = random.randint(-5,5)
        if start_ball_vel_x and start_ball_vel_y != 0: break

    ball = Ball(screen, 350,250, 8, start_ball_vel_x, start_ball_vel_y)

    bricks = []
    bricks_num = 18
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
    for x in range(6): unbreakable_bricks.append(Brick(screen, 90 * (x+1), 200, 50, 20, (255, 212, 5)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        if is_game_over(screen, lifes): break

        screen.blit(game_background_image, (0, 0))


        ball.check_wall_collision(window_width, window_height, lifes)
        if ball.check_paddle_collision(paddle.pos_x, paddle.pos_y, paddle.width, paddle.height):
            play_sound(sounds_dir + r'/arkpad.wav')
        if ball.check_brick_collision(bricks):
            play_sound(sounds_dir + r'/arkbrick.wav')
        if ball.check_brick_collision(unbreakable_bricks, "unbreakable"):
            play_sound(sounds_dir + r'/arkbrick.wav')

        ball.move()
        paddle.move(pygame.key.get_pressed())

        paddle.draw()
        ball.draw()
        for life in lifes: life.draw()

        destroyed_bricks_counter = 0
        for brick in bricks: 
            brick.draw()
            if brick.Is_visible() == False: destroyed_bricks_counter+=1
        for u_brick in unbreakable_bricks: u_brick.draw()

        if destroyed_bricks_counter == bricks_num: 
            game_is_won() 
            break
        pygame.display.update()
        clock.tick(60)
    
if __name__ == "__main__":
    main_menu(screen,window_width, window_height)

    