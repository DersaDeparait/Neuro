from common.person import Person
from random import randint


class PersonTest(Person):
    def __init__(self, position: list = [0, 0], color: list = [255, 255, 255], size: int = 20, default_position_range=None) -> None:
        self.color2 = [randint(2, 50), randint(100, 200), randint(10,50)]
        self.color3 = [randint(2, 50), randint(10, 20), randint(100,200)]
        super().__init__(position, color, size, default_position_range)

    def draw(self, display):
        if len(self.position) == 1:
            self.pygame.draw.circle(display, self.color, [int(self.position[0]), 500], int(self.size))
        elif len(self.position) >= 2:
            self.pygame.draw.circle(display, self.color, [int(self.position[0]), int(self.position[1])], int(self.size))

        if len(self.position) >= 4:
            self.pygame.draw.circle(display, self.color2, [int(self.position[2]), int(self.position[3])], int(self.size))
        if len(self.position) >= 6:
            self.pygame.draw.circle(display, self.color3, [int(self.position[4]), int(self.position[5])], int(self.size))
