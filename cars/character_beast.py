from character import Character
import random
import config
import math

class Character_beast(Character):
    def __init__(self, person = None, web = None):
        super().__init__(person, web)
        if Character_beast.iterator == 1: person.color = [0, 0, 255]
        # if Character_beast.iterator == 998: person.color = [0, 0, 255]
        # if Character_beast.iterator == 999: person.color = [0, 255, 0]
        # if Character_beast.iterator == 1000: person.color = [255, 0, 0]

    def calculate_move(self, lazer_of_death, ceiling, floor, enemies):
        lazer_distance = lazer_of_death[1].position - lazer_of_death[0].position
        distance_to_left_lazer_normed = (self.person.position[0] - lazer_of_death[0].position) / lazer_distance
        distance_to_right_lazer_normed = (lazer_of_death[1].position - self.person.position[0]) / lazer_distance
        wall_distance = ceiling - floor
        distance_to_up_wall_normed = (ceiling - self.person.position[1]) / wall_distance
        distance_to_down_wall_normed = (self.person.position[1] - floor) / wall_distance




        enemies_distances = {}
        for i in range(len(enemies)):
            enemies_distances[math.sqrt((self.person.position[0] - enemies[i].position[0] - enemies[i].size)**2 +
                     (self.person.position[1] - enemies[i].position[1] - enemies[i].size)**2)] = i

        keys = sorted(enemies_distances)
        enem_dis_and_angle = []
        for i in range(config.CAR_COUNT_OF_IMPORTANT_ENEMIES_TO_NEURO):
            this_key = enemies_distances[keys[-i]]
            enem_dis_and_angle.append( math.sqrt((self.person.position[0] - enemies[this_key].position[0] - enemies[i].size)**2 +
                         (self.person.position[1] - enemies[this_key].position[1] - enemies[i].size)**2)
                        / lazer_distance)
            angle = math.atan2(self.person.position[1] - enemies[this_key].position[1],
                                   self.person.position[0] - enemies[this_key].position[0])
            # angle -= self.person.angle
            y = math.sin(angle)
            x = math.cos(angle)
            enem_dis_and_angle.append(y)
            enem_dis_and_angle.append(x)



        self.person.calculate_move(self.web, [distance_to_left_lazer_normed,
                                      distance_to_right_lazer_normed,
                                      distance_to_up_wall_normed,
                                      distance_to_down_wall_normed,
                                      *enem_dis_and_angle
                                              ])
    def update(self, camera_move, lazer_of_death, enemies):
        self.person.possible_to_die_from_frame(lazer_of_death)
        # self.person.possible_to_die_from_enemies(enemies)
        self.person.update_life_time()
        self.fitnes += self.person.update_fitnes_walls(lazer_of_death) * config.CAR_HOW_MANY_COST_BE_IN_MIDDLE
        # self.fitnes += self.person.update_fitnes_enemies(enemies) * config.CAR_HOW_MANY_COST_BE_FAR_FROM_ENEMIES
        self.person.update(camera_move)
    def draw(self, display):
        self.person.draw(display)

    @staticmethod
    def how_many_alive():
        counter = 0
        for i in range(len(Character_beast.characters_all)):
            if Character_beast.characters_all[i].person.life:
                counter += 1
        return counter




    def epoch_done(self):
        if self.person.life:
            self.fitnes += config.CAR_HOW_MANY_COST_ALIVE

    @staticmethod
    def calculate_end_epoch_custom():
        Character_beast.wayOfLife_simple_crossover()
        # super().calculate_end_epoch()
        Character_beast._reset_position()
        Character_beast._remake_the_same()

    @staticmethod
    def wayOfLife_copy_neuro_from_random_alive_to_dead():
        life_beast = []
        for i in range(len(Character_beast.characters_all)):
            if Character_beast.characters_all[i].person.life:
                life_beast.append(Character_beast.characters_all[i])

        if len(life_beast) < 1:
            life_beast.append(Character_beast.characters_all[0])
            life_beast[0].person.neuro.randomize(1)

        for i in range(len(Character_beast.characters_all)):
            if not Character_beast.characters_all[i].person.life:
                Character_beast.characters_all[i].web = random.choice(life_beast).web.new_randomize_deep_copy()

    @staticmethod
    def wayOfLife_copy_neuro_from_best_to_dead():
        life_beast = Character_beast.characters_all[0]
        for i in range(1, len(Character_beast.characters_all)):
            if Character_beast.characters_all[i].fitnes > life_beast.fitnes:
                life_beast = Character_beast.characters_all[i]

        for i in range(len(Character_beast.characters_all)):
            if not Character_beast.characters_all[i].person.life:
                Character_beast.characters_all[i].web = life_beast.web.new_randomize_deep_copy()

    @staticmethod
    def wayOfLife_copy_neuro_from_best_to_all():
        life_beast = 0
        for i in range(1, len(Character_beast.characters_all)):
            if Character_beast.characters_all[i].fitnes > Character_beast.characters_all[life_beast].fitnes:
                life_beast = i

        web = Character_beast.characters_all[life_beast].web.new_randomize_deep_copy(size = 0)

        for i in range(len(Character_beast.characters_all)):
            Character_beast.characters_all[i].web = web.new_randomize_deep_copy()

    @staticmethod
    def wayOfLife_simple_crossover():
        Character_beast._make_parents_roulette_not_unique()
        Character_beast._make_who_not_die()
        Character_beast._make_new_population()
        Character_beast._make_mutation()