import pygame
import random
import config
from Scene import Scene
from cars.Beast import Beast
from cars.Lazer_of_death import Lazer_of_death
from cars.character_beast import Character_beast

class Scene_car(Scene):
    alive = []
    def __init__(self):
        super().__init__()

    def init_battlefield(self):
        super(Scene_car, self).init_battlefield()
        self.camera_move = config.CAR_CAMERA_MOVE_SPEED
        self.floor = config.CAR_FLOOR_POSITION
        self.ceiling = config.CAR_CEILING_POSITION

        self.lazer_of_death = [Lazer_of_death(config.CAR_LAZER_OF_DEATH_POSITION), Lazer_of_death(self.display_size[0] - config.CAR_LAZER_OF_DEATH_POSITION_REVERSE)]

        self.enemies_number = config.CAR_ENEMIES_NUMBER
        self.enemies = []
        for i in range(self.enemies_number):
            self.enemies.append(
                Beast(position=[1000 + i * 300 + random.randrange(0, 500), random.randrange(self.floor, self.ceiling)],
                      size=random.randrange(50, 200), only_circle=True,
                      color=[random.randrange(1,100), random.randrange(100, 255), random.randrange(255)]))
    def init_character(self):
        super(Scene_car, self).init_character()
        self.ball_number_of_parts = config.START_POPULATION
        self.ball_position_default = config.CAR_BALL_POSITION_DEFAULT

        self.character = []
        for i in range(self.ball_number_of_parts):
            self.character.append(Character_beast(person= Beast([self.ball_position_default[0],
                                                                 self.ball_position_default[1]],
                                                                self.floor,
                                                                self.ceiling,
                                                                )))
        self.number_of_life = 0


    def rule(self):
        for i in range(len(self.character)):
            self.character[i].calculate_move(self.lazer_of_death, self.ceiling, self.floor, self.enemies)
    def update(self):
        self.__update_enemies()
        self.__update_lazer_of_death()
        self.__update_beast()
        self.__update_display()
    def __update_enemies(self):
        for i in range(len(self.enemies)):
            self.enemies[i].update(self.camera_move)
            if self.enemies[i].position[0] + self.enemies[i].size < 0:
                self.enemies[i].position = [2000 + i * 300 + random.randrange(0, 500) + self.camera_move[0], random.randrange(self.floor, self.ceiling)]
                self.enemies[i].size = random.randint(20, 150)
                self.enemies[i].color=[random.randrange(128,256), random.randrange(0, 155), random.randrange(0, 125)]
                # self.enemies[i].color=[random.randrange(1,100), random.randrange(100, 255), random.randrange(255)]
    def __update_lazer_of_death(self):
        for i in range(len(self.lazer_of_death)):
            self.lazer_of_death[i].update()
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
                                   + str(Scene_car.alive))


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

        Scene_car.alive.append(Character_beast.how_many_alive())
        if len(Scene_car.alive) > 20: Scene_car.alive.pop(0)

        Character_beast.calculate_end_epoch_custom()




    def _draw_all(self):
        self.draw_enemies()
        self.draw_characters()
        self.draw_frame()
        self.draw_lazer_of_death()
    def draw_enemies(self):
        for i in range(len(self.enemies)):
            self.enemies[i].draw(self.display)
    def draw_characters(self):
        for i in range(len(self.character)):
            if i % 1==0:
                self.character[i].draw(self.display)
    def draw_frame(self, frame_size = 4, color = [255, 0, 255]):
        pygame.draw.line(self.display, color, [-1000 - self.camera_move[0], self.floor - self.camera_move[1]], [self.display_size[0] * 1000 - self.camera_move[0], self.floor - self.camera_move[1]], frame_size)
        pygame.draw.line(self.display, color, [-1000 - self.camera_move[0], self.ceiling - self.camera_move[1]], [self.display_size[0] * 1000 - self.camera_move[0], self.ceiling - self.camera_move[1]], frame_size)
    def draw_lazer_of_death(self):
        for i in range(len(self.lazer_of_death)):
            self.lazer_of_death[i].draw(self.display)