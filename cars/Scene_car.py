from pygame import time
import pygame
import random
import os
import config
from Scene import Scene
from cars.Beast import Beast
from cars.Lazer_of_death import Lazer_of_death
from cars.neuro import Neuro

class Scene_car(Scene):
    def __init__(self):
        super().__init__()

    def init_battlefield(self):
        super(Scene_car, self).init_battlefield()
        self.camera_move = [2, 0]
        self.floor = 100
        self.ceiling = 900

        self.lazer_of_death = [Lazer_of_death(50), Lazer_of_death(self.display_size[0] - 50)]

        self.enemies_number = 10
        self.enemies = []
        for i in range(self.enemies_number):
            self.enemies.append(
                Beast(position=[i * 300 + random.randrange(0, 500), random.randrange(self.floor, self.ceiling)],
                      size=random.randrange(50, 200), only_circle=True,
                      color=[random.randrange(55), random.randrange(255), random.randrange(255)]))
    def init_character(self):
        super(Scene_car, self).init_character()
        self.ball_number_of_parts = 1300
        self.ball_position_default = [500, 500]
        self.beast = []
        self.neuro = []
        for i in range(self.ball_number_of_parts):
            self.beast.append(Beast([self.ball_position_default[0], self.ball_position_default[1]], self.floor, self.ceiling))
            self.neuro.append(Neuro())
        self.beast[0].color = (0, 255, 255)
        self.number_of_life = 0


    def loop(self):
        while(self.run):
            self.rule()
            self.update()
            pygame.display.set_caption(str(self.beast[0].position[0]))#"FPS: " + str(int(self.clock.get_fps())) + " Counter: " + str(self.counter) + " Beast: " + str(self.number_of_life) + "/" + str(len(self.beast)))
            self.draw()
            self.clock.tick(self.fps_default)
        pygame.quit()


    def rule(self):
        for i in range(len(self.beast)):
            lazer_distance = self.lazer_of_death[1].position - self.lazer_of_death[0].position
            distance_to_left_lazer_normed = (self.beast[i].position[0] - self.lazer_of_death[0].position) / lazer_distance
            distance_to_right_lazer_normed = (self.lazer_of_death[1].position - self.beast[i].position[0]) / lazer_distance
            result = self.neuro[i].calculate_bool([self.beast[i].angle, distance_to_left_lazer_normed, distance_to_right_lazer_normed])
            self.beast[i].rule(clockwise=result[0], counterclockwise=result[1], forward=result[2], back=result[3])


    def update(self):
        for i in range(len(self.enemies)):
            self.enemies[i].update(self.camera_move)
            if self.enemies[i].position[0] + self.enemies[i].size < 0:
                self.enemies[i].position = [2000 + i * 300 + random.randrange(0, 500) + self.camera_move[0], random.randrange(self.floor, self.ceiling)]
                self.enemies[i].color = [random.randrange(100), random.randrange(255), random.randrange(255)]

        for i in range(len(self.lazer_of_death)):
            self.lazer_of_death[i].update()

        self.number_of_life = 0
        for i in range(len(self.beast)):
            self.beast[i].update(self.camera_move)
            if self.beast[i].position[0] < self.lazer_of_death[0].position:self.beast[i].die()
            if self.beast[i].position[0] > self.lazer_of_death[1].position:self.beast[i].die()
            if self.beast[i].life : self.number_of_life += 1



    def draw(self):
        self.display.fill(self.display_color)
        self.draw_enemies()
        self.draw_characters()
        self.draw_frame()
        self.draw_lazer_of_death()
        pygame.display.flip()
    def draw_enemies(self):
        for i in range(len(self.enemies)):
            self.enemies[i].draw(self.display)
    def draw_characters(self):
        for i in range(len(self.beast)):
            self.beast[i].draw(self.display)
    def draw_frame(self, frame_size = 4, color = [255, 0, 255]):
        pygame.draw.line(self.display, color, [-1000 - self.camera_move[0], self.floor - self.camera_move[1]], [self.display_size[0] * 1000 - self.camera_move[0], self.floor - self.camera_move[1]], frame_size)
        pygame.draw.line(self.display, color, [-1000 - self.camera_move[0], self.ceiling - self.camera_move[1]], [self.display_size[0] * 1000 - self.camera_move[0], self.ceiling - self.camera_move[1]], frame_size)
        pass
    def draw_lazer_of_death(self):
        for i in range(len(self.lazer_of_death)):
            self.lazer_of_death[i].draw(self.display)