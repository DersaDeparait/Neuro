from common.web import Web
from common.character import Character
from test_1_lineral.personTest import PersonTest
from test_1_lineral.geneticAlgorithmParamsTest import GeneticAlgorithmParamsTest

import math


class CharacterTest(Character):

    def __init__(self, person=None, web=None, default_position_range=None) -> None:
        super(CharacterTest, self).__init__(person, web, default_position_range)

    def calculate(self, start_pos, end_pos, goal_relative):
        distance = []
        for i in range(self.web.layers[0]):
            distance.append(end_pos[i // 2][i % 2] - start_pos[i // 2][i % 2])

        input_data = []
        for i in range(self.web.layers[0]):
            input_data.append((self.person.position[i] - start_pos[i // 2][i % 2]) / distance[i])
        output = self.web.calculate_all(input_data)

        input_to_output = self.web.layers[-1]//self.web.layers[0]
        for i in range(self.web.layers[0]):
            self.person.speed[i] = output[i * input_to_output] #1 if output[i * input_to_output] > 0.05 else (-1 if output[i * input_to_output]<-0.05 else 0)
            for j in range(1, input_to_output):
                self.person.speed[i] += output[i * input_to_output+j] * 10**j


    def calculate_fitness(self, goal_absolute, frame, geneticAlgorithmParamsTest:GeneticAlgorithmParamsTest):

        if geneticAlgorithmParamsTest.get_fitness_way_distance() == 1:
            sum_of_squers = 0
            for i in range(geneticAlgorithmParamsTest.get_dimension()):
                sum_of_squers += (self.person.position[i] - goal_absolute[i // 2][i % 2])**2
            self.fitness += 1 / (1 + math.sqrt(sum_of_squers))

        if geneticAlgorithmParamsTest.get_fitness_way_side() == 1:
            for i in range(geneticAlgorithmParamsTest.get_dimension()):
                self.fitness += 1 if self.person.speed[i] * (goal_absolute[i // 2][i % 2] - self.person.position[i]) > 0 else -1

        if geneticAlgorithmParamsTest.get_fitness_way_vector() == 1:
            if geneticAlgorithmParamsTest.get_dimension() == 1:
                self.fitness += 1 if self.person.speed[0] * (goal_absolute[0][0] - self.person.position[0]) > 0 else -1
            else:
                for i in range(geneticAlgorithmParamsTest.get_dimension()//2):
                    self.fitness += CharacterTest.find_cos_angle(central_point=[self.person.position[2*i], self.person.position[2*i+1]],
                                                                 speed_vector=[self.person.speed[2*i], self.person.speed[2*i+1]],
                                                                 goal_vector=[goal_absolute[i][0], goal_absolute[i][1]])
        if geneticAlgorithmParamsTest.get_fitness_way_kill_all_unwanted() == 1:
            for i in range(geneticAlgorithmParamsTest.get_dimension()):
                if self.person.position[i] > frame[1][i//2][i%2] or self.person.position[i] < frame[0][i//2][i%2]:
                    self.fitness = 0



    @staticmethod
    def find_cos_angle(central_point, speed_vector, goal_vector):
        return CharacterTest.cos_angle(vector1=speed_vector,
                                       vector2=[goal_vector[0] - central_point[0], goal_vector[1] - central_point[1]])
    @staticmethod
    def cos_angle(vector1, vector2):
        numerator = vector1[0] * vector2[0] + vector1[1] * vector2[1]
        denominator = (vector1[0] ** 2 + vector1[1] ** 2) ** 0.5 * (vector2[0] ** 2 + vector2[1] ** 2) ** 0.5
        return 0 if denominator == 0 else numerator / denominator
