from common.web import Web
from common.character import Character
from test_1_lineral.personTest import PersonTest

import math


class CharacterTest(Character):

    def __init__(self, person=None, web=None) -> None:
        super(CharacterTest, self).__init__(person, web)
        # self.web = Web(layers=[2, 2], randomize=True)
        self.web = Web(layers=[2, 4], randomize_power=True)

    def calculate(self, start_pos, end_pos, goal_relative):
        distance = [end_pos[0] - start_pos[0], end_pos[1] - start_pos[1]]

        output = self.web.calculate_all([
                                            (self.person.position[0] - start_pos[0])/distance[0]
                                            ,
                                            (self.person.position[1] - start_pos[1])/distance[1]
                                        ])

        self.person.speed[0] = output[0]
        self.person.speed[0] += output[1] * 10
        self.person.speed[1] = output[2]
        self.person.speed[1] += output[3] * 10

    def calculate_fitness(self, goal_absolute):
        self.fitness += 1 / (0.1 + math.sqrt(
            (self.person.position[0] - goal_absolute[0]) ** 2
            +
            (self.person.position[1] - goal_absolute[1]) ** 2
        ))
        # self.fitness += 1 if self.person.speed[0] * (goal_absolute[0] - self.person.position[0]) > 0 else -1
        # self.fitness += 1 if self.person.speed[1] * (goal_absolute[1] - self.person.position[1]) > 0 else -1
        self.fitness += self.person.speed[0] * (goal_absolute[0] - self.person.position[0]) / 1000
        self.fitness += self.person.speed[1] * (goal_absolute[1] - self.person.position[1]) / 1000
