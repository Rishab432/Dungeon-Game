# pygame template

import pygame
import random

pygame.init()
pygame.font.init()

WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0,162,232)
RED = (237,28,36)
MAROON = (136,0,21)
PINK = (255,174,201)
ORANGE = (255,127,39)
YELLOW = (255,242,0)
GREY = (127,127,127)
PURPLE = (163,73,164)

global complete1
complete1 = False
global complete2
complete2 = False
global complete3
complete3 = False
global complete4
complete4 = False
# ---------------------------
def main_base():
    player_x = 305
    player_y = 225
    hearts = 3
    running = True
    while running:
        
        screen.fill(BLACK)  # always the first drawing command
        pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)


        if hearts >= 1:
            pygame.draw.rect(screen, RED, [88, 5, 10, 10])
        if hearts >= 2:
            pygame.draw.rect(screen, RED, [103, 5, 10, 10])
        if hearts == 3:
            pygame.draw.rect(screen, RED, [118, 5, 10, 10])
        player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])

        door1 = pygame.draw.rect(screen, RED, [220, 3, 200, 10])
        if player.colliderect(door1):
            dungeon1()
        global complete1
        if complete1:
            door2 = pygame.draw.rect(screen, RED, [547, 140, 10, 200])
            if player.colliderect(door2):
                dungeon2()
        global complete2
        if complete2:
            door3 = pygame.draw.rect(screen, RED, [220, 467, 200, 10])
            if player.colliderect(door3):
                dungeon3()
        global complete3
        if complete3:
            door4 = pygame.draw.rect(screen, RED, [83, 140, 10, 200])
            if player.colliderect(door4):
                dungeon4()
        global complete4
        if complete4:
            door5 = pygame.draw.rect(screen, RED, [305, 300, 30, 30], 5)
            if player.colliderect(door5):
                dungeon5()

        if player_x < 83:
            player_x = 83
        if player_x > 527:
            player_x = 527
        if player_y < 3:
            player_y = 3
        if player_y > 447:
            player_y = 447

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player_x > 83:
                player_x -= 3
        if keys[pygame.K_RIGHT]:
            if player_x < 527:
                player_x += 3
        if keys[pygame.K_UP]:
            if player_y > 3:
                player_y -= 3
        if keys[pygame.K_DOWN]:
            if player_y < 447:
                player_y += 3
        if keys[pygame.K_SPACE]:
            pass
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(30)
    #---------------------------

