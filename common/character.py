from common.web import Web
from common.person import Person
from common.geneticAlgorithmParams import GeneticAlgorithmParams

import random


class Character:
    counter = 0
    characters_all = []

    def __init__(self, person: Person=None, web=None) -> None:
        self.person = person or Person()
        self.web = web or Web(randomize_power=1)
        self.fitness = 0
        Character.counter += 1
        Character.characters_all.append(self)

    def add_fitness(self, value): self.fitness += value
    def reset_fitness(self): self.fitness = 0
    def get_fitness(self): return self.fitness

    def reset_person(self): pass

    def move(self):
        self.person.move()

    def draw(self, display):
        self.person.draw(display)

    @staticmethod
    def calculate_new_population(genetic_algorithm_params: GeneticAlgorithmParams):
        Character.characters_all = sorted(Character.characters_all, key=lambda x: x.fitness, reverse=True) # Сортує по всіх від того хто з найбільшою фітнес до тих хто з найменшою

        # Нормує всіх, так щоб сума всіх фітнес функцій була 1
        suma = 0
        for i in range(len(Character.characters_all)):
            if Character.characters_all[i].fitness <= 0:
                Character.characters_all[i].fitness = 0.00001
            suma += Character.characters_all[i].fitness
        for i in range(len(Character.characters_all)):
            Character.characters_all[i].fitness /= suma
            Character.characters_all[i].web.print_neuro_chain()

        print(suma/len(Character.characters_all)) # fixme del after test

        count_of_alive = genetic_algorithm_params.get_count_of_alive_after_epoch() # Кількість виживших із минулого покоління
        web = []# Оригінальний список нейронок
        fitness = []# Оригінальний список фітнес функцій
        web_temp = []
        fitness_temp = []
        for i in range(len(Character.characters_all)):
            web.append(Character.characters_all[i].web)
            web_temp.append(Character.characters_all[i].web)
            fitness.append(Character.characters_all[i].fitness)
            fitness_temp.append(Character.characters_all[i].fitness)


        web_new = []  # всі нейронки,
        fitness_new = []  # всі фітнес функції
        for i in range(min(count_of_alive, len(fitness))):
            n = random.choices(range(len(web_temp)), fitness_temp, k=1)[0]
            web_new.append(web_temp.pop(n))
            fitness_new.append(fitness_temp.pop(n))

        # створення потомства і заповнення залишившихся слотів
        for i in range(len(web_new), len(web)):
            parents_web = random.choices(web, fitness, k=2) # Вибирається двоє батьків
            couple = parents_web[0].cross_crossover_several(parents_web[1],
                                                            point_number=genetic_algorithm_params.get_crossover_point_number(),
                                                            return_couple=True) # створення двох дітей
            web_new.append(couple[0])
            web_new.append(couple[1])
            i += 1

        # Мутації
        for i in range(len(web_new)):
            web_new[i].make_mutation(randomize_probability=genetic_algorithm_params.get_mutation_probability())

        # Оновлення вагів всіх осіб. Заміна старих значень на нові і обновлення стартових позицій
        for i in range(len(Character.characters_all)):
            Character.characters_all[i].web = web_new[i]
            Character.characters_all[i].fitness = 0
            Character.characters_all[i].person.reset_position(position=[random.randint(100, 1100), random.randint(100, 1100)])
