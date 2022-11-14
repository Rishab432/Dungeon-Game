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
    player_x = 320
    player_y = 240
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
            door5 = pygame.draw.rect(screen, RED, [315, 300, 30, 30], 5)
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
    global complete1
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
