import pygame


def render(screen, x, y):
    pygame.draw.circle(screen, pygame.Color("red"), (x, y), 20)


def main():
    pygame.init()
    screen = pygame.display.set_mode((501, 501))
    clock = pygame.time.Clock()
    running = True
    x, y = 501 // 2, 501 // 2
    x_n, y_n = 501 // 2, 501 // 2
    speed = 5
    move = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x_n, y_n = event.pos
                move = True

        screen.fill("black")
        if move:
            if x != x_n and y != y_n:
                if x < x_n:
                    x += min(speed, x_n - x)
                elif x > x_n:
                    x -= min(speed, x - x_n)
                if y < y_n:
                    y += min(speed, y_n - y)
                elif y > y_n:
                    y -= min(speed, y - y_n)
            elif x != x_n:
                if x < x_n:
                    x += min(speed, x_n - x)
                elif x > x_n:
                    x -= min(speed, x - x_n)
            elif y != y_n:
                if y < y_n:
                    y += min(speed, y_n - y)
                elif y > y_n:
                    y -= min(speed, y - y_n)

        if x == x_n and y == y_n:
            move = False
        render(screen, x, y)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
