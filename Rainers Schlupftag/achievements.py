# ------------------------------------------------
# Dateiname: achievements.py
# Version: 1.0
# Funktion: Erfolgsübersicht des Spiele-Geschenkes für Rainer
# Autor: AP
# Datum der letzten Änderung: 23.01.2024
# ------------------------------------------------

# Modules used --------------------------------------------------------------------------------------------------------

import pygame
import sys
import subprocess


# Definition of Variables ----------------------------------------------------------------------------------------------

pygame.quit()
pygame.init()

screen_width = 800
screen_height = 800
framerate = 60
clock = pygame.time.Clock()

screen_erfolge = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Erfolge')
screen_erfolge.fill('grey')
achievement_file = 'achievement.txt'


# import Fonts ---------------------------------------------------------------------------------------------------------

font_text = pygame.font.Font(r'fonts\spacerangercond.ttf', 50)
font_alien = pygame.font.Font(r'fonts\Alien_Hieroglyph.ttf', 60)
font_erfolg = pygame.font.Font(r'fonts\SPACE.ttf', 40)


# import Images --------------------------------------------------------------------------------------------------------

bg_erfolge_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\starfield.png').convert_alpha(), 0, 1)
jumper_tile_bw_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\jumper_tile_bw.png').convert_alpha(), 0, 0.2)
snake_tile_bw_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\snake_tile_bw.png').convert_alpha(), 0, 0.2)
invaders_tile_bw_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\invaders_tile_bw.png').convert_alpha(), 0, 0.2)
gallows_tile_bw_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\gallows_tile_bw.png').convert_alpha(), 0, 0.2)
back_button_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\back.png').convert_alpha(), 0, 0.05)

# generate rectangles and surfaces --------------------------------------------------------------------------------------

title_s = font_erfolg.render('Deine Erfolge', True, (157,140,206))
title_r = title_s.get_rect(center = (400,80))
bg_erfolge_r = bg_erfolge_s.get_rect(center = (400,400))
back_button_r = back_button_s.get_rect(midleft = (10,20))
jumper_tile_bw_r = jumper_tile_bw_s.get_rect(midleft = (100,250))
snake_tile_bw_r = snake_tile_bw_s.get_rect(midleft = (100,400))
gallows_tile_bw_r = gallows_tile_bw_s.get_rect(midleft = (100,550))
invaders_tile_bw_r = invaders_tile_bw_s.get_rect(midleft = (100,700))
frame_jumper_r = pygame.Rect(jumper_tile_bw_r.left -10, jumper_tile_bw_r.top -10 , 620, jumper_tile_bw_r.height +20)
frame_snake_r = pygame.Rect(snake_tile_bw_r.left -10, snake_tile_bw_r.top -10 , 620, snake_tile_bw_r.height +20)
frame_gallows_r = pygame.Rect(gallows_tile_bw_r.left -10, gallows_tile_bw_r.top -10 , 620, gallows_tile_bw_r.height +20)
frame_invaders_r = pygame.Rect(invaders_tile_bw_r.left -10, invaders_tile_bw_r.top -10 , 620, invaders_tile_bw_r.height +20)
jumper_erfolg_s = font_alien.render('5WQ6Q-HGZWK-XXXX', True, (25,25,25))
snake_erfolg_s = font_alien.render('WK7WK-G04GJ-XXXX', True, (25,25,25))
gallows_erfolg_s = font_alien.render('activate in', True, (25,25,25))
invaders_erfolg_s = font_alien.render('steam', True, (25,25,25))
jumper_erfolg_r = jumper_erfolg_s.get_rect(center = (frame_jumper_r.centerx+50, frame_jumper_r.centery+5))
snake_erfolg_r = snake_erfolg_s.get_rect(center = (frame_snake_r.centerx+50, frame_snake_r.centery+5))
gallows_erfolg_r = gallows_erfolg_s.get_rect(center = (frame_gallows_r.centerx+50, frame_gallows_r.centery+5))
invaders_erfolg_r = invaders_erfolg_s.get_rect(center = (frame_invaders_r.centerx+50, frame_invaders_r.centery+5))


# check achievement status ----------------------------------------------------------------------------------------------

with open(achievement_file, 'r') as file:
        content = file.read()
if "Jumper = True" in content:
    jumper_erfolg_s = font_text.render('5WQ6Q-HGZWK-0JLKG', True, (25,25,25))
    jumper_tile_bw_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\jumper_tile.png').convert_alpha(), 0, 0.2)
if "Snake = True" in content:
    snake_erfolg_s = font_text.render('WK7WK-G04GJ-FLL4H', True, (25,25,25))
    snake_tile_bw_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\snake_tile.png').convert_alpha(), 0, 0.2)
if "Gallows = True" in content:
    gallows_erfolg_s = font_text.render('activate in', True, (25,25,25))
    gallows_tile_bw_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\gallows_tile.png').convert_alpha(), 0, 0.2)
if "Invaders = True" in content:
    invaders_erfolg_s = font_text.render('steam', True, (25,25,25))
    invaders_tile_bw_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\invaders_tile.png').convert_alpha(), 0, 0.2)


# draw elements---------------------------------------------------------------------------------------------------------
    
screen_erfolge.blit(bg_erfolge_s, bg_erfolge_r)
screen_erfolge.blit(back_button_s, back_button_r)
screen_erfolge.blit(title_s, title_r)
screen_erfolge.blit(jumper_tile_bw_s, jumper_tile_bw_r)
screen_erfolge.blit(snake_tile_bw_s, snake_tile_bw_r)
screen_erfolge.blit(gallows_tile_bw_s, gallows_tile_bw_r)
screen_erfolge.blit(invaders_tile_bw_s, invaders_tile_bw_r)
pygame.draw.rect(screen_erfolge, (79,1,131), frame_jumper_r, 5, 10)
pygame.draw.rect(screen_erfolge, (61,1,101), frame_snake_r, 5, 10)
pygame.draw.rect(screen_erfolge, (51,0,85), frame_gallows_r, 5, 10)
pygame.draw.rect(screen_erfolge, (44,0,72), frame_invaders_r, 5, 10)
screen_erfolge.blit(jumper_erfolg_s, jumper_erfolg_r)
screen_erfolge.blit(snake_erfolg_s, snake_erfolg_r)
screen_erfolge.blit(gallows_erfolg_s, gallows_erfolg_r)
screen_erfolge.blit(invaders_erfolg_s, invaders_erfolg_r)


# Game Loop ------------------------------------------------------------------------------------------------------------

while True:

    for event in pygame.event.get():
        # close game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_button_r.collidepoint(event.pos):
                pygame.quit()
                subprocess.run(['python', 'menu.py'])
                sys.exit()
    
    pygame.display.update()
    clock.tick(framerate)