# ------------------------------------------------
# Dateiname: hangman.py
# Version: 1.1
# Funktion: Galgenmännchen-Spiel
# Autor: AP
# Datum der letzten Änderung: 24.01.2024
# ------------------------------------------------

# Modules used --------------------------------------------------------------------------------------------

import pygame 
import random
import sys
import subprocess
import math


# Definition of Functions ------------------------------------------------------------------------------------

def draw_title_screen():
    global back_button_r
    screen.fill('#090909')
    screen.blit(background, (-20,0))
    back_button_r = back_button.get_rect(midleft = (10,20))
    screen.blit(back_button, back_button_r)
    title = font_title.render('Hangman', True, (64,64,64))
    screen.blit(title, (screen_width/2 - title.get_width()/2, 40)) 
    screen.blit(reaper, (screen_width/2 - reaper.get_width()/2+20, screen_height/2 - reaper.get_height()/2+80)) 
    if score >= 0:
        your_score = font_text.render('YOUR SCORE: ' + str(score), True, (64,64,64))
        screen.blit(your_score, (screen_width/2 - your_score.get_width()/2, 200)) 
    start_game = font_text.render('PRESS [ENTER] TO START', True, (64,64,64))
    screen.blit(start_game,(screen_width/2 - start_game.get_width()/2, 750))

    if score >= 10:
        screen.blit(background, (-20,0))
        screen.blit(back_button, back_button_r)
        screen.blit(title, (screen_width/2 - title.get_width()/2, 40)) 
        screen.blit(your_score, (screen_width/2 - your_score.get_width()/2, 200)) 
        screen.blit(reaper_dead, (screen_width/2 - reaper_dead.get_width()/2+20, screen_height/2 - reaper_dead.get_height()/2+80)) 
        screen.blit(start_game,(screen_width/2 - start_game.get_width()/2, 750))
        pygame.display.flip()
        with open(achievement_file, 'r') as file:
            content = file.read()
        search_pattern = f'{achievement_key} = False'
        if search_pattern in content:
            content = content.replace(search_pattern, f'{achievement_key} = True')
        with open(achievement_file, 'w') as file:
            file.write(content)

    
        
def draw_elements():
    screen.fill('#090909')
    screen.blit(background, (screen_width/2 - background.get_width()/2, 0))
   
    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = font_word.render(display_word, 1, (240,240,240))
    screen.blit(text, (screen_width/2 - text.get_width()/2, 150))

    # draw buttons
    for letter in letters:
        x, y, character, visible = letter
        text = font_button.render(character, True, (220,220,220))
        if visible:
            pygame.draw.circle(screen, (245,245,245), (x,y), radius, 3)
            screen.blit(text, (x - text.get_width() / 2, y - text.get_width() / 2))

    screen.blit(gallows[gallows_status], (screen_width/2 - gallows[gallows_status].get_width()/2,230))
    pygame.display.update()


def display_message(message):
    pygame.time.delay(1000)
    screen.fill('grey')
    text = font_word.render(message, 1, 'black')
    screen.blit(text, (screen_width/2 - text.get_width()/2, screen_height/2 - text.get_height()/2))
    
    pygame.display.update()
    pygame.time.delay(1500)

def reset():
    global game_active, gallows_status
    global hangman_status, word, guessed, letters
    letters = []
    for i in range(26):
        x = buttons_tl_x + gap * 2 + ((radius * 2 + gap) * (i % 13))
        y = buttons_tl_y + ((i // 13) * (gap + radius * 2))
        letters.append([x, y, chr(A + i), True])
    hangman_status = 0
    word = random.choice(words)
    guessed = []
    gallows_status = 0
    game_active = False

# Definition of Variables ----------------------------------------------------------------------------------------------
    
pygame.init()

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Hangman')
clock = pygame.time.Clock()
framerate = 60
game_active = False
achievement_file = 'achievement.txt'
achievement_key = 'Gallows'

screen.fill('#090909')

hangman_status = 0
words = ["PROGRAMMIEREN", "ANSIBLE", "PYTHON", "DOCKER", 'GERRY', 'SMAUG', 'LINUX', 'KLETTERGARTEN', 
         'BOGENPARCOUR', 'KLETTERSTEIG', 'FINJA', 'GHOSTBUSTERS', 'ALIEN', 'WHISKY' ]
word = random.choice(words)
guessed = []
gallows_status = 0
score = 0

# button variables
radius = 20
gap = 15
#number the upper A is adressed with
A = 65
letters = []
buttons_tl_x = round((screen_width - (radius * 2 + gap) * 13) / 2)
buttons_tl_y = 700

for i in range (26):
        x = buttons_tl_x + gap * 2 + ((radius * 2 + gap) * (i % 13))
        y = buttons_tl_y + ((i // 13) * (gap + radius * 2))
        letters.append([x, y, chr(A + i), True])

# import Fonts ---------------------------------------------------------------------------------------------------------

font_title = pygame.font.Font(r'fonts\who asks satan.ttf', 90)
font_button = pygame.font.Font(r'fonts\Strange Path.ttf', 15)
font_word = pygame.font.Font(r'fonts\Strange Path.ttf', 30)
font_text = pygame.font.Font(r'fonts\Strange Path.ttf', 20)

# import Images --------------------------------------------------------------------------------------------------------

background = pygame.transform.rotozoom(pygame.image.load(r'graphics\gallows\dark_bg.png').convert_alpha(), 0, 1)
back_button = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\back.png').convert_alpha(), 0, 0.05)
reaper = pygame.transform.rotozoom(pygame.image.load(r'graphics\gallows\reaper.png').convert_alpha(), 0, 0.4)
reaper_dead = pygame.transform.rotozoom(pygame.image.load(r'graphics\gallows\reaper_dead.png').convert_alpha(), 0, 0.4)
# shorter way to import numbered images
gallows = []
for i in range(7):
    image = pygame.transform.rotozoom(pygame.image.load(r'graphics\gallows\gallows' +  str(i) + '.png'), 0, 0.8)
    gallows.append(image)



# import Music ----------------------------------------------------------------------------------------

bg_music = pygame.mixer.Sound(r'sounds\tchaikovsky_the_seasons_march_songofthelark.mp3')
bg_music.set_volume(0.08)
bg_music.play(loops= -1)


# Game Loop ------------------------------------------------------------------------------------------------------------

while True:
    clock.tick(framerate)

    for event in pygame.event.get():
        # close game
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, character, visible = letter
                    if visible:
                        distance =  math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                        if distance < radius:
                            print(f"Clicked on {character}")
                            letter[3] = False
                            guessed.append(character)
                            if character not in word:
                                gallows_status += 1

            draw_elements()

            won = True
            for letter in word:
                if letter not in guessed:
                    won = False
                    break
            
            if won:
                display_message('YOU WON!')
                score += 1
                pygame.time.delay(2000)
                reset()
              
            if gallows_status == 6:
                display_message('YOU LOST!')
                pygame.time.delay(2000)
                reset()


             
        
        else:
            draw_title_screen()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                
                game_active = True
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_r.collidepoint(event.pos):
                    pygame.quit()
                    subprocess.run(['python', 'menu.py'])
                    sys.exit()

    pygame.display.update()
    