def dungeon1():
    room_list = []
    enemies = 0
    boss = 1
    room0 = [None, None, None, 1, 0]
    room_list.append(room0)
    room1 = [None, 0, 2, None, 1]
    room_list.append(room1)
    room2 = [1, 3, None, None, 2]
    room_list.append(room2)
    room3 = [None, 4, None, 2, 2]
    room_list.append(room3)
    room4 = [5, None, None, 3, 3]
    room_list.append(room4)
    room5 = [6, None, 4, None, 3]
    room_list.append(room5)
    room6 = [None, None, 5, 7, 3]
    room_list.append(room6)
    room7 = [None, 6, None, 8, 4]
    room_list.append(room7)
    room8 = [None, 7, None, None, 100]
    room_list.append(room8)
    current_room = 0
    next_room = 0
    enemies_list = [0, 1, 2, 3, 4]
    enemy1_x = 100
    enemy1_y = 20
    enemy2_x = 510
    enemy2_y = 20
    enemy3_x = 100
    enemy3_y = 430
    enemy4_x = 510
    enemy4_y = 430
    magic = 0, 0, 0, 0
    damage = True
    boss = 0
    
    player_x = 305
    player_y = 225
    hearts = 3
    running = True
    while running:
        
        screen.fill(BLACK)  # always the first drawing command
        pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)

        if hearts >= 1:
            pygame.draw.rect(screen, RED, [88, 5, 10, 10])
        if hearts >= 2:
            pygame.draw.rect(screen, RED, [103, 5, 10, 10])
        if hearts == 3:
            pygame.draw.rect(screen, RED, [118, 5, 10, 10])
        if hearts == 0:
            main_base()
        player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])

        # enemies = room_list[current_room][4]
        # if enemies == 1:
        #     enemy1 = pygame.draw.rect(screen, RED, [enemy1_x, enemy1_y, 30, 30])
        #     if enemy1_x < player_x:
        #         enemy1_x += 1
        #     elif enemy1_x > player_x:
        #         enemy1_x -= 1
        #     if enemy1_y < player_y:
        #         enemy1_y += 1
        #     elif enemy1_y > player_y:
        #         enemy1_y -= 1
        #     if enemy1.colliderect(player):
        #         if damage == True:
        #             hearts -= 1
        #             if enemy1_x < player_x and player_x < 507:
        #                 player_x += 20
        #             elif enemy1_x > player_x and player_x > 103:
        #                 player_x -= 20
        #             if enemy1_y < player_y and player_y > 23:
        #                 player_y += 20
        #             elif enemy1_y > player_y and player_y < 427:
        #                 player_y -= 20
        #             damage = False
        #     else: 
        #         damage = True
        #     if enemy1.colliderect(magic):
        #         enemies == 0
        #         enemy1 = pygame.draw.rect(screen, RED, [1000, 1000, 30, 30])
            

        if enemies == 0:
            if room_list[current_room][0] != None:
                next_room = room_list[current_room][0]
                door1 = pygame.draw.rect(screen, RED, [220, 3, 200, 10])
                if player.colliderect(door1):
                    player_x = 305
                    player_y = 437
                    current_room = next_room
            if room_list[current_room][1] != None:
                next_room = room_list[current_room][1]
                door2 = pygame.draw.rect(screen, RED, [547, 140, 10, 200])
                if player.colliderect(door2):
                    player_x = 93
                    player_y = 225
                    current_room = next_room
            if room_list[current_room][2] != None:
                next_room = room_list[current_room][2]
                door3 = pygame.draw.rect(screen, RED, [220, 467, 200, 10])
                if player.colliderect(door3):
                    player_x = 305
                    player_y = 13
                    current_room = next_room
            if room_list[current_room][3] != None:
                next_room = room_list[current_room][3]
                door4 = pygame.draw.rect(screen, RED, [83, 140, 10, 200])
                if player.colliderect(door4):
                    player_x = 517
                    player_y = 225
                    current_room = next_room
        if boss == 0:
            if room_list[current_room] == room8:
                dungeon_door = pygame.draw.rect(screen, RED, [305, 225, 30, 30], 3)
                if player.colliderect(dungeon_door):
                    global complete1
                    complete1 = True
                    main_base()

        if player_x < 83:
            player_x = 83
        if player_x > 527:
            player_x = 527
        if player_y < 3:
            player_y = 3
        if player_y > 447:
            player_y = 447

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if player_x > 83:
                player_x -= 3
        if keys[pygame.K_RIGHT]:
            if player_x < 527:
                player_x += 3
        if keys[pygame.K_UP]:
            if player_y > 3:
                player_y -= 3
        if keys[pygame.K_DOWN]:
            if player_y < 447:
                player_y += 3

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    if keys[pygame.K_UP]:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-5, player_y-10, 40, 3])
                    elif keys[pygame.K_DOWN]:
                        magic = pygame.draw.line(screen, WHITE, [player_x-5, player_y+40, 40, 3], 3)
                    elif keys[pygame.K_LEFT]:
                        magic = pygame.draw.line(screen, WHITE, [player_x-10, player_y-5], [player_x-10, player_y+35], 3)
                    elif keys[pygame.K_RIGHT]:
                        magic = pygame.draw.line(screen, WHITE, [player_x+40, player_y-5], [player_x+40, player_y+35], 3)
                    else:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-10, 50, 50], 3)
                        # if enemy1.colliderect(magic):
                        #     print("True")
                        #     enemies == 0
                        #     enemy1 = pygame.draw.rect(screen, RED, [1000, 1000, 30, 30])
            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(30)

    complete1 = True
    main_base()
def dungeon2():
    global complete2
    complete2 = True
    main_base()
def dungeon3():
    global complete3
    complete3 = True
    main_base()
def dungeon4():
    global complete4
    complete4 = True
    main_base()
def dungeon5():
    main_base()

main_base()
