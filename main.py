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
        if self.length > 1 and (point[0] * -1, point[1]*-1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        #          [x, y]
        cur_pos = self.get_head_position()
        x, y = self.direction
        new_pos = (((cur_pos[0] + (x*GRID_SIZE)) % SCREEN_WIDTH), (cur_pos[1]+(y*GRID_SIZE)) % SCREEN_HEIGTH)
        if len(self.positions) > 2 and new_pos in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new_pos)
            if len(self.positions) > self.length:
                self.positions.pop()

    def draw(self, surface):
        for pos in self.positions:
            cube = pygame.Rect((pos[0], pos[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, cube)
            pygame.draw.rect(surface, (93, 216, 228), cube, 1)

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # nahoru
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    self.turn(UP)
                #dolu
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                #doleva
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                #doprava
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)

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
    #vytvoreni nove instance snake a food
    snake = Snake()

    while True:
        clock.tick(10)
        snake.handle_keys()
        draw_grid(surface)
        snake.move()
        snake.draw(surface)

        screen.blit(surface, (0, 0))
        pygame.display.update()


if __name__ == '__main__':
    main()

