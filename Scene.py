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
        self.read_data()
        self.save_data()

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

        self.iteration = 0
        self.epoch = 0

        self.population = config.START_POPULATION
        self.max_counter = config.MAX_COUNTER
        self.max_epoch = config.MAX_EPOCH
    def init_battlefield(self): pass
    def init_character(self): pass
    def read_data(self): pass


    def loop(self):
        while (self.run_epoch):
            while (self.run_iteration):
                self.rule()
                self.update()
                self.draw()
                self.clock_tick()
                self.count_counter()
                self.exit_iteration()

            self.evolution_operation()
            self.save_data()
            self.start_new_epoch()
            self.exit_epoch()
        pygame.quit()
    def evolution_operation(self): pass
    def save_data(self): pass
    def start_new_epoch(self):
        self.run_iteration = True
        self.iteration = 0
        self.epoch += 1
    def exit_epoch(self):
        if self.epoch >=self.max_epoch:
            self.run_epoch = False


    def rule(self): pass
    def update(self): pass
    def draw(self):
        self.__draw_fill_display()
        self.__draw_all()
        self.__draw_flip()
    def clock_tick(self): self.clock.tick(self.fps_default)
    def count_counter(self): self.iteration += 1
    def exit_iteration(self):
        if self.iteration >= self.max_counter:
            self.run_iteration = False

    def __draw_fill_display(self): self.display.fill(self.display_color)
    def __draw_all(self): pass
    def __draw_flip(self): pygame.display.flip()