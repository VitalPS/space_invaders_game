import pygame
from random import randint

#  initialize pygame
pygame.init()

#  create a screen
screen = pygame.display.set_mode((800, 600))

# title and logo of the screen
pygame.display.set_caption('Space Invaders!')
game_icon = pygame.image.load('icon.png')  # TIP! You can get icons on : flaticon.com (remember taking 32px icon)
pygame.display.set_icon(game_icon)

# player image and initial coordinates
player_img = pygame.image.load('player.png')
playerX = 360
playerY = 480
player_changeX = 0


# draw player image
def player(x, y):
    screen.blit(player_img, (x, y))


# enemy image and initial coordinates
enemy_img = pygame.image.load('ufo.png')
enemyX = randint(0, 735)
enemyY = randint(50, 150)
enemy_changeX = 0
enemy_changeY = 0


# draw player image
def enemy(x, y):
    screen.blit(enemy_img, (x, y))


#  Game Loop (set screen running until click on quit)
running = True
while running:
    for event in pygame.event.get():  # get all events occurring in pygame
        if event.type == pygame.QUIT:  # check if quit event is active
            running = False

        screen.fill((150, 0, 150))  # Coloring the screen background (RGB)
        # TIP! Remember placing all other items above screen.fill!!

        #  create responsive keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_changeX = -0.3
            if event.key == pygame.K_RIGHT:
                player_changeX = 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player_changeX = 0

    # coordinate alteration
    playerX += player_changeX

    # create boundaries
    if playerX < 0:
        playerX = 0
    elif playerX > 736:
        playerX = 736

    player(playerX, playerY)  # calling player image
    enemy(enemyX, enemyY)  # calling enemy image

    pygame.display.update()  # display keep updating
