# ------------------------------------------------
# Dateiname: Jumper.py
# Version: 1.0
# Funktion: jump over enemies and try to stay alive as long as you can
# Autor: AP
# Datum der letzten Änderung: 21.01.2024
# ------------------------------------------------


# Modules used ------------------------------------------------------------------------------------------------------------------------------

import pygame
import subprocess
import sys
from random import randint


# Definition of Functions -------------------------------------------------------------------------------------------------------------------

def display_score():
    current_time = int(pygame.time.get_ticks() /1000) - start_time 
    score_surf = main_font.render(str(current_time), False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstactle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if score > 50: obstacle_rect.x -= 1
            if score > 100: obstacle_rect.x -= 1
            if score > 150: obstacle_rect.x -= 1
            if obstacle_rect.bottom == 450: screen.blit(dog_surf, obstacle_rect) 
            elif obstacle_rect.bottom == 451: screen.blit(coopa_surf, obstacle_rect) 
            else: 
                screen.blit(goomba_surf, obstacle_rect) 

        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else:
        return []
            
def collisions(player, obstacles):
    global player_rect
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                player_surf = player_death_surf
                player_rect = player_surf.get_rect(topleft = (player_rect.x,player_rect.y))
                screen.blit(player_death_surf, player_rect)
                pygame.display.flip()  # Bild sofort aktualisieren
                bg_music.stop()
                burn_sound.play()
                pygame.time.delay(2000)  # Pause für 2 Sekunden
                bg_music.play(loops=-1)
                return False
    return True

def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 450:
        player_surf = player_jump_surf
                
    else:
        player_index += 0.08
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]
    

# Definition of variables -------------------------------------------------------------------------------------------------------------------

# improves sound output (44100 Hz, 16bit, stereo, buffer)
pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
pygame.display.set_caption('Super Jumper')
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
framerate = 60
game_active = False
sound_on = True  
victory_sound_played = False
start_time = 0
score = 0

achievement_file = 'achievement.txt'
achievement_key = 'Jumper'

obstacle_rect_list = []

# Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer, 1500)

dog_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(dog_animation_timer, 100)

goomba_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(goomba_animation_timer, 100)

coopa_animation_timer = pygame.USEREVENT + 4
pygame.time.set_timer(coopa_animation_timer, 200)







# import Fonts --------------------------------------------------------------------------------------------------------------------------------
main_font = pygame.font.Font(r'fonts\Pixeltype.ttf', 50)

# import Sound --------------------------------------------------------------------------------------------------------------------------------
bg_music = pygame.mixer.Sound(r'sounds\music.wav')
bg_music.set_volume(0.04)
bg_music.play(loops= -1)
jump_sound = pygame.mixer.Sound(r'sounds\jump.mp3')
jump_sound.set_volume(0.07)
burn_sound = pygame.mixer.Sound(r'sounds\burn.wav')
burn_sound.set_volume(0.2)
victory_sound = pygame.mixer.Sound(r'sounds\victory.wav')
victory_sound.set_volume(0.2)


# import Images --------------------------------------------------------------------------------------------------------------------------------

# background images
background_surf = pygame.image.load(r'graphics\environment\SMW_background.png').convert_alpha()
background_start_surf = pygame.image.load(r'graphics\environment\SMW_background_start.png').convert_alpha()
ground_surf = pygame.image.load(r'graphics\environment\SMW_ground.png')
busch_small_surf = pygame.image.load(r'graphics\environment\SMW_bush_small.png')
bush_big_surf = pygame.image.load(r'graphics\environment\SMW_bush_big.png')
sound_on_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\sound_on.png').convert_alpha(), 0, 0.1)
sound_off_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\sound_off.png').convert_alpha(), 0, 0.1)
back_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\back.png').convert_alpha(), 0, 0.06)

# Player images
player_walk1_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\mario\SMW_Mario_walk_right_1.png').convert_alpha(), 0, 0.125)
player_walk2_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\mario\SMW_Mario_walk_right_2.png').convert_alpha(), 0, 0.125)
player_walk3_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\mario\SMW_Mario_walk_right_3.png').convert_alpha(), 0, 0.125)
player_walk = [player_walk2_surf, player_walk3_surf, player_walk2_surf, player_walk1_surf]
player_index = 0
player_jump_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\mario\SMW_Mario_jump_right.png').convert_alpha(), 0, 0.125)
player_start_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\mario\SMW_Mario_victory.png').convert_alpha(), 0, 0.125)
player_death_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\mario\SMW_Mario_burned.png').convert_alpha(), 0, 0.125)
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(bottomleft = (80,450))
player_gravity = 0


# achivement images
stars1_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\SMW_stars_1.png').convert_alpha(), 0, 0.2)
stars2_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\SMW_stars_2.png').convert_alpha(), 0, 0.2)
stars3_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\SMW_stars_3.png').convert_alpha(), 0, 0.2)
stars4_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\title_screen\SMW_stars_4.png').convert_alpha(), 0, 0.2)
stars_shine = [stars1_surf, stars2_surf, stars3_surf, stars4_surf]
stars_index = 0
stars_surf = stars_shine[stars_index]


# enemy images
dog1_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\dog\SMW_dog_walk_left_1.png').convert_alpha(), 0, 1)
dog2_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\dog\SMW_dog_walk_left_2.png').convert_alpha(), 0, 1)
dog3_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\dog\SMW_dog_walk_left_3.png').convert_alpha(), 0, 1)
dog4_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\dog\SMW_dog_walk_left_4.png').convert_alpha(), 0, 1)
dog_walk = [dog1_surf, dog2_surf, dog3_surf, dog4_surf]
dog_index = 0
dog_surf = dog_walk[dog_index]

