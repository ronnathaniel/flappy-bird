
import pygame as pyg
from random import randint as rnd
from bird import Bird


class Wall:
    def __init__(self, y, length):
        self.pos = [450, y]
        self.vel = [-2.4, 0]
        self.size = (40, length)
        self.passed = False

    def update(self):
        twice = range(2)
        for i in twice:
            self.pos[i] += self.vel[i]


class Brain:

    def __init__(self, parent=None):
        if not parent:
            self.need = rnd(0, 100) / 100

    @staticmethod
    def input(distance, top_height, bot_height, vel):
        #  return distance * (top_height - bot_height) // -15000 # 3 is right before, 2 is insidee
        pass


class Game:
    def __init__(self):
        self.setup()
        self.main()

    def setup(self):
        pyg.init()
        self.surface = pyg.display.set_mode((400, 400))
        pyg.display.set_caption("samo flappy bird")
        self.score = 0
        self.bird = Bird()
        self.walls = []
        self.wall_create()

    def update(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                break
        self.bird.update()
        for walls in self.walls:
            for wall in walls:
                wall.update()
        self.wall_check()
        self.rule_check()
        self.key_press()

        walls = self.closest_walls()
        distance = walls[1].pos[0]
        top = walls[0].pos[1] - self.bird.pos[1]
        bottom = walls[1].pos[1] - self.bird.pos[1]
        #print(Brain.input(distance, top, bottom))
        #print(self.closest_wall()[1].pos[0])

    def closest_walls(self):
        for walls in self.walls:
            if walls[1].pos[0] - self.bird.pos[0] > 0:
                return walls

    def wall_create(self):
        length = rnd(20, 240)
        top_wall = Wall(0, length)
        bot_wall = Wall(length+160, 400-160-length)
        self.walls.append((top_wall, bot_wall))

    def wall_check(self):
        # check only the first wall
        if self.walls[0][0].pos[0] + 30 < 0:
            self.walls.pop(0)
        if self.walls[len(self.walls)-1][0].pos[0] < 250:
            self.wall_create()

    def rule_check(self):
        bird_rect = pyg.Rect(*self.bird.pos, *self.bird.size)
        for walls in self.walls:
            if self.bird.pos[0] - walls[1].pos[0] > 4 and not walls[1].passed:
                walls[0].passed = True
                walls[1].passed = True
                self.score += 10
                print(self.score)
            for wall in walls:
                wall_rect = pyg.Rect(*wall.pos, *wall.size)
                if bird_rect.colliderect(wall_rect):
                    self.__init__()
        if self.bird.pos[1] + self.bird.size[1] > 400:
            self.__init__()

    def draw_background(self):
        pyg.draw.rect(self.surface, (0, 0, 255), (0, 0, 400, 400))

    def draw_bird(self):
        pyg.draw.rect(self.surface, (0, 255, 0), (*self.bird.pos, *self.bird.size))

    def draw_walls(self):
        for walls in self.walls:
            for wall in walls:
                pyg.draw.rect(self.surface, (255, 0, 0), (*wall.pos, *wall.size))

    def draw(self):
        pyg.display.flip()
        pyg.time.Clock().tick(60)
        self.draw_background()
        self.draw_bird()
        self.draw_walls()

    def key_press(self):
        press = pyg.key.get_pressed()
        esc = pyg.K_ESCAPE
        space = pyg.K_SPACE
        if press[esc]:
            pyg.quit()
        elif press[space]:
            self.bird.jump()

    def main(self):
        while 1:

            self.update()
            self.draw()


Game()
