from common.person import Person
from random import randint


class PersonTest(Person):
    def __init__(self, position: list = [0, 0], color: list = [255, 255, 255], size: int = 20) -> None:
        super().__init__(position, color, size)
