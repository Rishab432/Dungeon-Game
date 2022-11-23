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
def main_base():
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
    room8 = [None, 7, None, None, "boss"]
    room_list.append(room8)
    current_room = 0
    next_room = 0
    enemy1_x = 100
    enemy1_y = 20
    enemy2_x = 510
    enemy2_y = 20
    enemy3_x = 100
    enemy3_y = 430
    enemy4_x = 510
    enemy4_y = 430
    magic = pygame.draw.rect(screen, BLACK, [0, 0, 1, 1])
    damage = True
    boss = 0
    
    player_x = 305
    player_y = 225
    hearts = 3
    attackup = False
    attackdown = False
    attackleft = False
    attackright = False
    attack = False
    room = False
    running = True
    while running:
        
        screen.fill(BLACK)  # always the first drawing command
        pygame.draw.rect(screen, WHITE, [80, 0, 480, 480], 3)
        dun1_txt = mega_font.render("1", True, RED)
        screen.blit(dun1_txt, (dun1_txt.get_rect(center = screen.get_rect().center)[0], dun1_txt.get_rect(center = screen.get_rect().center)[1]))

        if hearts >= 1:
            pygame.draw.rect(screen, RED, [88, 5, 10, 10])
        if hearts >= 2:
            pygame.draw.rect(screen, RED, [103, 5, 10, 10])
        if hearts == 3:
            pygame.draw.rect(screen, RED, [118, 5, 10, 10])
        if hearts == 0:
            main_base()
        player = pygame.draw.rect(screen, BLUE, [player_x, player_y, 30, 30])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if player_y > 3:
                player_y -= 3
        if keys[pygame.K_DOWN]:
            if player_y < 447:
                player_y += 3
        if keys[pygame.K_LEFT]:
            if player_x > 83:
                player_x -= 3
        if keys[pygame.K_RIGHT]:
            if player_x < 527:
                player_x += 3

        if attackup == True:
            magic = pygame.draw.rect(screen, WHITE, [player_x-5, player_y-10, 40, 3])
            mag_fcount += 1
            print("Attacking")
            if mag_fcount == 3:
                print("No longer attacking")
                attackup = False
        if attackdown == True:
            magic = pygame.draw.rect(screen, WHITE, [player_x-5, player_y+40, 40, 3])
            mag_fcount += 1
            print("Attacking")
            if mag_fcount == 3:
                print("No longer attacking")
                attackdown = False
        if attackleft == True:
            magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-5, 3, 40])
            mag_fcount += 1
            print("Attacking")
            if mag_fcount == 3:
                print("No longer attacking")
                attackleft = False
        if attackright == True:
            magic = pygame.draw.rect(screen, WHITE, [player_x+37, player_y-5, 3, 40])
            mag_fcount += 1
            print("Attacking")
            if mag_fcount == 3:
                print("No longer attacking")
                attackright = False
        if attack == True:
            magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-10, 50, 50], 3)
            mag_fcount += 1
            print("Attacking")
            if mag_fcount == 3:
                print("No longer attacking")
                attack = False
        

        if player_x < 83:
            player_x = 83
        if player_x > 527:
            player_x = 527
        if player_y < 3:
            player_y = 3
        if player_y > 447:
            player_y = 447

        if room == False:
            enemies = room_list[current_room][4]
            enemies_left = room_list[current_room][4]
            room = True
        if enemies >= 1:
            enemy1 = pygame.draw.rect(screen, RED, [enemy1_x, enemy1_y, 30, 30])
            if enemy1_x < player_x:
                enemy1_x += 1
            elif enemy1_x > player_x:
                enemy1_x -= 1
            if enemy1_y < player_y:
                enemy1_y += 1
            elif enemy1_y > player_y:
                enemy1_y -= 1
            if enemy1.colliderect(player):
                if damage == True:
                    hearts -= 1
                    if enemy1_x < player_x and player_x < 497:
                        player_x += 30
                    elif enemy1_x > player_x and player_x > 113:
                        player_x -= 30
                    if enemy1_y < player_y and player_y > 33:
                        player_y += 30
                    elif enemy1_y > player_y and player_y < 417:
                        player_y -= 30
                    damage = False
            else: 
                damage = True
            if enemy1.colliderect(magic):
                enemies_left -= 1
                enemy1_x, enemy1_y = -1000, -1000
        if enemies >= 2:
            enemy2 = pygame.draw.rect(screen, RED, [enemy2_x, enemy2_y, 30, 30])
            if enemy2_x < player_x:
                enemy2_x += 1
            elif enemy2_x > player_x:
                enemy2_x -= 1
            if enemy2_y < player_y:
                enemy2_y += 1
            elif enemy2_y > player_y:
                enemy2_y -= 1
            if enemy2.colliderect(player):
                if damage == True:
                    hearts -= 1
                    if enemy2_x < player_x and player_x < 497:
                        player_x += 30
                    elif enemy2_x > player_x and player_x > 113:
                        player_x -= 30
                    if enemy2_y < player_y and player_y > 33:
                        player_y += 30
                    elif enemy2_y > player_y and player_y < 417:
                        player_y -= 30
                    damage = False
            else: 
                damage = True
            if enemy2.colliderect(magic):
                enemies -= 1

        if enemies == 0:
            if room_list[current_room][0] != None:
                next_room = room_list[current_room][0]
                door1 = pygame.draw.rect(screen, RED, [220, 3, 200, 10])
                if player.colliderect(door1):
                    player_x = 305
                    player_y = 437
                    current_room = next_room
                    room = False
            if room_list[current_room][1] != None:
                next_room = room_list[current_room][1]
                door2 = pygame.draw.rect(screen, RED, [547, 140, 10, 200])
                if player.colliderect(door2):
                    player_x = 93
                    player_y = 225
                    current_room = next_room
                    room = False
            if room_list[current_room][2] != None:
                next_room = room_list[current_room][2]
                door3 = pygame.draw.rect(screen, RED, [220, 467, 200, 10])
                if player.colliderect(door3):
                    player_x = 305
                    player_y = 13
                    current_room = next_room
                    room = False
            if room_list[current_room][3] != None:
                next_room = room_list[current_room][3]
                door4 = pygame.draw.rect(screen, RED, [83, 140, 10, 200])
                if player.colliderect(door4):
                    player_x = 517
                    player_y = 225
                    current_room = next_room
                    room = False
        if boss == 0:
            if room_list[current_room] == room8:
                dungeon_door = pygame.draw.rect(screen, RED, [305, 300, 30, 30])
                if player.colliderect(dungeon_door):
                    global complete1
                    complete1 = True
                    main_base()



        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE:
                    if keys[pygame.K_UP]:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-5, player_y-10, 40, 3])
                        mag_fcount = 0
                        attackup = True
                    elif keys[pygame.K_DOWN]:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-5, player_y+40, 40, 3])
                        mag_fcount = 0
                        attackdown = True
                    elif keys[pygame.K_LEFT]:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-5, 3, 40])
                        mag_fcount = 0
                        attackleft = True
                    elif keys[pygame.K_RIGHT]: 
                        magic = pygame.draw.rect(screen, WHITE, [player_x+37, player_y-5, 3, 40])
                        mag_fcount = 0
                        attackright = True
                    else:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-10, 50, 50], 3)
                        mag_fcount = 0
                        attack = True
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
def dungeon2():
    room_list = []
    enemies = 0
    boss = 1
    room0 = [None, 1, None, None, 0]
    room_list.append(room0)
    room1 = [None, None, 2, 0, 1]
    room_list.append(room1)
    room2 = [1, 3, 4, None, 2]
    room_list.append(room2)
    room3 = [5, None, 6, 2, 2]
    room_list.append(room3)
    room4 = [2, None, None, None, 3]
    room_list.append(room4)
    room5 = [None, None, 3, None, 3]
    room_list.append(room5)
    room6 = [3, 7, None, None, 3]
    room_list.append(room6)
    room7 = [None, None, None, 6, 4]
    room_list.append(room7)
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
        dun2_txt = mega_font.render("2", True, RED)
        screen.blit(dun2_txt, (dun2_txt.get_rect(center = screen.get_rect().center)[0], dun2_txt.get_rect(center = screen.get_rect().center)[1]))

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
            if room_list[current_room] == room7:
                dungeon_door = pygame.draw.rect(screen, RED, [305, 300, 30, 30])
                if player.colliderect(dungeon_door):
                    global complete2
                    complete2 = True
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
                        mag_fcount = 0
                        attack = True
                    elif keys[pygame.K_DOWN]:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-5, player_y+40, 40, 3])
                        mag_fcount = 0
                        attack = True
                    elif keys[pygame.K_LEFT]:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-5, 3, 40])
                        mag_fcount = 0
                        attack = True
                    elif keys[pygame.K_RIGHT]: 
                        magic = pygame.draw.rect(screen, WHITE, [player_x+37, player_y-5, 3, 40])
                        mag_fcount = 0
                        attack = True
                    else:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-10, 50, 50], 3)
                        mag_fcount = 0
                        attack = True
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
def dungeon3():
    room_list = []
    enemies = 0
    boss = 1
    room0 = [1, 2, None, None, 0]
    room_list.append(room0)
    room1 = [None, 3, 0, None, 1]
    room_list.append(room1)
    room2 = [3, None, None, 0, 2]
    room_list.append(room2)
    room3 = [None, 4, 2, 1, 2]
    room_list.append(room3)
    room4 = [5, None, None, 3, 3]
    room_list.append(room4)
    room5 = [None, 6, 4, None, 3]
    room_list.append(room5)
    room6 = [None, None, 7, 5, 3]
    room_list.append(room6)
    room7 = [6, 8, None, None, 4]
    room_list.append(room7)
    room8 = [9, None, None, 7, 0]
    room_list.append(room8)
    room9 = [None, 10, 8, None, 1]
    room_list.append(room9)
    room10 = [11, None, 12, 9, 2]
    room_list.append(room10)
    room11 = [None, None, 10, None, 2]
    room_list.append(room11)
    room12 = [10, 13, None, None, 3]
    room_list.append(room12)
    room13 = [14, None, None, 12, 3]
    room_list.append(room13)
    room14 = [None, None, 13, None, 3]
    room_list.append(room14)
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
        dun3_txt = mega_font.render("3", True, RED)
        screen.blit(dun3_txt, (dun3_txt.get_rect(center = screen.get_rect().center)[0], dun3_txt.get_rect(center = screen.get_rect().center)[1]))

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
            if room_list[current_room] == room11:
                dungeon_door = pygame.draw.rect(screen, RED, [305, 300, 30, 30])
                if player.colliderect(dungeon_door):
                    global complete3
                    complete3 = True
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
                        mag_fcount = 0
                        attack = True
                    elif keys[pygame.K_DOWN]:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-5, player_y+40, 40, 3])
                        mag_fcount = 0
                        attack = True
                    elif keys[pygame.K_LEFT]:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-5, 3, 40])
                        mag_fcount = 0
                        attack = True
                    elif keys[pygame.K_RIGHT]: 
                        magic = pygame.draw.rect(screen, WHITE, [player_x+37, player_y-5, 3, 40])
                        mag_fcount = 0
                        attack = True
                    else:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-10, 50, 50], 3)
                        mag_fcount = 0
                        attack = True
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
def dungeon4():
    room_list = []
    enemies = 0
    boss = 1
    room0 = [1, None, None, None, 0]
    room_list.append(room0)
    room1 = [2, 3, 0, 4, 1]
    room_list.append(room1)
    room2 = [5, 6, 1, 7, 2]
    room_list.append(room2)
    room3 = [None, None, None, 1, 2]
    room_list.append(room3)
    room4 = [None, 1, None, None, 3]
    room_list.append(room4)
    room5 = [None, None, 2, None, 3]
    room_list.append(room5)
    room6 = [None, 8, None, 2, 3]
    room_list.append(room6)
    room7 = [None, 2, None, 13, 4]
    room_list.append(room7)
    room8 = [9, None, None, 6, 0]
    room_list.append(room8)
    room9 = [10, 11, 8, 12, 1]
    room_list.append(room9)
    room10 = [None, None, 9, None, 2]
    room_list.append(room10)
    room11 = [None, None, None, 9, 2]
    room_list.append(room11)
    room12 = [None, 9, None, None, 3]
    room_list.append(room12)
    room13 = [14, 7, None, None, 3]
    room_list.append(room13)
    room14 = [15, 16, 13, 17, 3]
    room_list.append(room14)
    room15 = [None, None, 14, None, 4]
    room_list.append(room15)
    room16 = [None, None, None, 14, 4]
    room_list.append(room16)
    room17 = [None, 14, None, None, 4]
    room_list.append(room17)
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
        dun4_txt = mega_font.render("4", True, RED)
        screen.blit(dun4_txt, (dun4_txt.get_rect(center = screen.get_rect().center)[0], dun4_txt.get_rect(center = screen.get_rect().center)[1]))

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
            if room_list[current_room] == room15 or room_list[current_room] == room10:
                dungeon_door = pygame.draw.rect(screen, RED, [305, 300, 30, 30])
                if player.colliderect(dungeon_door):
                    global complete4
                    complete4 = True
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
                        mag_fcount = 0
                        attack = True
                    elif keys[pygame.K_DOWN]:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-5, player_y+40, 40, 3])
                        mag_fcount = 0
                        attack = True
                    elif keys[pygame.K_LEFT]:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-5, 3, 40])
                        mag_fcount = 0
                        attack = True
                    elif keys[pygame.K_RIGHT]: 
                        magic = pygame.draw.rect(screen, WHITE, [player_x+37, player_y-5, 3, 40])
                        mag_fcount = 0
                        attack = True
                    else:
                        magic = pygame.draw.rect(screen, WHITE, [player_x-10, player_y-10, 50, 50], 3)
                        mag_fcount = 0
                        attack = True
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
def dungeon5():
    main_base()

main_base()
