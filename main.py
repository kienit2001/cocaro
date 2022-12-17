import pygame, sys
from pygame.locals import *
from game import danhvoiamy, maytudanh, choi2nguoi
from caro import caro

WINDOWWIDTH = 1000
WINDOWHEIGHT = 700

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Hello world!')
font = pygame.font.SysFont('Times New Roman', 20)
fontlon = pygame.font.SysFont('Times New Roman', 24)
# DISPLAYSURF.fill(GREEN)
toado = {
    1: 800,
    2: 200,
}

word = {
    1: font.render('Bắt Đầu', True, (255, 255, 0)),
    2: font.render('Chơi 2 Người', True, (255, 255, 0)),
    3: font.render('Chọn Cấp Độ', True, (255, 255, 0)),
    4: font.render('Hướng Dẫn', True, (255, 255, 0)),
    5: font.render('Thoát game', True, (255, 255, 0)),
    6: fontlon.render('HỌC VIỆN CÔNG NGHỆ BƯU CHÍNH VIỄN THÔNG', True, (0, 0, 0)),
    7: fontlon.render('THPCM', True, (0, 0, 0)),
    8: font.render('Máy đánh trước', True, (255, 255, 0)),
    9: font.render('Người Đánh trước', True, (255, 255, 0))
}

leve = {
    1: font.render('Dễ', True, (255, 255, 0)),
    2: font.render('Trung bình', True, (255, 255, 0)),
    3: font.render('Khó', True, (255, 255, 0)),
    4: font.render("Quay Lại", True, (255, 255, 0))
}



leve_chon = {
    1: font.render('Đang chọn: Dễ', True, (0, 0, 0)),
    2: font.render('Đang chọn: Trung bình', True, (0, 0, 0)),
    3: font.render('Đang chọn: Khó', True, (0, 0, 0))
}

muc = 1
danhtruoc = 1


def menu1(muc,danhtruoc):
    pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2], 170, 50), border_radius=100)
    DISPLAYSURF.blit(word[1], (toado[1] + 50, toado[2] + 15))
    pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2] + 70, 170, 50), border_radius=100)
    DISPLAYSURF.blit(word[2], (toado[1] + 30, toado[2] + 70 + 15))
    pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2] + 70 * 2, 170, 50), border_radius=100)
    DISPLAYSURF.blit(word[3], (toado[1] + 30, toado[2] + 70 * 2 + 15))
    pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2] + 70 * 4, 170, 50), border_radius=100)
    DISPLAYSURF.blit(word[4], (toado[1] + 30, toado[2] + 70 * 4 + 15))
    pygame.draw.rect(DISPLAYSURF, (255, 255, 210), (toado[1], toado[2] + 70 * 5, 200, 50), border_radius=100)

    pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2] + 70 * 5, 170, 50), border_radius=100)
    DISPLAYSURF.blit(word[5], (toado[1] + 30, toado[2] + 70 * 5 + 15))
    # DISPLAYSURF.blit(leve_xoa[muc], (toado[1] + 30, toado[2] + 70 * 5 + 15))
    pygame.draw.rect(DISPLAYSURF, (255, 255, 210), (toado[1], toado[2] + 70 * 3, 200, 50), border_radius=100)

    if danhtruoc == 1 :

        pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2] + 70 * 3, 170, 50), border_radius=100)
        DISPLAYSURF.blit(word[8], (toado[1] + 30, toado[2] + 70 * 3 + 15))
    elif danhtruoc == 2:
        pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2] + 70 * 3, 170, 50), border_radius=100)
        DISPLAYSURF.blit(word[9], (toado[1] + 15, toado[2] + 70 * 3 + 15))


