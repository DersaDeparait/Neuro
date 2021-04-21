from common.activity import Activity
from common.dataWriter import DataWriter
from common.geneticAlgorithmParams import GeneticAlgorithmParams
from common.monitor import Monitor
from common.web import Web

from test_1_lineral.personTest import PersonTest
from test_1_lineral.characterTest import CharacterTest
from test_1_lineral.geneticAlgorithmParamsTest import GeneticAlgorithmParamsTest
from test_1_lineral.frame import Frame

import random


class ActivityTest(Activity): # test 1 lineral
    def __init__(self, monitor: Monitor = None,
                 genetic_algorithm_params: GeneticAlgorithmParams = GeneticAlgorithmParamsTest(),
                 data_writer: DataWriter = None):
        self.start_pos = [[100, 100], [1200, 100], [2300, 100]]
        self.end_pos = [[1100, 1100], [2200, 1100], [3300, 1100]]
        self.distance = [[self.end_pos[0][0] - self.start_pos[0][0], self.end_pos[0][1] - self.start_pos[0][1]],
                         [self.end_pos[1][0] - self.start_pos[1][0], self.end_pos[1][1] - self.start_pos[1][1]],
                         [self.end_pos[2][0] - self.start_pos[2][0], self.end_pos[2][1] - self.start_pos[2][1]]]
        self.goal_relative = [[900, 800], [300, 750], [200, 400]]
        self.goal_absolute = [[self.goal_relative[0][0] + self.start_pos[0][0], self.goal_relative[0][1] + self.start_pos[0][1]],
                              [self.goal_relative[1][0] + self.start_pos[1][0], self.goal_relative[1][1] + self.start_pos[1][1]],
                              [self.goal_relative[2][0] + self.start_pos[2][0], self.goal_relative[2][1] + self.start_pos[2][1]]]
        super(ActivityTest, self).__init__(monitor, genetic_algorithm_params, data_writer)

    def _environment_init(self) -> None:
        self.environment = []
        for i in range(len(self.start_pos)):
            self.environment.append(Frame(start_pos=self.start_pos[i],
                                          end_pos=self.end_pos[i],
                                          goal_pos=self.goal_absolute[i]))

    def _character_init(self) -> None:
        self.character = []
        for i in range(self.genetic_algorithm_params._start_population):
            position = []
            for i in range(self.genetic_algorithm_params.get_dimension()):
                position.append(random.randint(self.start_pos[i//2][i%2], self.end_pos[i//2][i%2]))


            self.character.append(CharacterTest(person=PersonTest(
                                                color=[random.randint(10, 20), random.randint(0, 50), random.randint(0, 50)],
                                                position=position,
                                                size=10),
                                    web=Web(self.genetic_algorithm_params.get_web_layers(), randomize_power=1)))


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
            self.character[i].calculate_fitness(self.goal_absolute[0])





