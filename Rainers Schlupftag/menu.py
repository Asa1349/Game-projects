# ------------------------------------------------
# Dateiname: menu.py
# Version: 1.0
# Funktion: Menü des Spiele-Geschenkes für Rainer
# Autor: AP
# Datum der letzten Änderung: 23.01.2024
# ------------------------------------------------

# Modules used ---------------------------------------------------------------------------------------------------------

import pygame
import sys
import subprocess


# Definition of Functions ----------------------------------------------------------------------------------------------

def click_erfolge():
    pygame.quit()
    subprocess.run(['python', 'achievements.py'])
    sys.exit()

def click_jumper():
    pygame.quit()
    subprocess.run(['python', 'jumper.py'])
    sys.exit()
    
def click_snake():
    pygame.quit()
    subprocess.run(['python', 'snake.py'])
    sys.exit()

def click_gallows():
    pygame.quit()
    subprocess.run(['python', 'hangman.py'])
    sys.exit()
 
def click_invaders():
    pygame.quit()
    subprocess.run(['python', 'invaders.py'])
    sys.exit()


# Definition of Variables ----------------------------------------------------------------------------------------------
    
pygame.init()

screen_width = 800
screen_height = 800
framerate = 60

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Happy Schlupftag Challenge')
clock = pygame.time.Clock()

screen.fill('Orange')

menu = True
erfolge = False
jumper = False
snake = False
gallows = False
invaders = False


# import Fonts ---------------------------------------------------------------------------------------------------------

font_title = pygame.font.Font(r'fonts\Peach Cake.otf', 50)
font_text = pygame.font.Font(r'fonts\Peach Cake.otf', 20)
font_games = pygame.font.Font(r'fonts\Peach Cake.otf', 30)
font_jumper = pygame.font.Font(r'fonts\Pixeltype.ttf', 50)
font_snake = pygame.font.Font(r'fonts\Mabook.ttf', 30)
font_gallows = pygame.font.Font(r'fonts\Storm Gust.ttf', 40)
font_invaders = pygame.font.Font(r'fonts\Pixeled.ttf', 16)


# import Images --------------------------------------------------------------------------------------------------------

background_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\background.png').convert_alpha(), 0, 1.2)
shrimp_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\shrimp.png').convert_alpha(), 20, 0.4)
jumper_tile_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\jumper_tile.png').convert_alpha(), 0, 0.2)
snake_tile_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\snake_tile.png').convert_alpha(), 0, 0.2)
invaders_tile_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\invaders_tile.png').convert_alpha(), 0, 0.2)
gallows_tile_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\gallows_tile.png').convert_alpha(), 0, 0.2)
magic_star_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\magic_star.gif').convert_alpha(), 0, 0.6)


# build rectangles and surfaces ----------------------------------------------------------------------------------------

background_r = background_s.get_rect(midtop = (400,0))
shrimp_r = shrimp_s.get_rect(topleft = (30,120))
title_s = font_title.render('Verdien Dir Dein Geschenk selbst!', True, (64,64,64))
title_r = title_s.get_rect(midtop = (400,30))
explanation_s = font_text.render('Du musst die Spiele spielen um Erfolge zu ', True, (64,64,64))
explanation1_s = font_text.render('  erzielen. Mit jedem Erfolg verdienst Du ', True, (64,64,64))
explanation2_s = font_text.render('    Dir einen Hinweis auf Dein Geschenk.', True, (64,64,64))
explanation_r = explanation_s.get_rect(topleft = (440,155))
explanation1_r = explanation_s.get_rect(topleft = (440,180))
explanation2_r = explanation_s.get_rect(topleft = (440,205))
magic_star_r = magic_star_s.get_rect(midtop = (600, 325))
erfolge_s = font_games.render('Erfolge', True, (64,64,64))
erfolge_r = erfolge_s.get_rect(midtop = (600,405))

