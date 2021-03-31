import datetime
from common.genetic_algorithm_params import Genetic_algorithm_params
from common.data_writer import Data_writer
from common.monitor import Monitor

class Activity:
    def __init__(self, monitor: Monitor = None,
                 genetic_algorithm_params: Genetic_algorithm_params = None,
                 data_writer: Data_writer = None):
        self._init(monitor, genetic_algorithm_params, data_writer)

    def _init(self, monitor: Monitor = None,
              genetic_algorithm_params: Genetic_algorithm_params = None,
              data_writer: Data_writer = None):
        self.__system_init(monitor)
        self.__simulation_params_init(genetic_algorithm_params)
        self.__character_init()
        self.__enemy_init()
        self.__environment_init()
        self.__data_writer_init(data_writer)

    def __system_init(self, monitor: Monitor = None) -> None:
        self.monitor = monitor or Monitor()

    def __simulation_params_init(self, genetic_algorithm_params: Genetic_algorithm_params = None) -> None:
        self.epoch = 0
        self.iteration = 0
        self.is_epoch_work: bool = True
        self.is_iteration_work: bool = True
        self.start_time = datetime.datetime.now()

        self.genetic_algorithm_params = genetic_algorithm_params or Genetic_algorithm_params()

    def __character_init(self) -> None: pass
    def __enemy_init(self) -> None: pass
    def __environment_init(self) -> None: pass

    def __data_writer_init(self, data_writer: Data_writer = None) -> None:
        self.data_writer = data_writer or Data_writer()



    def loop(self) -> None:
        while self.is_epoch_work:
            self._run_iteration_cycle()
            self._calculate_fitness_function()
            self._save_character_data()
            self._create_new_population()
            self._check_loop_epoch_condition()

    def _save_character_data(self) -> None: pass

    def _run_iteration_cycle(self) -> None:
        while self.is_iteration_work:
            self.__control_input()

            self.__move_environment()
            self.__collide_environment()

            self.__move_enemies()
            self.__collide_enemies()
            self.__kill_enemies()

            self.__move_character()
            self.__collide_character()
            self.__kill_character()
            self.__calculate_fitness_function()

            self.__draw_all()
            self.__write_data_on_screen()
            self.__check_loop_iteration_condition()


    def __control_input(self): self.monitor.control_input()
    def __move_environment(self): pass
    def __collide_environment(self): pass
    def __move_enemies(self): pass
    def __collide_enemies(self): pass
    def __kill_enemies(self): pass
    def __move_character(self): pass
    def __collide_character(self): pass
    def __kill_character(self): pass
    def __calculate_fitness_function(self): pass
    def __draw_all(self): self.monitor.draw(environment=[], enemies=[], character=[])
    def __write_data_on_screen(self):
        self.monitor.write_data_on_screen("Test e:{}, i:{}".format(self.epoch, self.iteration))
    def __check_loop_iteration_condition(self):
        self.iteration += 1
        if self.iteration >= self.genetic_algorithm_params.get_max_iteration():
            self.is_iteration_work = False


    def _calculate_fitness_function(self) -> None: pass

    def _create_new_population(self) -> None: pass

    def _check_loop_epoch_condition(self) -> None:
        self.__count_epoch()
        self.__check_stop_epoch_condition()

    def __count_epoch(self) -> None:
        self.epoch += 1

    def __check_stop_epoch_condition(self) -> None:
        if self.epoch >= self.genetic_algorithm_params.get_max_epoch():
            self.is_epoch_work = False
        else:
            self.is_iteration_work = True
            self.iteration = 0
