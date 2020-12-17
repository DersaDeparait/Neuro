from pygame import time
import pygame
import random
import os
import config

class Scene:
    def __init__(self):
        self.init_display()
        self.init_common()

        self.init_battlefield()
        self.init_character()

    def init_display(self):
        self.display_position = config.DISPLAY_POSITION
        self.display_size = config.DISPLAY_SIZE
        self.display_color = config.DISPLAY_COLOR
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % self.display_position
        pygame.init()
        self.display = pygame.display.set_mode(self.display_size)
        self.display.fill(self.display_color)
        self.fps_default = config.FPS
        self.clock = time.Clock()

    def init_common(self):
        self.run_iteration = True
        self.run_epoch = True

        self.iteration = -1
        self.epoch = -1

        self.population = config.START_POPULATION
        self.max_counter = config.MAX_COUNTER
        self.max_epoch = config.MAX_EPOCH
    def init_battlefield(self): pass
    def init_character(self): pass

    def loop(self):
        while (self.run_epoch):

            while (self.run_iteration):
                self.count_counter()
                self.rule()
                self.update()
                self.draw()
                self.clock_tick()
                self.exit_iteration()
        pygame.quit()
    def start_new_epoch(self):
        self.run_iteration = True
        self.iteration = -1

    def count_counter(self):
        self.counter += 1
    def rule(self):
        for i in range(len(self.beast)):
            lazer_distance = self.lazer_of_death[1].position - self.lazer_of_death[0].position
            distance_to_left_lazer_normed = (self.beast[i].position[0] - self.lazer_of_death[
                0].position) / lazer_distance
            distance_to_right_lazer_normed = (self.lazer_of_death[1].position - self.beast[i].position[
                0]) / lazer_distance
            result = self.neuro[i].calculate_bool(
                [self.beast[i].angle, distance_to_left_lazer_normed, distance_to_right_lazer_normed])
            self.beast[i].rule(clockwise=result[0], counterclockwise=result[1], forward=result[2], back=result[3])
    def update(self):
        for i in range(len(self.enemies)):
            self.enemies[i].update(self.camera_move)
            if self.enemies[i].position[0] + self.enemies[i].size < 0:
                self.enemies[i].position = [2000 + i * 300 + random.randrange(0, 500) + self.camera_move[0],
                                            random.randrange(self.floor, self.ceiling)]
                self.enemies[i].color = [random.randrange(100), random.randrange(255), random.randrange(255)]

        for i in range(len(self.lazer_of_death)):
            self.lazer_of_death[i].update()

        self.number_of_life = 0
        for i in range(len(self.beast)):
            self.beast[i].update(self.camera_move)
            if self.beast[i].position[0] < self.lazer_of_death[0].position: self.beast[i].die()
            if self.beast[i].position[0] > self.lazer_of_death[1].position: self.beast[i].die()
            if self.beast[i].life: self.number_of_life += 1
    def draw(self):
        self.display.fill(self.display_color)
        self.draw_enemies()
        self.draw_characters()
        self.draw_frame()
        self.draw_lazer_of_death()
        pygame.display.flip()
    def clock_tick(self):
        self.clock.tick(self.fps_default)
    def exit_iteration(self):
        if self.iteration >= self.max_counter:
            self.run_iteration = False


    def draw_enemies(self):
        for i in range(len(self.enemies)):
            self.enemies[i].draw(self.display)

    def draw_characters(self):
        for i in range(len(self.beast)):
            self.beast[i].draw(self.display)

    def draw_frame(self, frame_size=4, color=[255, 0, 255]):
        pygame.draw.line(self.display, color, [-1000 - self.camera_move[0], self.floor - self.camera_move[1]],
                         [self.display_size[0] * 1000 - self.camera_move[0], self.floor - self.camera_move[1]],
                         frame_size)
        pygame.draw.line(self.display, color, [-1000 - self.camera_move[0], self.ceiling - self.camera_move[1]],
                         [self.display_size[0] * 1000 - self.camera_move[0], self.ceiling - self.camera_move[1]],
                         frame_size)
        pass

    def draw_lazer_of_death(self):
        for i in range(len(self.lazer_of_death)):
            self.lazer_of_death[i].draw(self.display)