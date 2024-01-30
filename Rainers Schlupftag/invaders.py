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

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Error 404')
screen.fill((25,25,25))
achievement_file = 'achievement.txt'
achievement_key = 'Invaders'


# import Fonts ---------------------------------------------------------------------------------------------------------

font_text = pygame.font.Font(r'fonts\Pixeltype.ttf', 30)
font_title = pygame.font.Font(r'fonts\Pixeled.ttf', 40)


# import Images --------------------------------------------------------------------------------------------------------


back_button_s = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\back.png').convert_alpha(), 0, 0.05)
button_click = pygame.transform.rotozoom(pygame.image.load(r'graphics\invaders\click.png').convert_alpha(), 0, 0.4)

# generate rectangles and surfaces --------------------------------------------------------------------------------------

title_s = font_title.render('404 -  GAME NOT FOUND', True, (244,244,244))
title_r = title_s.get_rect(topleft = (20,20))

back_button_r = back_button_s.get_rect(midleft = (10,20))

text = [font_text.render(r'\   The developer ran out of time', True, (244,244,244)), 
        font_text.render('\\', True, (244,244,244)),
        font_text.render(r'\   The issue could be that the developer did not start early enough.', True, (244,244,244)),
        font_text.render(r'\   Or there was something more important to do.', True, (244,244,244)),
        font_text.render(r'\   Maybe the developers house burned down.', True, (244,244,244)), 
        font_text.render(r'\   Or the whole world exploded.', True, (244,244,244)),
        font_text.render(r'\   . . .', True, (244,244,244)),
        font_text.render(r'\   What do I know, I am just a simple computer program.', True, (244,244,244)),
        font_text.render(r'\   Or maybe the developer was too lazy...', True, (244,244,244)),
        font_text.render(r'\   Yes, that is it.', True, (244,244,244)),
        font_text.render('\\', True, (244,244,244)),
        font_text.render('\\', True, (244,244,244)),
        font_text.render(r'\  But I think you should get the achievement anyway.', True, (244,244,244)),
        font_text.render(r'\   For at least trying to start such an annoying game.', True, (244,244,244)),
        font_text.render(r'\   Only click the button.', True, (244,244,244)),]



button_click_r = button_click.get_rect(center = (400,700))



# write achievement status ----------------------------------------------------------------------------------------------

with open(achievement_file, 'r') as file:
    content = file.read()
search_pattern = f'{achievement_key} = False'
if search_pattern in content:
    content = content.replace(search_pattern, f'{achievement_key} = True')
with open(achievement_file, 'w') as file:
    file.write(content)


# draw elements---------------------------------------------------------------------------------------------------------
distance = 0
for line in text:
    distance += 22
    screen.blit(line, (20, 200+line.get_height() + distance))  

# screen_erfolge.blit(back_button_s, back_button_r)
screen.blit(title_s, title_r)
screen.blit(button_click, button_click_r)




# Game Loop ------------------------------------------------------------------------------------------------------------

while True:

    for event in pygame.event.get():
        # close game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_click_r.collidepoint(event.pos):
                with open(achievement_file, 'r') as file:
                    content = file.read()
                search_pattern = f'{achievement_key} = False'
                if search_pattern in content:
                    content = content.replace(search_pattern, f'{achievement_key} = True')
                with open(achievement_file, 'w') as file:
                    file.write(content)
                pygame.quit()
                subprocess.run(['python', 'menu.py'])
                sys.exit()
    
    pygame.display.update()
    clock.tick(framerate)