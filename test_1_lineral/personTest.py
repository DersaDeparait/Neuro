from common.person import Person
from random import randint


class PersonTest(Person):
    def __init__(self, position: list = [0, 0], color: list = [255, 255, 255], size: int = 20) -> None:
        super().__init__(position, color, size)

    def draw(self, display):
        if len(self.position) == 1:
            self.pygame.draw.circle(display, self.color, [int(self.position[0]), 500], int(self.size))
        elif len(self.position) >= 2:
            self.pygame.draw.circle(display, self.color, [int(self.position[0]), int(self.position[1])], int(self.size))

        if len(self.position) >= 4:
            self.pygame.draw.circle(display, self.color, [int(self.position[2]), int(self.position[3])], int(self.size))
        if len(self.position) >= 6:
            self.pygame.draw.circle(display, self.color, [int(self.position[4]), int(self.position[5])], int(self.size))
