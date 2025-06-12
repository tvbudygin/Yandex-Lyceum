import pygame


def draws(screen, p):
    pygame.draw.circle(screen, pygame.Color("white"), (p[0], p[1]), 10)



def main():
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    clock = pygame.time.Clock()
    circles = []
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                circles.append(event.pos)
        screen.fill("black")
        for i in circles:
            draws(screen, i)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == '__main__':
    main()
