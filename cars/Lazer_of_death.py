import random
import pygame
from cars.Beast import Beast

class Lazer_of_death:
    def __init__(self, position = 50):
        self.position = position

    def update(self, add_position = 0):
        self.position += add_position

    def draw(self, display):
        pygame.draw.line(display, [255, 0, 0], [self.position, 0], [self.position, 2000], 4)