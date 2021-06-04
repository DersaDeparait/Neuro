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
            for j in range(self.genetic_algorithm_params.get_dimension()):
                position.append(random.randint(self.start_pos[j // 2][j % 2], self.end_pos[j // 2][j % 2]))

            web = Web(self.genetic_algorithm_params.get_web_layers(), randomize_power=1)
            person = PersonTest(color=[random.randint(10, 20), random.randint(0, 50), random.randint(0, 50)],#[i * 80, i * 80, 100],
                                position=position,
                                size=10,#5 + i * 5,
                                default_position_range=[self.start_pos, self.end_pos])
            self.character.append(CharacterTest(person=person, web=web))


    def _move_character(self):
        for i in range(len(self.character)):
            self.character[i].calculate(self.start_pos, self.end_pos, self.goal_relative)
            self.character[i].move()

    def _write_data_on_screen(self):
        self.monitor.write_data_on_screen("layers: {},  popul: {},  elita: {}, alive_after_epoch: {} mutation: {:.3%} |||| e:{}, i:{}"
                                          .format(self.genetic_algorithm_params.get_web_layers(),
                                                  self.genetic_algorithm_params.get_start_population(),
                                                  self.genetic_algorithm_params.get_count_elitism(),
                                                  self.genetic_algorithm_params.get_count_of_alive_after_epoch(),
                                                  self.genetic_algorithm_params.get_mutation_probability(),
                                                  self.epoch, self.iteration
                                                  ))

        # text = ""
        # for i in range(len(self.character)):
        #     t_n = self.character[i].web.get_neuro_chain()
        #     t0 = ""
        #     for pos in self.character[i].person.position:
        #         t0 += "{:.3f} ".format((pos - 100)/1000)
        #     t1 = ""
        #     for j in range(min(len(self.character[i].person.speed), 2)):
        #         t1 += "{:.3f} ".format(self.character[i].person.speed[j])
        #     text += "{}) chain: {} pos: {} sp: {} ||| ".format(i, t_n, t0, t1)
        # print(self.iteration, text)

        # print("1: {}, {} | 2: {},{} | 3: {},{} | 4: {},{}"
        #                                   .format(self.character[0].person.position, self.character[0].person.speed,
        #                                           self.character[1].person.position, self.character[1].person.speed,
        #                                           self.character[2].person.position, self.character[2].person.speed,
        #                                           self.character[3].person.position, self.character[3].person.speed))

    def _draw_all(self):
        self.monitor.draw(environment=self.environment, enemies=[], character=self.character)

    def _calculate_fitness_function_iteration(self):
        for i in range(len(self.character)):
            self.character[i].calculate_fitness(self.goal_absolute, frame=[self.start_pos,self.end_pos],
                                                geneticAlgorithmParamsTest=self.genetic_algorithm_params)
