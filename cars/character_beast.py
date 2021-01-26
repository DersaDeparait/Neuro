from character import Character
from cars.Beast import Beast
from web import Web
import random

class Character_beast(Character):
    def __init__(self, person = None, web = None):
        super().__init__(person, web)

    def calculate_move(self, lazer_of_death, ceiling, floor):
        lazer_distance = lazer_of_death[1].position - lazer_of_death[0].position
        distance_to_left_lazer_normed = (self.person.position[0] - lazer_of_death[0].position) / lazer_distance
        distance_to_right_lazer_normed = (lazer_of_death[1].position - self.person.position[0]) / lazer_distance
        wall_distance = ceiling - floor
        distance_to_up_wall_normed = (ceiling - self.person.position[1]) / wall_distance
        distance_to_down_wall_normed = (self.person.position[1] - floor) / wall_distance

        self.person.calculate_move(self.web, [distance_to_left_lazer_normed,
                                      distance_to_right_lazer_normed,
                                      distance_to_up_wall_normed,
                                      distance_to_down_wall_normed])
    def update(self, camera_move, lazer_of_death, enemies):
        self.person.possible_to_die_from_frame(lazer_of_death)
        # self.person.possible_to_die_from_enemies(enemies)
        self.person.update_life_time()
        self.fitnes += self.person.update_fitnes_walls(lazer_of_death)
        self.fitnes += self.person.update_fitnes_enemies(enemies)
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




    def set_web(self): super().set_web()
    def iteration_done(self): super().iteration_done()
    def epoch_done(self): super().epoch_done()

    @staticmethod
    def calculate_end_epoch_0(ball_position_default, floor, ceiling):
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
                Character_beast.characters_all[i].person.set_params([ball_position_default[0], ball_position_default[1]], floor, ceiling)

        # super().calculate_end_epoch()