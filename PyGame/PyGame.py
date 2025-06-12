import os
import sys
import pygame
from random import randrange

ALL_SPRITES = pygame.sprite.Group()


def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Bomb(pygame.sprite.Sprite):
    def __init__(self, group, width, height):
        super().__init__(group)
        self.image_normal = load_image("bomb.png")  # Сохраняем нормальное изображение
        self.image_boom = load_image("boom.png")  # Изображение взрыва
        self.image = self.image_normal  # Начинаем с нормального изображения
        self.rect = self.image.get_rect()
        self.rect.x = randrange(width)
        self.rect.y = randrange(height)
        self.is_exploded = False  # Флаг состояния (взорвано или нет)

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.is_exploded = True  # Бомба взорвана
            self.image = self.image_boom


class Mountain(pygame.sprite.Sprite):
    image = load_image("football.png")

    def __init__(self, size):
        super().__init__(ALL_SPRITES)
        self.image = Mountain.image
        self.rect = self.image.get_rect()
        # вычисляем маску для эффективного сравнения
        self.mask = pygame.mask.from_surface(self.image)
        # располагаем горы внизу
        self.rect.bottom = size[1]


def main():
    pygame.init()
    size = width, height = (1280, 720)
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    bombs = [Bomb(ALL_SPRITES, width, height) for _ in range(5)]
    all_sprites = pygame.sprite.Group()
    for _ in range(100):
        Bomb(all_sprites, width, height)
    running = True
    while running:
        mouse_pos = pygame.mouse.get_pos()  # Получаем текущую позицию мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("black")
        ALL_SPRITES.draw(screen)
        ALL_SPRITES.update(mouse_pos)
        all_sprites.update(mouse_pos)  # Передаем позицию мыши в update
        all_sprites.draw(screen)  # Отрисовка всех спрайтов
        pygame.display.flip()  # Обновление экрана
        clock.tick(60)

    pygame.quit()


size = width, height = (1280, 720)
if __name__ == '__main__':
    mountain = Mountain(size)
    main()
