import pygame
import sys
import random


class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGTH/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.color = (17, 24, 47)

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0]* -1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        pass
    def draw(self, surface):
        pass
    def handle_keys(self):
        pass

    def reset(self):
        self.length = 1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGTH/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0


class Food():
    def __init__(self):
        pass
    def randomize_position(self):
        pass
    def draw(self, surface):
        pass


def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x + y) % 2 == 0:
                cube = pygame.Rect((x*GRID_SIZE, y*GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (93, 216, 228), cube)
            else:
                cube1 = pygame.Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE))
                pygame.draw.rect(surface, (84, 194, 205), cube1)



#globalni
SCREEN_WIDTH = 480
SCREEN_HEIGTH = 480

GRID_SIZE = 20

GRID_WIDTH = SCREEN_WIDTH/GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGTH/GRID_SIZE
#     X,  Y
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

def main():
    pygame.init()

    # promenne pro clock, a velikost okna
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)
    while True:
        clock.tick(10)
        draw_grid(surface)

        screen.blit(surface, (0, 0))
        pygame.display.update()


if __name__ == '__main__':
    main()

