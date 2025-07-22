import pygame
from sys import exit

WIDTH = 1000
HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()
game_active = True

block_list = []
x = 0
y = 0
# True -> Blue -> X, False -> Red -> O
who = True

for i in range(0, 9):
    if i % 3 == 0 and i != 0:
        x += 350
        y += 250
    square = pygame.Rect((i * 350 - x*3, y, 300, 200))
    block_list.append([square, (255, 255, 255), 0])

while game_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for block in block_list:
                if block[0].collidepoint(event.pos):
                    # X starts
                    if who:
                        block[1] = (0, 0, 255)
                        block[2] = 1
                        who = False
                    else:
                        block[1] = (255, 0, 0)
                        block[2] = 2
                        who = True
    
    for block in block_list:
        pygame.draw.rect(screen, block[1], block[0])
    # For X
    # Rows
    if block_list[0][2] == 1 and block_list[1][2] == 1 and block_list[2][2] == 1:
        print("X won")
        game_active = False
    if block_list[3][2] == 1 and block_list[4][2] == 1 and block_list[5][2] == 1:
        print("X won")
        game_active = False
    if block_list[6][2] == 1 and block_list[7][2] == 1 and block_list[8][2] == 1:
        print("X won")
        game_active = False
    # Columns
    if block_list[0][2] == 1 and block_list[3][2] == 1 and block_list[6][2] == 1:
        print("X won")
        game_active = False
    if block_list[1][2] == 1 and block_list[4][2] == 1 and block_list[7][2] == 1:
        print("X won")
        game_active = False
    if block_list[2][2] == 1 and block_list[5][2] == 1 and block_list[8][2] == 1:
        print("X won")
        game_active = False
    # Diagonals
    if block_list[0][2] == 1 and block_list[4][2] == 1 and block_list[8][2] == 1:
        print("X won")
        game_active = False
    if block_list[2][2] == 1 and block_list[4][2] == 1 and block_list[6][2] == 1:
        print("X won")
        game_active = False
    # For O
    # Rows
    if block_list[0][2] == 2 and block_list[1][2] == 2 and block_list[2][2] == 2:
        print("O won")
        game_active = False
    if block_list[3][2] == 2 and block_list[4][2] == 2 and block_list[5][2] == 2:
        print("O won")
        game_active = False
    if block_list[6][2] == 2 and block_list[7][2] == 2 and block_list[8][2] == 2:
        print("O won")
        game_active = False
    # Columns
    if block_list[0][2] == 2 and block_list[3][2] == 2 and block_list[6][2] == 2:
        print("O won")
        game_active = False
    if block_list[1][2] == 2 and block_list[4][2] == 2 and block_list[7][2] == 2:
        print("O won")
        game_active = False
    if block_list[2][2] == 2 and block_list[5][2] == 2 and block_list[8][2] == 2:
        print("O won")
        game_active = False
    # Diagonals
    if block_list[0][2] == 2 and block_list[4][2] == 2 and block_list[8][2] == 2:
        print("O won")
        game_active = False
    if block_list[2][2] == 2 and block_list[4][2] == 2 and block_list[6][2] == 2:
        print("O won")
        game_active = False

    pygame.display.update()
    clock.tick(60)