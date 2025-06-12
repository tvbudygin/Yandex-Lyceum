import pygame
import sys


def draws(screen, w, n):
    col = ["red", "green", "blue"]
    x_y = 0
    r = w * n
    for i in range(n):
        c = col[i % 3]
        pygame.draw.circle(screen, pygame.Color(c), (x_y + r, x_y + r), r)
        x_y += w
        r -= w


def main():
    try:
        w = 10
        print("введите количество кругов")
        n = int(input())
        assert w >= 0
        assert n >= 0
        pygame.init()
        screen = pygame.display.set_mode((300, 300))
        clock = pygame.time.Clock()
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("black")
            draws(screen, w, n)
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
    except Exception:
        print("Неправильный формат ввода")
        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    main()