jumper_tile_r = jumper_tile_s.get_rect(midleft = (50,550))
snake_tile_r = snake_tile_s.get_rect(midleft = (50,700))
gallows_tile_r = gallows_tile_s.get_rect(midleft = (440,550))
invaders_tile_r = invaders_tile_s.get_rect(midleft = (440,700))

jumper_name_s = font_jumper.render('Jumper', True, (64,64,64))
jumper_name_r = jumper_name_s.get_rect(midleft = (jumper_tile_r.right + 50,jumper_tile_r.centery+5))
snake_name_s = font_snake.render('Snake', True, (64,64,64))
snake_name_r = snake_name_s.get_rect(midleft = (snake_tile_r.right + 60,snake_tile_r.centery+4))
gallows_name_s = font_gallows.render('Hangman', True, (64,64,64))
gallows_name_r = gallows_name_s.get_rect(midleft = (gallows_tile_r.right + 35,gallows_tile_r.centery))
invaders_name_s = font_invaders.render('SPACE INVADERS', True, (64,64,64))
invaders_name_r = invaders_name_s.get_rect(midleft = (invaders_tile_r.right + 12,invaders_tile_r.centery))

frame_star_r = pygame.Rect(magic_star_r.left -35, magic_star_r.top -20 , magic_star_r.width +70, magic_star_r.height +70)
frame_jumper_r = pygame.Rect(jumper_tile_r.left -10, jumper_tile_r.top -10 , screen_width/2 -70, jumper_tile_r.height +20)
frame_snake_r = pygame.Rect(snake_tile_r.left -10, snake_tile_r.top -10 , screen_width/2 -70, snake_tile_r.height +20)
frame_gallows_r = pygame.Rect(gallows_tile_r.left -10, gallows_tile_r.top -10 , screen_width/2 -70, gallows_tile_r.height +20)
frame_invaders_r = pygame.Rect(invaders_tile_r.left -10, invaders_tile_r.top -10 , screen_width/2 -70, invaders_tile_r.height +20)


# draw elements --------------------------------------------------------------------------------------------------------

screen.blit(background_s, background_r)
screen.blit(shrimp_s, shrimp_r)
screen.blit(title_s, title_r)
screen.blit(explanation_s, explanation_r)
screen.blit(explanation1_s, explanation1_r)
screen.blit(explanation2_s, explanation2_r)
screen.blit(magic_star_s, magic_star_r)
screen.blit(erfolge_s, erfolge_r)
screen.blit(jumper_tile_s, jumper_tile_r)
screen.blit(snake_tile_s, snake_tile_r)
screen.blit(gallows_tile_s, gallows_tile_r)
screen.blit(invaders_tile_s, invaders_tile_r)

screen.blit(jumper_name_s, jumper_name_r)
screen.blit(snake_name_s, snake_name_r)
screen.blit(gallows_name_s, gallows_name_r)
screen.blit(invaders_name_s, invaders_name_r)

pygame.draw.rect(screen, (132,60,12), frame_star_r, 5, 10)
pygame.draw.rect(screen, (132,60,12), frame_jumper_r, 5, 10)
pygame.draw.rect(screen, (132,60,12), frame_snake_r, 5, 10)
pygame.draw.rect(screen, (132,60,12), frame_gallows_r, 5, 10)
pygame.draw.rect(screen, (132,60,12), frame_invaders_r, 5, 10)



# Game Loop ------------------------------------------------------------------------------------------------------------

while True:

    for event in pygame.event.get():
        # close game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
        # open games and achievement overview
        if event.type == pygame.MOUSEBUTTONDOWN:
            if frame_star_r.collidepoint(event.pos):
                click_erfolge()
                
            if frame_jumper_r.collidepoint(event.pos):
                click_jumper() 
 
            if frame_snake_r.collidepoint(event.pos):
                click_snake()
            
            if frame_gallows_r.collidepoint(event.pos):
                click_gallows()
            
            if frame_invaders_r.collidepoint(event.pos):
                click_invaders()
    
    pygame.display.update()
    clock.tick(framerate)