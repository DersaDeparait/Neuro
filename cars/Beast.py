import random
import pygame
import math

class Beast:
    def __init__(self, position = [10, 10], floor = 100, ceiling = 900,  speed = [0, 0], size = 20, color = [200, 140, 70], only_circle = False, neuro = None):
        self.set_params(position, floor, ceiling, speed, size, color ,only_circle, neuro)
    def set_params(self, position = [10, 10], floor = 100, ceiling = 900,  speed = [0, 0], size = 20, color = [200, 140, 70], only_circle = False, neuro = None):
        self.position = [position[0], position[1]]

        self.floor = floor
        self.ceiling = ceiling

        self.angle = math.pi/2
        self.angle_speed = 0
        self.angle_acceleration = 0

        self.speed = [speed[0], speed[1]]
        self.acceleration = [0, 0]

        self.color = [color[0], color[1], color[2]]
        self.color_big = [0,0,0]
        self.color_eye = [250, 250, 250]
        self.color_dead = [120,120,120]
        self.color_dead_big = [80,80,80]
        self.color_dead_eye = [50,50,50]

        self.size = size
        self.size_small = self.size - 2
        self.size_eye = self.size / 3
        self.offset_eye = self.size * 0.6

        self.rule_spin_acceleration = 0.004
        self.rule_acceleration_forward = 0.1
        self.rule_acceleration_back = 0.02

        self.life = True
        self.only_circle = only_circle

        self.neuro = neuro

        self.life_time = 0
        self.fintes_last = 0
        self.fitnes_sum = 0
        self.fitnes_result = 0


    def calculate_move(self, distance):
        result = self.neuro.calculate_all([self.angle, *distance])
        result = self.__convert_to_bool(result)
        self.__rule(*result)
    def __convert_to_bool(self, result):
        for i in range(len(result)):
            if result[i] > 0: result[i] = True
            else: result[i] = False
        return result
    def __rule(self, clockwise = False, counterclockwise = False, forward = False, back = False):
        if clockwise: self.angle_acceleration += self.rule_spin_acceleration
        if counterclockwise: self.angle_acceleration -= self.rule_spin_acceleration
        if forward:
            self.acceleration[0] += self.rule_acceleration_forward * math.cos(self.angle)
            self.acceleration[1] += self.rule_acceleration_forward * math.sin(self.angle)
        if back:
            self.acceleration[0] -= self.rule_acceleration_back * math.cos(self.angle)
            self.acceleration[1] -= self.rule_acceleration_back * math.sin(self.angle)


    def possible_to_die(self, lazer_of_death, enemies):
        if self.position[0] < lazer_of_death[0].position: self.__die()
        if self.position[0] > lazer_of_death[1].position: self.__die()

        if self.position[1] + self.speed[1] + self.size >= self.ceiling: self.__die()
        if self.position[1] + self.speed[1] - self.size <= self.floor: self.__die()

        for i in range(len(enemies)):
            if math.sqrt((enemies[i].position[0] - self.position[0])**2 +
                    (enemies[i].position[1] - self.position[1])**2) < self.size + enemies[i].size :
                self.__die()
    def __die(self): self.life = False

    def update_fitnes_result(self, lazer_of_death, enemies):
        if self.life:
            self.life_time += 1
            self.fintes_last = min(abs(self.position[0] - lazer_of_death[0].position),
                         abs(self.position[0] - lazer_of_death[1].position)) # todo + self.size

            self.fintes_last = min(self.fintes_last,
                         abs(self.position[1] + self.speed[1] + self.size - self.ceiling),
                         abs(self.position[1] + self.speed[1] - self.size - self.floor))

            min_dist = math.sqrt((enemies[0].position[0] - self.position[0])**2 +(enemies[0].position[1] - self.position[1])**2) - self.size - enemies[0].size
            for i in range(1, len(enemies)):
                dist = math.sqrt((enemies[i].position[0] - self.position[0])**2 +(enemies[i].position[1] - self.position[1])**2) - self.size - enemies[i].size
                if dist < min_dist:
                    min_dist = dist
            self.fintes_last = min(self.fintes_last, min_dist)
            self.fintes_last = min_dist

            self.fitnes_sum += self.fintes_last
            self.fitnes_result = self.fitnes_sum / self.life_time
    def update(self, camera_move = None):
        if self.life:
            self.angle += self.angle_speed
            self.angle_speed += self.angle_acceleration
            self.angle_speed *= 0.98
            self.angle_acceleration = 0

            if self.position[1]+self.speed[1]+self.size>=self.ceiling: self.speed[1] = -abs(self.speed[1])
            if self.position[1]+self.speed[1]-self.size<=self.floor: self.speed[1] = abs(self.speed[1])

            for i in range(len(self.position)):
                self.position[i] = self.position[i] + self.speed[i]
                self.speed[i] = self.speed[i] + self.acceleration[i]
                self.speed[i] *= 0.993
                self.acceleration[i] = 0

        if camera_move != None and len(camera_move) == 2:
            self.position[0] -= camera_move[0]
            self.position[1] -= camera_move[1]


    def draw(self, display):
        if self.only_circle:
            pygame.draw.circle(display, self.color, [int(self.position[0]), int(self.position[1])], int(self.size))
        else:
            if self.life:
                pygame.draw.circle(display, self.color_big, [int(self.position[0]), int(self.position[1])], int(self.size))
                if self.size_small > 0: pygame.draw.circle(display, self.color, [int(self.position[0]), int(self.position[1])], int(self.size_small))
                pygame.draw.circle(display, self.color_eye, [int(self.position[0] + self.offset_eye * math.cos(self.angle)), int(self.position[1] + self.offset_eye * math.sin(self.angle))], int(self.size_eye))
            else:
                pygame.draw.circle(display, self.color_dead_big, [int(self.position[0]), int(self.position[1])], int(self.size))
                if self.size_small > 0: pygame.draw.circle(display, self.color_dead, [int(self.position[0]), int(self.position[1])], int(self.size_small))
                pygame.draw.circle(display, self.color_dead_eye, [int(self.position[0] + self.offset_eye * math.cos(self.angle)), int(self.position[1] + self.offset_eye * math.sin(self.angle))], int(self.size_eye))
