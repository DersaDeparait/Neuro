import config
import random
from web import Web

class Character:
    iterator = 0
    web_father = None
    web_mother = None
    characters_all = []
    characters_web_temp = []
    max = 0

    def __init__(self, person = None, web = None):
        self.person = person

        if web != None: self.web = web
        else: self.web = Web(randomize = 1)

        self.fitnes = 0
        self.fitnes_radical = 0

        Character.iterator += 1

        Character.characters_all.append(self)

    def set_web(self): pass

    def iteration_done(self):
        self.fitnes += 0
        self.fitnes_radical += 0

    def epoch_done(self):
        self.fitnes += 0
        self.fitnes_radical += 0


    @staticmethod
    def calculate_end_epoch():
        Character._calculate_max()
        Character._make_parents_roulette_unique()
        Character._make_who_not_die()
        Character._make_new_population()
        Character._make_mutation()
        Character._reset_position()
        Character._remake_the_same()

    @staticmethod
    def _calculate_max():
        Character.max = 0
        for i in range(1, len(Character.characters_all)):
            if (Character.characters_all[i].fitnes
                    > Character.characters_all[Character.max].fitnes):
                Character.max = i

    @staticmethod
    def _tournament(): pass
    @staticmethod
    def _make_parents_roulette_unique():
        index_all = []
        fitnes_all = []
        for i in range(len(Character.characters_all)):
            index_all.append(i)
            fitnes_all.append(Character.characters_all[i].fitnes)


        index_father = []
        index_mother = []
        for i in range(config.NUMBER_OF_PARENTS_COUPLES):
            index_father.append(random.choices(index_all, fitnes_all, k = 1)[0])
            index = index_father.index(index_father[i])
            index_all.pop(index)
            fitnes_all.pop(index)

            index_mother.append(random.choices(index_all, fitnes_all, k = 1)[0])
            index = index_mother.index(index_mother[i])
            index_all.pop(index)
            fitnes_all.pop(index)

        Character.web_father = []
        Character.web_mother = []

        for i in range(config.NUMBER_OF_PARENTS_COUPLES):
            Character.web_father.append(Character.characters_all[index_father[i]].web)
            Character.web_mother.append(Character.characters_all[index_mother[i]].web)
    @staticmethod
    def _make_parents_roulette_not_unique():
        sum_value = 0
        for i in range(len(Character.characters_all)):
            sum_value += Character.characters_all[i].fitnes

        index_all = []
        fitnes_all = []
        for i in range(len(Character.characters_all)):
            index_all.append(i)
            fitnes_all.append((Character.characters_all[i].fitnes)/sum_value)
        #     print("{0:>5}  {1:10.1f}  {2:10.4f}".format(i, Character.characters_all[i].fitnes, fitnes_all[i]), end= "  >  ")
        #     print(Character.characters_all[i].web.axon_weigh)
        # print()

        index_father = []
        index_mother = []
        for i in range(config.NUMBER_OF_PARENTS_COUPLES):
            index_father.append(random.choices(index_all, fitnes_all, k = 1)[0])
            index = index_father.index(index_father[i])
            to_append_index = index_all.pop(index)
            to_append_fitnes = fitnes_all.pop(index)
            index_mother.append(random.choices(index_all, fitnes_all, k = 1)[0])
            index_all.append(to_append_index)
            fitnes_all.append(to_append_fitnes)

        Character.web_father = []
        Character.web_mother = []

        for i in range(config.NUMBER_OF_PARENTS_COUPLES):
            Character.web_father.append(Character.characters_all[index_father[i]].web)
            Character.web_mother.append(Character.characters_all[index_mother[i]].web)

        # print(index_father)
        # print(index_mother)

    @staticmethod
    def _make_who_not_die():
        index_all = []
        fitnes_all = []
        for i in range(len(Character.characters_all)):
            index_all.append(i)
            fitnes_all.append(Character.characters_all[i].fitnes)

        Character.characters_web_temp = []
        for i in range(config.COUNT_OF_ALIVE_AFTER_EPOCH):
            index = random.choices(index_all, fitnes_all, k = 1)[0]
            Character.characters_web_temp.append(Character.characters_all[index].web)
            index_all.remove(index)
            fitnes_all.remove(Character.characters_all[index].fitnes)

    @staticmethod
    def _make_new_population():
        start = len(Character.characters_web_temp)
        for i in range(start, config.START_POPULATION):
            number = i % config.NUMBER_OF_PARENTS_COUPLES

            Character.characters_web_temp.extend(Character.web_father[number]
                                                 .cross_crossover_several(
                                                 Character.web_mother[number], config.CROSSOVER_POINT_NUMBER, return_couple = True))

        for i in range(len(Character.characters_all)):
            Character.characters_all[i].web = Character.characters_web_temp[i]

    @staticmethod
    def _make_mutation():
        for i in range(len(Character.characters_all)):
            Character.characters_all[i].web.make_mutation(config.MUTATION_POWER)

    @staticmethod
    def _reset_position():
        for i in range(len(Character.characters_all)):
            Character.characters_all[i].person.reset_position()
            Character.characters_all[i].fitnes = 0

    @staticmethod
    def _remake_the_same():
        for i in range(len(Character.characters_all)):
            for j in range(i + 1, len(Character.characters_all)):
                if Character.characters_all[i].web == Character.characters_all[j].web:
                    Character.characters_all[j].web.randomize(size = 0.1)



    @staticmethod
    def save_to_db_fitnes():
        d = {}
        for i in range(len(Character.characters_all)):
            d["f_{}".format(i)] = [Character.characters_all[i].fitnes]
            d["fr_{}".format(i)] = [Character.characters_all[i].fitnes_radical]
        return d

    @staticmethod
    def save_to_db_last_web():
        d = {}
        d.update(Character.characters_all[Character.max].web.axon_line(0))
        return d