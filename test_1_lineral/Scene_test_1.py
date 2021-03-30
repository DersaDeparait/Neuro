import config
from Scene import Scene
from test_1_lineral.Character_test import Character_test
from test_1_lineral.Person import Person
from web import Web

class Scene_test(Scene):
    alive = []
    def __init__(self):
        super().__init__()

    def init_battlefield(self):
        super(Scene_test, self).init_battlefield()
    def init_character(self):
        super(Scene_test, self).init_character()
        self.ball_number_of_parts = config.START_POPULATION
        self.ball_position_default = config.CAR_BALL_POSITION_DEFAULT

        self.character = []
        for i in range(self.ball_number_of_parts):
            self.character.append(Character_test(Person(), Web([1])))
        self.number_of_life = 0

    '''
    def rule(self):
        for i in range(len(self.character)):
            self.character[i].calculate_move(self.lazer_of_death, self.ceiling, self.floor, self.enemies)
    def update(self):
        self.__update_beast()
        self.__update_display()
    def __update_beast(self):
        for i in range(len(self.character)):
            self.character[i].update(self.camera_move, self.lazer_of_death, self.enemies)
        self.number_of_life = Character_beast.how_many_alive()
    def __update_display(self):
        pygame.display.set_caption("Жив:{0:4}/{1}, Ітер:{2:5} Еп:{3:5} | Alive:"#// Фітнес результат -1: {3:5.2f} "#  -2: {4:5.2f}, {5}, {6}"
                                   .format(self.number_of_life,
                                           config.START_POPULATION,
                                           self.iteration,
                                           self.epoch,
                                           # self.character[999].person.update_fitnes_walls(lazer_of_death=self.lazer_of_death)
                                           )
                                   + str(Scene_car_test.alive))

    
    def exit_iteration(self):
        super().exit_iteration()
        self.number_of_life = Character_beast.how_many_alive()
        if self.number_of_life < 1:
            self.run_iteration = False


    def evolution_operation(self):
        for i in range(len(self.enemies)):
            self.enemies[i].update(self.camera_move)
            if self.enemies[i].position[0] + self.enemies[i].size < 1500:
                self.enemies[i].position = [2000 + i * 300 + random.randrange(0, 500) + self.camera_move[0], random.randrange(self.floor, self.ceiling)]
                self.enemies[i].size = random.randint(20, 150)

        for i in range(len(self.character)):
            self.character[i].epoch_done()

        Scene_car_test.alive.append(Character_beast.how_many_alive())
        if len(Scene_car_test.alive) > 20: Scene_car_test.alive.pop(0)

        Character_beast.calculate_end_epoch_custom()
    '''

    def _draw_all(self):
        self.draw_characters()
    def draw_characters(self):
        for i in range(len(self.character)):
            if i % 1==0:
                self.character[i].draw(self.display)