goomba1_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\goomba\SMW_goomba_left_1.png').convert_alpha(), 0, 0.15)
goomba2_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\goomba\SMW_goomba_left_2.png').convert_alpha(), 0, 0.15)
goomba_walk = [goomba1_surf, goomba2_surf]
goomba_index = 0
goomba_surf = goomba_walk[goomba_index]

coopa1_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\coopa\SMW_Coopa_red_walk_left_1.png').convert_alpha(), 0, 0.1)
coopa2_surf = pygame.transform.rotozoom(pygame.image.load(r'graphics\coopa\SMW_Coopa_red_walk_left_2.png').convert_alpha(), 0, 0.1)
coopa_walk = [coopa1_surf, coopa2_surf]
coopa_index = 0
coopa_surf = coopa_walk[coopa_index]




# Gameloop ---------------------------------------------------------------------------------------------------------------------------------

while True:
    
    for event in pygame.event.get():
        # game quit
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            exit()

        if game_active:
            # Player jump
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom == 450:
                    player_gravity = -20
                    jump_sound.play()

        else:
            # in title screen, starting the game
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_active = True                   
                    pygame.time.delay(500)
                    # starts the timer for the score
                    start_time = int(pygame.time.get_ticks() /1000)

        if game_active:
            # randomly chooses the enemy type, depending on the score
            if event.type == obstacle_timer:
                random_number = randint(0,2)
                if random_number == 0 and score >= 10:
                    obstacle_rect_list.append(goomba_surf.get_rect(bottomright = (randint(900,1100),250)))
                elif random_number == 1 and score >= 30:
                    obstacle_rect_list.append(coopa_surf.get_rect(bottomright = (randint(900,1100), 451)))
                else:
                    obstacle_rect_list.append(dog_surf.get_rect(bottomright = (randint(900,1100), 450)))

            if event.type == dog_animation_timer:
                if dog_index == 0: dog_index = 1
                elif dog_index == 1: dog_index = 2
                elif dog_index == 2: dog_index = 3
                else: dog_index = 0
                dog_surf = dog_walk[dog_index]

            if event.type == goomba_animation_timer:
                if goomba_index == 0: goomba_index = 1
                else: goomba_index = 0
                goomba_surf = goomba_walk[goomba_index]
            
            if event.type == coopa_animation_timer:
                if coopa_index == 0: coopa_index = 1
                else: coopa_index = 0
                coopa_surf = coopa_walk[coopa_index]

    if game_active:    
        # inaktiver Hintergrund
        screen.fill((107,204,232))
        screen.blit(background_surf, (0,0))
        screen.blit(ground_surf, (0,450))
        sound_surf = sound_on_surf if sound_on else sound_off_surf
        movement_surf = main_font.render('Press [SPACE] to jump', True, (64,64,64))
        movement_rect = movement_surf.get_rect(bottomleft = (10,590))
        screen.blit(movement_surf, movement_rect)
        

        score = display_score()

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 450:
            player_rect.bottom = 450
        player_animation()
        screen.blit(player_surf, player_rect)
        
        # Obstacle movement
        obstacle_rect_list = obstactle_movement(obstacle_rect_list)
        # collision
        game_active = collisions(player_rect, obstacle_rect_list)

        

    else:
        obstacle_rect_list.clear()
        
        player_rect.midbottom = (80,450)
        player_gravity = 0
        screen.fill((107,204,232))
        screen.blit(background_start_surf, (0,0))
        screen.blit(ground_surf, (0,450))

        sound_surf = sound_on_surf
        sound_rect = sound_surf.get_rect(center= (770, 30))
        screen.blit(sound_surf, sound_rect)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if sound_rect.collidepoint(event.pos) and sound_on == True:
                bg_music.stop()
                sound_on = False
                sound_surf = sound_off_surf
            elif sound_rect.collidepoint(event.pos) and sound_on == False:
                bg_music.play(loops=-1)
                sound_on = True
                sound_surf = sound_on_surf
                
            screen.blit(sound_surf, sound_rect)
 
        
        back_rect = back_surf.get_rect(midleft = (20,30))
        screen.blit(back_surf, back_rect)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if back_rect.collidepoint(event.pos):
                pygame.quit()
                subprocess.run(['python', 'menu.py'])
                sys.exit()

        title_surf = main_font.render('Super Jumper', False, (64,64,64))
        title_rect = title_surf.get_rect(center = (400,50))
        
        title_score_surf = main_font.render('Your Score: ' + str(score), False, (202,4,34))
        title_score_rect = title_score_surf.get_rect(center = (400,200))
        stars_rect = stars_surf.get_rect(center = (400,420))
        player_start_rect = player_start_surf.get_rect(midbottom = (400,450))
        start_game_surf = main_font.render('START GAME?    [ENTER]', False, (64,64,64))
        start_game_rect = start_game_surf.get_rect(midbottom = (400,550))

        screen.blit(title_surf, title_rect)
        if score > 0: screen.blit(title_score_surf, title_score_rect)
        
        stars_index += 0.06
        if stars_index >= len(stars_shine): stars_index = 0
        stars_surf = stars_shine[int(stars_index)]

        if score >= 150 and not victory_sound_played:
            victory_sound.play()
            victory_sound_played = True
        if score >= 150:
            screen.blit(stars_surf, stars_rect)
            with open(achievement_file, 'r') as file:
                content = file.read()
                search_pattern = f'{achievement_key} = False'
                if search_pattern in content:
                    content = content.replace(search_pattern, f'{achievement_key} = True')
            with open(achievement_file, 'w') as file:
                file.write(content)

        screen.blit(player_start_surf, player_start_rect)
        screen.blit(start_game_surf, start_game_rect)

    clock.tick(framerate)
    pygame.display.update()