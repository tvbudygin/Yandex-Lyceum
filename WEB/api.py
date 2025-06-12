import os
import sys
import pygame
import requests
from env import api

ALL_SPRITES = pygame.sprite.Group()
ALL_SPRITES1 = pygame.sprite.Group()
ALL_SPRITES2 = pygame.sprite.Group()
server_address = 'https://static-maps.yandex.ru/v1?'
api_key = api
ll_spn = 'll=133.767123,-25.5996468&spn=20,20'
ll_spn1 = 'll=170.423190,-44.048055&spn=10,10'
ll_spn2 = 'll=46.276908,-21.088370&spn=10,10'
map_request = f"{server_address}{ll_spn}&apikey={api_key}"
response = requests.get(map_request)
map_request = f"{server_address}{ll_spn1}&apikey={api_key}"
response1 = requests.get(map_request)
map_request = f"{server_address}{ll_spn2}&apikey={api_key}"
response2 = requests.get(map_request)

if not response and response1 and response2:
    print("Ошибка выполнения запроса:")
    print(map_request)
    print("Http статус:", response.status_code, "(", response.reason, ")")
    sys.exit(1)

map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

map_file1 = "map1.png"
with open(map_file1, "wb") as file:
    file.write(response1.content)

map_file2 = "map2.png"
with open(map_file2, "wb") as file:
    file.write(response2.content)


def load_image(name):
    fullname = os.path.join(name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Map_file(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(ALL_SPRITES)
        self.image = load_image("map.png")
        self.rect = self.image.get_rect()


class Map_file1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(ALL_SPRITES1)
        self.image = load_image("map1.png")
        self.rect = self.image.get_rect()


class Map_file2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(ALL_SPRITES2)
        self.image = load_image("map2.png")
        self.rect = self.image.get_rect()


pygame.init()
screen = pygame.display.set_mode((600, 450))
pygame.display.flip()
m = 0
running = True
Map_file()
Map_file1()
Map_file2()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                m -= 1
                if m == -1:
                    m = 2
            if event.key == pygame.K_DOWN:
                m += 1
                if m == 3:
                    m = 0
    screen.fill((0, 0, 0))
    if m == 0:
        ALL_SPRITES.draw(screen)
    elif m == 1:
        ALL_SPRITES1.draw(screen)
    elif m == 2:
        ALL_SPRITES2.draw(screen)
    pygame.display.flip()

pygame.quit()

os.remove(map_file)
os.remove(map_file1)
os.remove(map_file2)
