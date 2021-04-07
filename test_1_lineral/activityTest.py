from common.activity import Activity
from common.dataWriter import DataWriter
from common.geneticAlgorithmParams import GeneticAlgorithmParams
from common.monitor import Monitor
from common.character import Character
from common.web import Web

from test_1_lineral.personTest import PersonTest
from test_1_lineral.characterTest import CharacterTest
from test_1_lineral.geneticAlgorithmParamsTest import GeneticAlgorithmParamsTest
from test_1_lineral.frame import Frame

import datetime
import random


class ActivityTest(Activity):# test 1 lineral
    def __init__(self, monitor: Monitor = None,
                 genetic_algorithm_params: GeneticAlgorithmParams = GeneticAlgorithmParamsTest(),
                 data_writer: DataWriter = None):
        self.start_pos = [100, 100]
        self.end_pos = [1100, 1100]
        self.distance = [self.end_pos[0]-self.start_pos[0], self.end_pos[1]-self.start_pos[1]]
        self.goal_relative = [900, 800]
        self.goal_absolute = [self.goal_relative[0] + self.start_pos[0], self.goal_relative[1] + self.start_pos[1]]
        super(ActivityTest, self).__init__(monitor, genetic_algorithm_params, data_writer)

    def _environment_init(self) -> None:
        self.environment = [Frame(start_pos=self.start_pos,
                                 end_pos=self.end_pos,
                                 goal_pos=self.goal_absolute)]

    def _character_init(self) -> None:
        self.character = []
        for i in range(self.genetic_algorithm_params.start_population):
            self.character.append(CharacterTest(person=PersonTest(
                color=[random.randint(10, 20), random.randint(0,50), random.randint(0,50)],
                position=[random.randint(self.start_pos[0], self.end_pos[0]),
                          random.randint(self.start_pos[1], self.end_pos[1])],
                size=10)))


    def _move_character(self):
        for i in range(len(self.character)):
            self.character[i].calculate(self.start_pos, self.end_pos, self.goal_relative)
            self.character[i].move()

    def _write_data_on_screen(self):
        self.monitor.write_data_on_screen("Test e:{}, i:{}".format(self.epoch, self.iteration))

    def _draw_all(self):
        self.monitor.draw(environment=self.environment, enemies=[], character=self.character)

    def _calculate_fitness_function_iteration(self):
        for i in range(len(self.character)):
            self.character[i].calculate_fitness(self.goal_absolute)





