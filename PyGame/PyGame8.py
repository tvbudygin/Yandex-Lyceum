import pygame


def main():
    pygame.init()
    screen = pygame.display.set_mode((501, 501))
    screen2 = pygame.Surface(screen.get_size())
    screen2.fill((0, 0, 0))
    x1, y1, w, h = 0, 0, 0, 0
    rectangl = []
    drawing = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                drawing = True
                x1, y1 = event.pos
            if event.type == pygame.MOUSEBUTTONUP:
                screen2.blit(screen, (0, 0))
                drawing = False
                rectangl.append((x1, y1, w, h))
                x1, y1, w, h = 0, 0, 0, 0
            if event.type == pygame.MOUSEMOTION:
                if drawing:
                    w, h = event.pos[0] - x1, event.pos[1] - y1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    if len(rectangl) > 0:
                        rectangl.pop()
                        screen2.fill((0, 0, 0))
                        for i in rectangl:
                            pygame.draw.rect(screen2, (0, 0, 255), i, 5)
        screen.fill(pygame.Color('black'))
        screen.blit(screen2, (0, 0))
        if drawing:
            if w > 0 and h > 0:
                pygame.draw.rect(screen, (0, 0, 255), ((x1, y1), (w, h)), 5)
        pygame.display.flip()


if __name__ == '__main__':
    main()
