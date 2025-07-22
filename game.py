import pygame
from sys import exit

WIDTH = 1000
HEIGHT = 700

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

clock = pygame.time.Clock()
game_active = False

font = pygame.font.Font("Pixeltype.ttf", 50)
block_list = []
x_offset = 0
y_offset = 125
# True -> Blue -> X, False -> Red -> O
who = True
who_won = 0

# Improved spacing
for i in range(0, 9):
    x_offset = 175 + ((i%3)*325)
    if i % 3 == 0 and i != 0:
        x_offset = 175
        y_offset = 125 + (i*75)
    square = pygame.Rect((0, 0, 300, 200))
    square.center = (x_offset, y_offset)
    block_list.append([square, (255, 255, 255), 0])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
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
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                for block in block_list:
                    block[1] = (255, 255, 255)
                    block[2] = 0
        if game_active:
            screen.fill((189, 183, 107))
            for block in block_list:
                pygame.draw.rect(screen, block[1], block[0])
            # For X
            # Rows
            if block_list[0][2] == 1 and block_list[1][2] == 1 and block_list[2][2] == 1:
                print("X won")
                who_won = 1
                game_active = False
            if block_list[3][2] == 1 and block_list[4][2] == 1 and block_list[5][2] == 1:
                print("X won")
                who_won = 1
                game_active = False
            if block_list[6][2] == 1 and block_list[7][2] == 1 and block_list[8][2] == 1:
                print("X won")
                who_won = 1
                game_active = False
            # Columns
            if block_list[0][2] == 1 and block_list[3][2] == 1 and block_list[6][2] == 1:
                print("X won")
                who_won = 1
                game_active = False
            if block_list[1][2] == 1 and block_list[4][2] == 1 and block_list[7][2] == 1:
                print("X won")
                who_won = 1
                game_active = False
            if block_list[2][2] == 1 and block_list[5][2] == 1 and block_list[8][2] == 1:
                print("X won")
                who_won = 1
                game_active = False
            # Diagonals
            if block_list[0][2] == 1 and block_list[4][2] == 1 and block_list[8][2] == 1:
                print("X won")
                who_won = 1
                game_active = False
            if block_list[2][2] == 1 and block_list[4][2] == 1 and block_list[6][2] == 1:
                print("X won")
                who_won = 1
                game_active = False
            # For O
            # Rows
            if block_list[0][2] == 2 and block_list[1][2] == 2 and block_list[2][2] == 2:
                print("O won")
                who_won = 2
                game_active = False
            if block_list[3][2] == 2 and block_list[4][2] == 2 and block_list[5][2] == 2:
                print("O won")
                who_won = 2
                game_active = False
            if block_list[6][2] == 2 and block_list[7][2] == 2 and block_list[8][2] == 2:
                print("O won")
                who_won = 2
                game_active = False
            # Columns
            if block_list[0][2] == 2 and block_list[3][2] == 2 and block_list[6][2] == 2:
                print("O won")
                who_won = 2
                game_active = False
            if block_list[1][2] == 2 and block_list[4][2] == 2 and block_list[7][2] == 2:
                print("O won")
                who_won = 2
                game_active = False
            if block_list[2][2] == 2 and block_list[5][2] == 2 and block_list[8][2] == 2:
                print("O won")
                who_won = 2
                game_active = False
            # Diagonals
            if block_list[0][2] == 2 and block_list[4][2] == 2 and block_list[8][2] == 2:
                print("O won")
                who_won = 2
                game_active = False
            if block_list[2][2] == 2 and block_list[4][2] == 2 and block_list[6][2] == 2:
                print("O won")
                who_won = 2
                game_active = False
        else:
            screen.fill((189, 183, 107))

            title_message = font.render("TICTACTOE", 0, (255, 255, 255))
            title_message_rect = title_message.get_rect(center = (500, 150))
            
            hello_message = font.render("Click mouse to start", 0, (255, 255, 255))
            hello_message_rect = hello_message.get_rect(center = (500, 450))
            
            x_won_message = font.render("X won!", 0, (255, 255, 255))
            x_won_message_rect = x_won_message.get_rect(center = (500, 250))

            o_won_message = font.render("O won!", 0, (255, 255, 255))
            o_won_message_rect = x_won_message.get_rect(center = (500, 250))

            try_again_message = font.render("Click mouse to try again", 0, (255, 255, 255))
            try_again_message_rect = try_again_message.get_rect(center = (500, 450))
            
            if who_won == 0:
                screen.blit(title_message, title_message_rect)
                screen.blit(hello_message, hello_message_rect)
            elif who_won == 1:
                screen.blit(title_message, title_message_rect)
                screen.blit(x_won_message, x_won_message_rect)
                screen.blit(try_again_message, try_again_message_rect)
            else:
                screen.blit(title_message, title_message_rect)
                screen.blit(o_won_message, o_won_message_rect)
                screen.blit(try_again_message, try_again_message_rect)

    pygame.display.update()
    clock.tick(60)