import pygame

class Person:
    def __init__(self, position:list = [0,0,0,0,0,0], color:list = [255,255,255], size: int = 20) -> None:
        self.pygame = pygame
        self.init(position,color,size)
        super().__init__()

    def init(self, position:list = [0,0,0,0,0,0], color:list = [255,255,255], size:int = 20):
        self.position = position or [0,0,0,0,0,0]
        self.speed = [0, 0, 0, 0, 0, 0]
        self.color = color or [255,255,255]
        self.size = size or 20

    def move(self):
        for i in range(len(self.position)):
            self.position[i] += self.speed[i]
            if self.position[i] > 1000000: self.position[i] = 1000000
            if self.position[i] < -1000000: self.position[i] = -1000000


    def reset_position(self, position):
        self.position = position

    def draw(self, display):
        self.pygame.draw.circle(display,
                                self.color,
                                [int(self.position[0]), int(self.position[1])],
                                int(self.size))

