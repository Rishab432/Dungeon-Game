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

room_list1 = []
room1_0 = [None, None, None, 1, 0]
room1_1 = [None, 0, 2, None, 1]
room1_2 = [1, 3, None, None, 2]
room1_3 = [None, 4, None, 2, 2]
room1_4 = [5, None, None, 3, 3]
room1_5 = [6, None, 4, None, 3]
room1_6 = [None, None, 5, 7, 3]
room1_7 = [None, 6, None, 8, 4]
room1_8 = [None, 7, None, None, 100]
room_list1.append([room1_0, room1_1, room1_2, room1_3, room1_4, room1_5, room1_6, room1_7, room1_8])

room_list2 = []
room2_0 = [None, 1, None, None, 0]
room2_1 = [None, None, 2, 0, 1]
room2_2 = [1, 3, 4, None, 2]
room2_3 = [5, None, 6, 2, 2]
room2_4 = [2, None, None, None, 3]
room2_5 = [None, None, 3, None, 3]
room2_6 = [3, 7, None, None, 3]
room2_7 = [None, None, None, 6, 4]
room_list2.append([room2_0, room2_1, room2_2, room2_3, room2_4, room2_5, room2_6, room2_7])
    
room_list3 = []
room3_0 = [1, 2, None, None, 0]
room3_1 = [None, 3, 0, None, 1]
room3_2 = [3, None, None, 0, 2]
room3_3 = [None, 4, 2, 1, 2]
room3_4 = [5, None, None, 3, 3]
room3_5 = [None, 6, 4, None, 3]
room3_6 = [None, None, 7, 5, 3]
room3_7 = [6, 8, None, None, 4]
room3_8 = [9, None, None, 7, 0]
room3_9 = [None, 10, 8, None, 1]
room3_10 = [11, None, 12, 9, 2]
room3_11 = [None, None, 10, None, 2]
room3_12 = [10, 13, None, None, 3]
room3_13 = [14, None, None, 12, 3]
room3_14 = [None, None, 13, None, 3]


room_list4 = []
room4_0 = [1, None, None, None, 0]
room4_1 = [2, 3, 0, 4, 1]
room4_2 = [5, 6, 1, 7, 2]
room4_3 = [None, None, None, 1, 2]
room4_4 = [None, 1, None, None, 3]
room4_5 = [None, None, 2, None, 3]
room4_6 = [None, 8, None, 2, 3]
room4_7 = [None, 2, None, 13, 4]
room4_8 = [9, None, None, 6, 0]
room4_9 = [10, 11, 8, 12, 1]
room4_10 = [None, None, 9, None, 2]
room4_11 = [None, None, None, 9, 2]
room4_12 = [None, 9, None, None, 3]
room4_13 = [14, 7, None, None, 3]
room4_14 = [15, 16, 13, 17, 3]
room4_15 = [None, None, 14, None, 4]
room4_16 = [None, None, None, 14, 4]
room4_17 = [None, 14, None, None, 4]
room_list4.append([room4_0, room4_1, room4_2, room4_3, room4_4, room4_5, room4_6, room4_7, room4_8, room4_8, room4_9, room4_10, room4_11, room4_12, room4_13, room4_14, room4_15, room4_16, room4_17])

# ---------------------------
# Initialize global variables
mega_font = pygame.font.SysFont("papyrus", 150)
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
def room_generate(room_list, current_room):
    global player_x, player_y, player, complete1
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
    if room_list[current_room] == room_list[-1]:
        dungeon_door = pygame.draw.rect(screen, RED, [305, 300, 30, 30])
        if player.colliderect(dungeon_door):
            complete1 = True
            main_base()
    return current_room

def movement():
    global player_x, player_y
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

    if player_x < 83:
        player_x = 83
    if player_x > 527:
        player_x = 527
    if player_y < 3:
        player_y = 3
    if player_y > 447:
        player_y = 447

def event_getter(run_value):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run_value = False
            if event.key == pygame.K_SPACE:
                print("space hit")
        elif event.type == pygame.QUIT:
            run_value = False
    return run_value

def heart_value(hearts):
    if hearts >= 1:
        pygame.draw.rect(screen, RED, [88, 5, 10, 10])
    if hearts >= 2:
        pygame.draw.rect(screen, RED, [103, 5, 10, 10])
    if hearts == 3:
        pygame.draw.rect(screen, RED, [118, 5, 10, 10])
    if hearts == 0:
        main_base()
    return hearts

# def enemy():
#     if enemies == 1:
#         enemy1 = pygame.draw.rect(screen, RED, [enemy1_x, enemy1_y, 30, 30])
#         if enemy1_x < player_x:
#             enemy1_x += 1
#         elif enemy1_x > player_x:
#             enemy1_x -= 1
#         if enemy1_y < player_y:
#             enemy1_y += 1
#         elif enemy1_y > player_y:
#             enemy1_y -= 1
#         if enemy1.colliderect(player):
#             if damage == True:
#                 hearts -= 1
#                 if enemy1_x < player_x and player_x < 507:
#                     player_x += 20
#                 elif enemy1_x > player_x and player_x > 103:
#                     player_x -= 20
#                 if enemy1_y < player_y and player_y > 23:
#                     player_y += 20
#                 elif enemy1_y > player_y and player_y < 427:
#                     player_y -= 20
#                 damage = False
#         else: 
#             damage = True

def main_base():
    global player_x, player_y, player
    global complete1, complete2, complete3, complete4
    player_x = 305
    player_y = 225
    hearts = 3
    running = True
    while running:
        
        screen.fill(BLACK)  # always the first drawing command
        pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)
        home = mega_font.render("HOME", True, RED)
        screen.blit(home, (home.get_rect(center = screen.get_rect().center)[0], home.get_rect(center = screen.get_rect().center)[1]))


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
        if complete1:
            door2 = pygame.draw.rect(screen, RED, [547, 140, 10, 200])
            if player.colliderect(door2):
                dungeon2()
        if complete2:
            door3 = pygame.draw.rect(screen, RED, [220, 467, 200, 10])
            if player.colliderect(door3):
                dungeon3()
        if complete3:
            door4 = pygame.draw.rect(screen, RED, [83, 140, 10, 200])
            if player.colliderect(door4):
                dungeon4()
        if complete4:
            door5 = pygame.draw.rect(screen, RED, [305, 300, 30, 30], 5)
            if player.colliderect(door5):
                dungeon5()

        movement()
        running = event_getter(running)

        pygame.display.flip()
        clock.tick(30)
    pygame.quit()

def dungeon1():
    current_room = 0
    hearts = 3
    
    running = True
    while running:
        
        screen.fill(BLACK)  # always the first drawing command
        pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)
        dun1_txt = mega_font.render("1", True, RED)
        screen.blit(dun1_txt, (dun1_txt.get_rect(center = screen.get_rect().center)[0], dun1_txt.get_rect(center = screen.get_rect().center)[1]))
        hearts = heart_value(hearts)

        player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])

        movement()

        current_room = room_generate(room_list1, current_room)
        running = event_getter(running)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()


def dungeon2():
    global complete2
    print("dungeon 2")
    main_base()
    

def dungeon3():
    global complete3
    print("dungeon 3")
    main_base()


def dungeon4():
    global complete4
    print("dungeon 4")
    main_base()


def dungeon5():
    print("dungeon5")
    main_base()


if __name__ == "__main__":
    main_base()
