from common.web import Web
from common.person import Person

class Character:
    counter = 0
    characters_all = []

    def __init__(self, person: Person=None, web=None) -> None:
        self.person = person or Person()
        self.web = web or Web(randomize=1)
        self.fitness = 0
        Character.counter += 1
        Character.characters_all.append(self)

    def add_fitness(self, value): self.fitness += value
    def reset_fitness(self): self.fitness = 0
    def get_fitness(self): return self.fitness

    def reset_person(self): pass

    def draw(self, display):
        self.person.draw(display)
