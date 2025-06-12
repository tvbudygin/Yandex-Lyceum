import pygame


class Board:
    def __init__(self):
        self.width = 10
        self.height = 7
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 25
        self.top = 25
        self.cell_size = 50
        self.color_t = True
        self.types = 1

    #     2 синий, 1 красный

    def render(self, screen):
        self.screen = screen
        for x in range(self.width):
            for y in range(self.height):
                pygame.draw.rect(screen,
                                 pygame.Color("white"),
                                 (x * self.cell_size + self.left,
                                  y * self.cell_size + self.top,
                                  self.cell_size,
                                  self.cell_size), 1)
                if self.board[y][x] == 1:
                    pygame.draw.circle(screen, pygame.Color("red"), (25 + (50 * x) + 25, 25 + (50 * y) + 25),
                                       23, 2)
                if self.board[y][x] == 2:
                    pygame.draw.line(screen, pygame.Color("blue"), (25 + (50 * x) + 2, 25 + (50 * y) + 2),
                                     (25 + (50 * (x + 1)) - 2, 25 + (50 * (y + 1)) - 2), 2)
                    pygame.draw.line(screen, pygame.Color("blue"),
                                     (25 + (50 * (x + 1)) - 2, 25 + (50 * y) + 2),
                                     (25 + (50 * x) + 2, 25 + (50 * (y + 1)) - 2), 2)

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def get_cell(self, mouse_pos):
        x = (mouse_pos[0] - self.left) // self.cell_size
        y = (mouse_pos[1] - self.top) // self.cell_size
        if 0 < x + 1 <= self.width and 0 < y + 1 <= self.height:
            return x, y

    def on_click(self, cell):
        x, y = cell
        if self.board[y][x] == 0:
            if self.types == 1:
                self.board[y][x] = 1
            else:
                self.board[y][x] = 2
            if self.types == 1:
                self.types = 2
            else:
                self.types = 1
        self.render(self.screen)


def main():
    pygame.init()
    size = 550, 400
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()
    board = Board()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.get_click(event.pos)

        screen.fill("black")
        board.render(screen)
        pygame.display.flip()
        clock.tick(4)

    pygame.quit()


if __name__ == '__main__':
    print("игра крестики нолики")
    main()