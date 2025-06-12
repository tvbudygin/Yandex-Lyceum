import pygame
import sys
import os

ALL_SPRITES = pygame.sprite.Group()


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f'Файл с изображением {fullname} не найден')
        sys.exit()
    image = pygame.image.load(fullname)
    return image


class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(ALL_SPRITES)
        self.image = load_image("arrow.png")
        self.rect = self.image.get_rect()

    def update(self, k):
        self.rect.center = k


def main():
    pygame.init()
    size = 300, 300
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    a = Arrow()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if pygame.mouse.get_focused():
                a.update(pygame.mouse.get_pos())

        screen.fill("black")
        ALL_SPRITES.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
