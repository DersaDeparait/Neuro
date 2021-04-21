from common.web import Web
from common.character import Character
from test_1_lineral.personTest import PersonTest

import math


class CharacterTest(Character):

    def __init__(self, person=None, web=None) -> None:
        super(CharacterTest, self).__init__(person, web)

    def calculate(self, start_pos, end_pos, goal_relative):
        distance = []
        for i in range(self.web.layers[0]):
            distance.append(end_pos[i//2][i % 2] - start_pos[i//2][i%2])

        input_data = []
        for i in range(self.web.layers[0]):
            input_data.append((self.person.position[i] - start_pos[i//2][i%2])/distance[i])
        output = self.web.calculate_all(input_data)

        input_to_output = self.web.layers[-1]//self.web.layers[0]
        for i in range(self.web.layers[0]):
            self.person.speed[i] = output[i * input_to_output]
            for j in range(1, input_to_output):
                self.person.speed[i] += output[i*input_to_output+j] * 10**j

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
