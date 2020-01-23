import pygame
import sys
from random import randint

pygame.init()
pygame.font.init()
font = pygame.font.Font(None, 70)
font_color = (150, 130, 60)
bg = (80, 40, 110)
pygame.display.set_caption('krestiki')
height = 600  # высота = y
weight = 600  # ширина = x
sc = pygame.display.set_mode((weight, height))
clock = pygame.time.Clock()

def DrawText(text, font, surface_menu, x, y):
    textobj = font.render(text, 1, font_color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface_menu.blit(textobj, textrect)

def cross(cort):
    x = cort[0] * 40
    y = cort[1] * 40
    pygame.draw.line(sc, (100, 30, 30), [x + 7, y + 7], [x - 7 + 40, y - 7 + 40], 5)
    pygame.draw.line(sc, (100, 30, 30), [x + 7, y - 7 + 40], [x - 7 + 40, y + 7], 5)

def zero(cort):
    x = cort[0] * 40
    y = cort[1] * 40
    pygame.draw.circle(sc, (100, 30, 30), (x + 20, y + 21), 16, 4)

def check(figure, cort, field):
    count = 0
    j = cort[0]    # x
    i = cort[1]    # y

    # вверх / вниз

    while count < 5:
        if field[i][j] == figure and i >= 0 and i <= 14:
            i -= 1
            count += 1
        elif (i + 5 <= 14) and (field[i + 5][j] == figure):
            i += 5
        else:
            count = 0
            break

    if count >= 5:
        game_over = True
        return game_over
    count = 0
    j = cort[0]
    i = cort[1]

    # вправо / влево

    while count < 5:
        if field[i][j] == figure and j >= 0 and j <= 14:
            j -= 1
            count += 1
        elif (j + 5 <= 14) and (field[i][j + 5] == figure):
            j += 5
        else:
            count = 0
            break

    if count >= 5:
        game_over = True
        return game_over
    count = 0
    j = cort[0]
    i = cort[1]

    # главная диагональ

    while count < 5:
        if field[i][j] == figure and i <= 14 and j <= 14 and i >= 0 and i <= 14:
            i -= 1
            j -= 1
            count += 1
        elif (j + 5 <= 14) and (i + 5 <= 14) and (field[i + 5][j + 5] == figure):
            j += 5
            i += 5
        else:
            count = 0
            break

    if count >= 5:
        game_over = True
        return game_over
    count = 1
    j = cort[0]
    i = cort[1]
    
    # побочная диагональ

    if i - 1 >= 0 and j + 1 <= 14 and field[i - 1][j + 1] == figure:
        count += 1
        if i - 2 >= 0 and j + 2 <= 14 and field[i - 2][j + 2] == figure:
            count += 1
            if i - 3 >= 0 and j + 3 <= 14 and field[i - 3][j + 3] == figure:
                count += 1
                if i - 4 >= 0 and j + 4 <= 14 and field[i - 4][j + 4] == figure:
                    count += 1
                    if i - 5 >= 0 and j + 5 <= 14 and field[i - 5][j + 5] == figure:
                        count += 1

    if i + 1 <= 14 and j - 1 >= 0 and field[i + 1][j - 1] == figure:
        count += 1
        if i + 2 <= 14 and j - 2 >= 0 and field[i + 2][j - 2] == figure:
            count += 1
            if i + 3 <= 14 and j - 3 >= 0 and field[i + 3][j - 3] == figure:
                count += 1
                if i + 4 <= 14 and j - 4 >= 0 and field[i + 4][j - 4] == figure:
                    count += 1
                    if i + 5 <= 14 and j - 5 >= 0 and field[i + 5][j - 5] == figure:
                        count += 1

    if count >= 5:
        game_over = True
        return game_over

def menu():
    sc.fill(bg)
    DrawText('Крестики нолики', font, sc, 80, 20)
    DrawText('Игра', font, sc, 40, 200)
    DrawText('Выход', font, sc, 40, 250)
    pygame.draw.line(sc, (150, 130, 60), [350, 200], [350, 500], 3)
    pygame.draw.line(sc, (150, 130, 60), [450, 200], [450, 500], 3)
    pygame.draw.line(sc, (150, 130, 60), [250, 300], [550, 300], 3)
    pygame.draw.line(sc, (150, 130, 60), [250, 400], [550, 400], 3)
    pygame.draw.circle(sc, (100, 30, 30), (400, 350), 40, 7)
    pygame.draw.circle(sc, (100, 30, 30), (300, 250), 40, 7)
    pygame.draw.circle(sc, (100, 30, 30), (500, 450), 40, 7)
    pygame.draw.line(sc, (100, 30, 30), [250, 200], [550, 500], 5)

    x_circle = 20   # х - координата центра круга
    y_circle = 220  # у - координата центра круга
    pygame.draw.circle(sc, (100, 30, 30), (x_circle, y_circle), 15)
    mouse_up_down = 1

    done_menu = True
    while done_menu:
        pos = pygame.mouse.get_pos()
        for event_menu in pygame.event.get():
            if event_menu.type == pygame.QUIT:
                sys.exit()
            if event_menu.type == pygame.KEYDOWN:
                if event_menu.key == pygame.K_KP_ENTER or event_menu.key == pygame.K_e:
                    if y_circle == 220:
                        mode()
                    elif y_circle == 270:
                        sys.exit()
            # выбор раздела мышью
            if pos[0] <= 200:
                if pos[1] >= 250 and mouse_up_down == 1 and pos[1] <= 300:
                    pygame.draw.circle(sc, bg, (x_circle, y_circle), 15)
                    y_circle += 50
                    pygame.draw.circle(sc, (100, 30, 30), (x_circle, y_circle), 15)
                    mouse_up_down = 2
                elif pos[1] < 250 and mouse_up_down == 2 and pos[1] > 200:
                    pygame.draw.circle(sc, bg, (x_circle, y_circle), 15)
                    y_circle -= 50
                    pygame.draw.circle(sc, (100, 30, 30), (x_circle, y_circle), 15)
                    mouse_up_down = 1
                if event_menu.type == pygame.MOUSEBUTTONDOWN:
                    if y_circle == 220:
                        mode()
                    elif y_circle == 270:
                        sys.exit()

        pygame.display.update()
        clock.tick(20)

def mode():
    sc.fill(bg)
    pygame.draw.line(sc, (100, 30, 30), [300, 0], [300, 400], 7)
    pygame.draw.line(sc, (100, 30, 30), [0, 400], [600, 400], 7)
    font = pygame.font.Font(None, 35)

    DrawText('игрок vs игрок+', font, sc, 53, 20)
    DrawText('игрок vs компьютер-', font, sc, 337, 20)
    DrawText('компьютер vs компьютер-', font, sc, 145, 450)

    done_mode = True
    while done_mode:
        pos = pygame.mouse.get_pos()          # координаты мыши

        for event_mode in pygame.event.get():
            if event_mode.type == pygame.QUIT:
                sys.exit()
            elif event_mode.type == pygame.MOUSEBUTTONDOWN:
                if pos[1] <= 400 and pos[0] < 297:
                    gamepp()
                elif pos[1] <= 400 and pos[0] > 303:
                    gamepc()
            elif event_mode.type == pygame.KEYDOWN:
                if event_mode.key == pygame.K_ESCAPE:
                    menu()

        if pos[1] > 400:
            pygame.draw.rect(sc, bg, (0, 0, 297, 397))
            pygame.draw.rect(sc, bg, (303, 0, 297, 397))
            pygame.draw.rect(sc, (100, 60, 130), (0, 404, 600, 200))
        elif pos[0] < 300:
            pygame.draw.rect(sc, bg, (0, 404, 600, 200))
            pygame.draw.rect(sc, bg, (303, 0, 297, 397))
            pygame.draw.rect(sc, (100, 60, 130), (0, 0, 297, 397))
        else:
            pygame.draw.rect(sc, bg, (0, 404, 600, 200))
            pygame.draw.rect(sc, bg, (0, 0, 297, 397))
            pygame.draw.rect(sc, (100, 60, 130), (303, 0, 297, 397))

        DrawText('игрок vs игрок+', font, sc, 53, 20)
        DrawText('игрок vs компьютер-', font, sc, 337, 20)
        DrawText('компьютер vs компьютер-', font, sc, 145, 450)

        clock.tick(20)
        pygame.display.update()

def gamepp():
    mouse = [0, 0]
    count = 0
    game_over = False
    #  поле

    field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    x = 0
    y = 0
    sc.fill(bg)

    # рисуем поле

    for i in range(16):
        pygame.draw.line(sc, (0, 0, 0), [x, 0], [x, height], 3)
        x += 40
    for i in range(16):
        pygame.draw.line(sc, (0, 0, 0), [0, y], [weight, y], 3)
        y += 40

    done_game = True
    while done_game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    menu()
            if not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse[0] = event.pos[0] // 40
                    mouse[1] = event.pos[1] // 40

                    if field[mouse[1]][mouse[0]] == 0:
                        if count % 2 == 0:
                            cross(mouse)
                            field[mouse[1]][mouse[0]] = 'x'
                            figure = 'x'
                        else:
                            zero(mouse)
                            field[mouse[1]][mouse[0]] = 'o'
                            figure = 'o'
                        count += 1

                        game_over = check(figure, mouse, field)

                    if game_over:
                        pygame.draw.rect(sc, (55, 55, 55), (130, 210, 340, 100))
                        pygame.draw.rect(sc, font_color, (130, 210, 340, 100), 4)
                        DrawText('Выиграл: ' + figure, font, sc, 165, 235)
        pygame.display.update()
        clock.tick(20)

def gamepc():
    count = 1
    mouse = [0, 0]
    game_over = False

    x = 0
    y = 0

    field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    sc.fill(bg)

    # рисуем поле

    for i in range(16):
        pygame.draw.line(sc, (0, 0, 0), [x, 0], [x, height], 3)
        x += 40
    for i in range(16):
        pygame.draw.line(sc, (0, 0, 0), [0, y], [weight, y], 3)
        y += 40

    done_gamepc = True
    while done_gamepc:
        for event_pc in pygame.event.get():
            if event_pc.type == pygame.QUIT:
                sys.exit()
            elif event_pc.type == pygame.KEYDOWN:
                if event_pc.key == pygame.K_ESCAPE:
                    menu()

            if not game_over:
                if event_pc.type == pygame.MOUSEBUTTONDOWN and count % 2 == 1:
                    mouse[0] = event_pc.pos[0] // 40
                    mouse[1] = event_pc.pos[1] // 40

                    if field[mouse[1]][mouse[0]] == 0:
                        cross(mouse)
                        field[mouse[1]][mouse[0]] = 'x'
                        figure = 'x'
                        count += 1
                        game_over = check(figure, mouse, field)

                # далее пишу ИИ

                elif count == 2:

                    mouse[0] = randint(0, 14)
                    mouse[1] = randint(0, 14)
                    if field[mouse[1]][mouse[0]] == 0:
                        pygame.time.delay(300)
                        zero(mouse)
                        field[mouse[1]][mouse[0]] = 'o'
                        figure = 'o'
                        game_over = check(figure, mouse, field)
                        count += 1
                elif count % 2 == 0:
                    pass

                if game_over:
                    pygame.draw.rect(sc, (55, 55, 55), (130, 210, 340, 100))
                    pygame.draw.rect(sc, font_color, (130, 210, 340, 100), 4)
                    DrawText('Выиграл: ' + figure, font, sc, 165, 235)

        clock.tick(20)
        pygame.display.update()

#gamepp()
#gamepc()
menu()
#mode()
