# жизнь на торе


import pygame


class Board:
    def __init__(self, n):
        self.width = n
        self.height = n
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 25
        self.top = 25
        self.cell_size = 700 // n
        self.color_t = True

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
                if self.board[y][x] != 0:
                    pygame.draw.rect(screen,
                                     pygame.Color("green"),
                                     (x * self.cell_size + self.left + 1,
                                      y * self.cell_size + self.top + 1,
                                      self.cell_size - 2,
                                      self.cell_size - 2))

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
        self.board[y][x] = int(not self.board[y][x])
        self.render(self.screen)


def main():
    try:
        pygame.init()
        size = 750, 750
        screen = pygame.display.set_mode(size)
        clock = pygame.time.Clock()
        print("введите количество квадратов")
        board = Board(int(input()))
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
    except Exception as e:
        print("invalid format", e)


if __name__ == '__main__':
    main()
