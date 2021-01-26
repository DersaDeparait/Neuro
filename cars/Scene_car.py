import pygame
import random
import config
from Scene import Scene
from cars.Beast import Beast
from cars.Lazer_of_death import Lazer_of_death
from web import Web
from cars.character_beast import Character_beast

class Scene_car(Scene):
    def __init__(self):
        super().__init__()

    def init_battlefield(self):
        super(Scene_car, self).init_battlefield()
        self.camera_move = config.CAR_CAMERA_MOVE_SPEED
        self.floor = config.CAR_FLOOR_POSITION
        self.ceiling = config.CAR_CEILING_POSITION

        self.lazer_of_death = [Lazer_of_death(config.CAR_LAZER_OF_DEATH_POSITION), Lazer_of_death(self.display_size[0] - config.CAR_LAZER_OF_DEATH_POSITION_REVERSE)]

        self.enemies_number = config.CAR_ENEMIES_NUMBER
        self.enemies = []
        for i in range(self.enemies_number):
            self.enemies.append(
                Beast(position=[i * 300 + random.randrange(0, 500), random.randrange(self.floor, self.ceiling)],
                      size=random.randrange(50, 200), only_circle=True,
                      color=[random.randrange(1,100), random.randrange(100, 255), random.randrange(255)]))
    def init_character(self):
        super(Scene_car, self).init_character()
        self.ball_number_of_parts = config.START_POPULATION
        self.ball_position_default = config.CAR_BALL_POSITION_DEFAULT

        self.character = []
        for i in range(self.ball_number_of_parts):
            self.character.append(Character_beast(person= Beast([self.ball_position_default[0],
                                                                 self.ball_position_default[1]],
                                                                self.floor,
                                                                self.ceiling,
                                                                )))
        self.number_of_life = 0


    def rule(self):
        for i in range(len(self.character)):
            self.character[i].calculate_move(self.lazer_of_death, self.ceiling, self.floor)
    def update(self):
        self.__update_enemies()
        self.__update_lazer_of_death()
        self.__update_beast()
        self.__update_display()
    def __update_enemies(self):
        for i in range(len(self.enemies)):
            self.enemies[i].update(self.camera_move)
            if self.enemies[i].position[0] + self.enemies[i].size < 0:
                self.enemies[i].position = [2000 + i * 300 + random.randrange(0, 500) + self.camera_move[0], random.randrange(self.floor, self.ceiling)]
                self.enemies[i].color=[random.randrange(1,100), random.randrange(100, 255), random.randrange(255)]
    def __update_lazer_of_death(self):
        for i in range(len(self.lazer_of_death)):
            self.lazer_of_death[i].update()
    def __update_beast(self):
        for i in range(len(self.character)):
            self.character[i].update(self.camera_move, self.lazer_of_death, self.enemies)
        self.number_of_life = Character_beast.how_many_alive()
    def __update_display(self):
        pygame.display.set_caption("Кількість живих: {0:5}, Ітерація:{1:5} Епоха:{2:5}"# // Фітнес результат -1: {3:5.2f}   -2: {4:5.2f}, {5}, {6}"
                                   .format(self.number_of_life,
                                           self.iteration,
                                           self.epoch))


    def exit_iteration(self):
        super().exit_iteration()
        self.number_of_life = Character_beast.how_many_alive()
        if self.number_of_life < 1:
            self.run_iteration = False


    def evolution_operation(self):
        Character_beast.calculate_end_epoch_0(self.ball_position_default, self.floor, self.ceiling)


    def _draw_all(self):
        self.draw_enemies()
        self.draw_characters()
        self.draw_frame()
        self.draw_lazer_of_death()
    def draw_enemies(self):
        for i in range(len(self.enemies)):
            self.enemies[i].draw(self.display)
    def draw_characters(self):
        for i in range(len(self.character)):
            self.character[i].draw(self.display)
    def draw_frame(self, frame_size = 4, color = [255, 0, 255]):
        pygame.draw.line(self.display, color, [-1000 - self.camera_move[0], self.floor - self.camera_move[1]], [self.display_size[0] * 1000 - self.camera_move[0], self.floor - self.camera_move[1]], frame_size)
        pygame.draw.line(self.display, color, [-1000 - self.camera_move[0], self.ceiling - self.camera_move[1]], [self.display_size[0] * 1000 - self.camera_move[0], self.ceiling - self.camera_move[1]], frame_size)
    def draw_lazer_of_death(self):
        for i in range(len(self.lazer_of_death)):
            self.lazer_of_death[i].draw(self.display)