def menu2(muc):
    pygame.draw.rect(DISPLAYSURF, (250, 250, 210), (toado[1], toado[2], 170, 50), border_radius=100)
    pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2] + 70, 170, 50), border_radius=100)
    DISPLAYSURF.blit(leve[1], (toado[1] + 30, toado[2] + 70 + 15))
    pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2] + 70 * 2, 170, 50), border_radius=100)
    DISPLAYSURF.blit(leve[2], (toado[1] + 30, toado[2] + 70 * 2 + 15))
    pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2] + 70 * 3, 170, 50), border_radius=100)
    DISPLAYSURF.blit(leve[3], (toado[1] + 30, toado[2] + 70 * 3 + 15))

    pygame.draw.rect(DISPLAYSURF, ((100, 0, 0)), (toado[1], toado[2] + 70 * 4, 170, 50), border_radius=100)
    DISPLAYSURF.blit(leve[4], (toado[1] + 30, toado[2] + 70 * 4 + 15))
    pygame.draw.rect(DISPLAYSURF, (250, 250, 210), (toado[1], toado[2] + 70 * 5, 170, 50), border_radius=100)
    DISPLAYSURF.blit(leve_chon[muc], (toado[1] , toado[2] + 70 * 5 + 15))


def load_nen():
    DISPLAYSURF.fill((250, 250, 210))
    a = pygame.image.load("image/nen1.png")
    DISPLAYSURF.blit(a, (50, 200))
    a = pygame.image.load("image/logotruong2.png")
    DISPLAYSURF.blit(a, (50, 20))
    DISPLAYSURF.blit(word[6], (200, 40))
    DISPLAYSURF.blit(word[7], (400, 70))




def run(muc, menu=1,danhtruoc=1):
    while True:

        # a = pygame.image.load("image/co1.png")
        # DISPLAYSURF.blit(a, (60
        # 0, 20))
        if menu == 1:
            menu1(muc,danhtruoc)
        else:
            if menu == 2:
                menu2(muc)

        # pygame.draw.rect(DISPLAYSURF, (100, 0, 0), (toado[1], toado[2] +70*5, 170, 50), border_radius = 100)
        # DISPLAYSURF.blit(word[6], (toado[1]+50, 435))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:  # 2
                spot = event.pos  # 3
                # print(spot)
                if toado[1] <= spot[0] <= toado[1] + 170 and toado[2] <= spot[1] <= toado[2] + 50 and menu == 1:
                    danhvoiamy(muc,danhtruoc)
                    load_nen()
                    run(muc, 1, danhtruoc)
            if event.type == pygame.MOUSEBUTTONDOWN:  # 2
                spot = event.pos  # 3
                # print(spot)
                if toado[1] <= spot[0] <= toado[1] + 170 and toado[2] + 70 <= spot[1] <= toado[2] + 50 + 70:
                    if menu == 1:
                        choi2nguoi()
                        load_nen()
                        run(muc, 1, danhtruoc)
                    elif menu == 2:
                        run(1, 1, danhtruoc)

            if event.type == pygame.MOUSEBUTTONDOWN:  # 2
                spot = event.pos  # 3
                # print(spot)
                if toado[1] <= spot[0] <= toado[1] + 170 and toado[2] + 70 * 2 <= spot[1] <= toado[2] + 50 + 70 * 2:
                    if menu == 1:
                        run(muc, 2, danhtruoc)
                    elif menu == 2:
                        run(2, 1, danhtruoc)
            if event.type == pygame.MOUSEBUTTONDOWN:  # 2
                spot = event.pos  # 3
                # print(spot)
                if toado[1] <= spot[0] <= toado[1] + 170 and toado[2] + 70 * 3 <= spot[1] <= toado[2] + 50 + 70 * 3:
                    if menu == 1:
                        if danhtruoc == 1:
                            danhtruoc =2
                        else:
                            danhtruoc =1
                        run(muc, 1, danhtruoc)
                    elif menu == 2:
                        run(3, 1, danhtruoc)
            if event.type == pygame.MOUSEBUTTONDOWN:  # 2
                spot = event.pos  # 3
                # print(spot)
                if toado[1] <= spot[0] <= toado[1] + 170 and toado[2] + 70 * 4 <= spot[1] <= toado[2] + 50 + 70 * 4:
                    # maytudanh(muc)
                    # run(muc, 1)
                    if menu == 2:
                        run(muc, 1, danhtruoc)
            if event.type == pygame.MOUSEBUTTONDOWN:  # 2
                spot = event.pos  # 3
                # print(spot)
                if toado[1] <= spot[0] <= toado[1] + 170 and toado[2] + 70 * 5 <= spot[1] <= toado[2] + 50 + 70 * 5:
                    pygame.quit()


if __name__ == '__main__':
    load_nen()
    run(muc)
