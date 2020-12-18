import pygame
import random
import config
from Scene import Scene
from cars.Beast import Beast
from cars.Lazer_of_death import Lazer_of_death
from neuro.Web import Web

class Scene_car(Scene):
    def __init__(self):
        super().__init__()

    def init_battlefield(self):
        super(Scene_car, self).init_battlefield()
        self.camera_move = [2, 0]
        self.floor = 100
        self.ceiling = 900

        self.lazer_of_death = [Lazer_of_death(50), Lazer_of_death(self.display_size[0] - 50)]

        self.enemies_number = 20
        self.enemies = []
        for i in range(self.enemies_number):
            self.enemies.append(
                Beast(position=[i * 300 + random.randrange(0, 500), random.randrange(self.floor, self.ceiling)],
                      size=random.randrange(50, 200), only_circle=True,
                      color=[random.randrange(1,100), random.randrange(100, 255), random.randrange(255)]))
    def init_character(self):
        super(Scene_car, self).init_character()
        self.ball_number_of_parts = config.START_POPULATION
        self.ball_position_default = [500, 500]
        self.beast = []
        self.neuro = []
        for i in range(self.ball_number_of_parts):
            self.beast.append(Beast([self.ball_position_default[0], self.ball_position_default[1]],
                                    self.floor, self.ceiling, neuro=Web([5,4], randomize=0.1)))
        self.number_of_life = 0


    def evolution_operation(self):
        life_beast = []
        for i in range(len(self.beast)):
            if self.beast[i].life:
                life_beast.append(self.beast[i])

        if len(life_beast)<1:
            life_beast.append(Beast([self.ball_position_default[0], self.ball_position_default[1]],
                                    self.floor, self.ceiling, neuro=Web([5,4], randomize=0.1)))

        for i in range(len(self.beast)):
            if not self.beast[i].life:
                neuro = random.choice(life_beast).neuro.new_randomize_deep_copy()
                self.beast[i].set_params([self.ball_position_default[0], self.ball_position_default[1]],
                                    self.floor, self.ceiling, neuro=neuro)


    def rule(self):
        for i in range(len(self.beast)):
            lazer_distance = self.lazer_of_death[1].position - self.lazer_of_death[0].position
            distance_to_left_lazer_normed = (self.beast[i].position[0] - self.lazer_of_death[0].position) / lazer_distance
            distance_to_right_lazer_normed = (self.lazer_of_death[1].position - self.beast[i].position[0]) / lazer_distance
            wall_distance = self.ceiling - self.floor
            distance_to_up_wall_normed = (self.ceiling - self.beast[i].position[1]) / wall_distance
            distance_to_down_wall_normed = (self.beast[i].position[1] - self.floor) / wall_distance

            self.beast[i].calculate_move([distance_to_left_lazer_normed, distance_to_right_lazer_normed,
                                          distance_to_up_wall_normed, distance_to_down_wall_normed])
    def update(self):
        for i in range(len(self.enemies)):
            self.enemies[i].update(self.camera_move)
            if self.enemies[i].position[0] + self.enemies[i].size < 0:
                self.enemies[i].position = [2000 + i * 300 + random.randrange(0, 500) + self.camera_move[0], random.randrange(self.floor, self.ceiling)]
                self.enemies[i].color=[random.randrange(1,100), random.randrange(100, 255), random.randrange(255)]

        for i in range(len(self.lazer_of_death)):
            self.lazer_of_death[i].update()

        self.number_of_life = 0
        for i in range(len(self.beast)):
            self.beast[i].update(self.camera_move)
            self.beast[i].possible_to_die(self.lazer_of_death, self.enemies)
            if self.beast[i].life : self.number_of_life += 1
        pygame.display.set_caption("Кількість живих: {0:5}, Ітерація:{1:5} Епоха:{2:5}".format(self.number_of_life, self.iteration, self.epoch))

    def exit_iteration(self):
        super().exit_iteration()
        for i in range(len(self.beast)):
            if self.beast[i].life:
                return
        self.run_iteration = False

    def draw_all(self):
        self.draw_enemies()
        self.draw_characters()
        self.draw_frame()
        self.draw_lazer_of_death()
    def draw_enemies(self):
        for i in range(len(self.enemies)):
            self.enemies[i].draw(self.display)
    def draw_characters(self):
        for i in range(len(self.beast)):
            self.beast[i].draw(self.display)
    def draw_frame(self, frame_size = 4, color = [255, 0, 255]):
        pygame.draw.line(self.display, color, [-1000 - self.camera_move[0], self.floor - self.camera_move[1]], [self.display_size[0] * 1000 - self.camera_move[0], self.floor - self.camera_move[1]], frame_size)
        pygame.draw.line(self.display, color, [-1000 - self.camera_move[0], self.ceiling - self.camera_move[1]], [self.display_size[0] * 1000 - self.camera_move[0], self.ceiling - self.camera_move[1]], frame_size)
    def draw_lazer_of_death(self):
        for i in range(len(self.lazer_of_death)):
            self.lazer_of_death[i].draw(self.display)