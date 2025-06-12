import pygame


class Circle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 10
        self.radius = 10

    def draw(self, screen):
        pygame.draw.circle(screen, pygame.Color("yellow"), (self.x, self.y), self.radius)

    def update(self):
        self.radius += 2


def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((500, 500))
        clock = pygame.time.Clock()
        running = True
        circles = []

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        b = Circle(event.pos[0], event.pos[1])
                        b.draw(screen)
                        circles = b
            screen.fill("blue")
            if circles:
                circles.draw(screen)
                circles.update()
            pygame.display.flip()
            clock.tick(60)

        pygame.quit()
    except Exception as e:
        print("неверный формат данных", e)


if __name__ == '__main__':
    main()
