import pygame

ALL_SPRITES = pygame.sprite.Group()
PATFORMS = pygame.sprite.Group()
PATFORMS_RED = pygame.sprite.Group()
square = None
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Лесенки")
clock = pygame.time.Clock()


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(PATFORMS)
        self.image = pygame.Surface((50, 10))
        self.image.fill((169, 169, 169))
        self.rect = self.image.get_rect(topleft=(x, y))


class Platform_red(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(PATFORMS_RED)
        self.image = pygame.Surface((10, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))


class Square(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__(ALL_SPRITES)
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed_y = 50 / 60
        self.platform_red = False

    def update(self, platforms, platforms_red):
        self.rect.y += self.speed_y
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.speed_y == 50 / 60:
                self.rect.bottom = platform.rect.top
                self.speed_y = 0
                break
        else:
            self.speed_y = 50 / 60
        self.platform_red = False
        for platform in platforms_red:
            if self.rect.colliderect(platform.rect) and self.speed_y == 50 / 60:
                self.platform_red = True
                self.speed_y = 0
                break

    def move(self, direction):
        print(self.platform_red)
        if direction == "l":
            self.rect.x -= 10
        elif direction == "r":
            self.rect.x += 10
        elif direction == "u" and self.platform_red:
            self.rect.y -= 10
        elif direction == "d" and self.platform_red:
            self.rect.y += 10


running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not (
                pygame.key.get_mods() & pygame.KMOD_CTRL):
            Platform(event.pos[0], event.pos[1])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and pygame.key.get_mods() & pygame.KMOD_CTRL:
            Platform_red(event.pos[0], event.pos[1])
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            if square is None:
                square = Square(event.pos[0], event.pos[1])
            else:
                square.rect.topleft = event.pos
                square.speed_y = 50 / 60

        if event.type == pygame.KEYDOWN:
            if square:
                if event.key == pygame.K_LEFT:
                    square.move("l")
                if event.key == pygame.K_RIGHT:
                    square.move("r")
                if event.key == pygame.K_UP:
                    square.move("u")
                if event.key == pygame.K_DOWN:
                    square.move("d")

    if square:
        square.update(PATFORMS, PATFORMS_RED)
    ALL_SPRITES.draw(screen)
    PATFORMS.draw(screen)
    PATFORMS_RED.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()