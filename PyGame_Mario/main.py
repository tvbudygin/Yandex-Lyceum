import pygame
import sys
import os

ALL_SPRITES = pygame.sprite.Group()
ALL_SPRITES1 = pygame.sprite.Group()


def load_level(filename):
    filename = filename
    max_width = 0
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]
    if level_map:
        max_width = max(map(len, level_map))
    return list(map(lambda x: x.ljust(max_width, '.'), level_map)), max_width, len(level_map)


def load_image(name):
    fullname = os.path.join('images', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(ALL_SPRITES)
        self.image = load_image("box.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, t):
        if t == "r":
            self.rect.x += 50
        if t == "l":
            self.rect.x -= 50
        if t == "u":
            self.rect.y -= 50
        if t == "d":
            self.rect.y += 50


class Fon(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(ALL_SPRITES1)
        self.image = load_image("fon.jpg")
        self.rect = self.image.get_rect()


class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(ALL_SPRITES)
        self.image = load_image("grass.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, t):
        if t == "r":
            self.rect.x += 50
        if t == "d":
            self.rect.y += 50


class Mar(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(ALL_SPRITES)
        self.image = load_image("mar.png")
        self.rect = self.image.get_rect()
        self.rect.x = x + 13
        self.rect.y = y + 5
        self.k = 0
        self.k1 = 0


def adddd(pole, x1, y):
    x = x1
    ALL_SPRITES.empty()
    for i in pole:
        for e in i:
            if e == "." or e == "@":
                Grass(x, y)
            elif e == "#":
                Box(x, y)
            x += 50
        y += 50
        x = x1


def menu(file):
    pygame.init()
    size = 960, 540
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    Fon()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = False
                    main(file)
        screen.fill("black")
        ALL_SPRITES1.draw(screen)
        font = pygame.font.Font(None, 100)
        text = font.render(f"Press Space", True, "black")
        screen.blit(text, (300, 470))
        pygame.display.flip()
        clock.tick(4)

    pygame.quit()


def main(file):
    ALL_SPRITES.empty()
    pygame.init()
    clock = pygame.time.Clock()
    running = True
    pole, w, h = load_level(file)
    x = 0
    y = 0
    k = 0
    k1 = 0
    mario_koord = []
    grass = []
    box = []
    for i in pole:
        for e in i:
            if e == ".":
                grass.append(Grass(x, y))
            elif e == "#":
                box.append(Box(x, y))
            elif e == "@":
                grass.append(Grass(x, y))
                mario_koord.append(x)
                mario_koord.append(y)
            x += 50
        y += 50
        x = 0
    mario = Mar(mario_koord[0], mario_koord[1])
    screen = pygame.display.set_mode((w * 50 + 100, h * 50 + 100))
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu(file)
                sys.exit()
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    if pole[mario_koord[1] // 50][mario_koord[0] // 50 - 1] != "#":
                        if k == 0:
                            for i in grass:
                                i.update("r")
                            for i in box:
                                i.update("r")
                        if mario:
                            k = 50
                            for i in range(len(pole)):
                                pole[i] = pole[i][-1] + pole[i][:-1]
                            adddd(pole, k, k1)
                            if k1 == 50:
                                mario = Mar(mario_koord[0] + 50, mario_koord[1] + 50)
                            elif k1 == 0:
                                mario = Mar(mario_koord[0] + 50, mario_koord[1])

                if event.key == pygame.K_RIGHT:
                    if pole[mario_koord[1] // 50][mario_koord[0] // 50 - len(pole[mario_koord[1] // 50]) + 1] != "#":
                        if k == 0:
                            for i in grass:
                                i.update("r")
                            for i in box:
                                i.update("r")
                        if mario:
                            k = 50
                            for i in range(len(pole)):
                                pole[i] = pole[i][1:] + pole[i][0]
                            adddd(pole, k, k1)
                            if k1 == 50:
                                mario = Mar(mario_koord[0] + 50, mario_koord[1] + 50)
                            elif k1 == 0:
                                mario = Mar(mario_koord[0] + 50, mario_koord[1])

                if event.key == pygame.K_UP:
                    if pole[mario_koord[1] // 50 - 1][mario_koord[0] // 50] != "#":
                        if k1 == 0:
                            for i in grass:
                                i.update("d")
                            for i in box:
                                i.update("d")
                        if mario:
                            k1 = 50
                            pole.insert(0, pole.pop())
                            adddd(pole, k, k1)
                            if k == 50:
                                mario = Mar(mario_koord[0] + 50, mario_koord[1] + 50)
                            elif k == 0:
                                mario = Mar(mario_koord[0], mario_koord[1] + 50)

                if event.key == pygame.K_DOWN:
                    if pole[mario_koord[1] // 50 - len(pole) + 1][mario_koord[0] // 50] != "#":
                        if k1 == 0:
                            for i in grass:
                                i.update("d")
                            for i in box:
                                i.update("d")
                        if mario:
                            k1 = 50
                            pole.append(pole.pop(0))
                            adddd(pole, k, k1)
                            if k == 50:
                                mario = Mar(mario_koord[0] + 50, mario_koord[1] + 50)
                            elif k == 0:
                                mario = Mar(mario_koord[0], mario_koord[1] + 50)

                if event.key == pygame.K_ESCAPE:
                    menu(file)
                    sys.exit()
        screen.fill("black")
        ALL_SPRITES.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    print("ввидите файл: file.txt или file1.txt или file2.txt")
    file_name = input()
    try:
        load_level(file_name)
    except FileNotFoundError:
        print("file not found")
        sys.exit()
    menu(file_name)
