from common.activity import Activity
from common.dataWriter import DataWriter
from common.geneticAlgorithmParams import GeneticAlgorithmParams
from common.monitor import Monitor
from common.character import Character

from test_3_lineral_and_spin.personTest import PersonTest
from test_3_lineral_and_spin.characterTest import CharacterTest
from test_3_lineral_and_spin.geneticAlgorithmParamsTest import GeneticAlgorithmParamsTest

import datetime


class ActivityTest(Activity): # test 3 lineral and spin
    def __init__(self, monitor: Monitor = None,
                 genetic_algorithm_params: GeneticAlgorithmParams = None,
                 data_writer: DataWriter = None):
        super(ActivityTest, self).__init__(monitor, genetic_algorithm_params, data_writer)
        self.init(monitor, genetic_algorithm_params, data_writer)

    def init(self, monitor: Monitor = None,
             genetic_algorithm_params: GeneticAlgorithmParams = None,
             data_writer: DataWriter = None):
        self._system_init(monitor)
        self._simulation_params_init(genetic_algorithm_params)
        self._character_init()
        self._enemy_init()
        self._environment_init()
        self._data_writer_init(data_writer)

    def _system_init(self, monitor: Monitor = None) -> None:
        self.monitor = monitor or Monitor()

    def _simulation_params_init(self, genetic_algorithm_params: GeneticAlgorithmParams = None) -> None:
        self.epoch = 0
        self.iteration = 0
        self.is_epoch_work: bool = True
        self.is_iteration_work: bool = True
        self.start_time = datetime.datetime.now()

        self.genetic_algorithm_params = genetic_algorithm_params or GeneticAlgorithmParams()

    def _character_init(self) -> None:
        self.character = []
        for i in range(self.genetic_algorithm_params._start_population):
            self.character.append(Character())

    def _enemy_init(self) -> None: pass

    def _environment_init(self) -> None: pass

    def _data_writer_init(self, data_writer: DataWriter = None) -> None:
        self.data_writer = data_writer or DataWriter()




    def loop(self) -> None:
        while self.is_epoch_work:
            self._run_iteration_cycle()
            self._calculate_fitness_function_epoch()
            self._save_character_data()
            self._create_new_population()
            self._check_loop_epoch_condition()


    def _run_iteration_cycle(self) -> None:
        while self.is_iteration_work:
            self._control_input()

            self._move_environment()
            self._collide_environment()

            self._move_enemies()
            self._collide_enemies()
            self._kill_enemies()

            self._move_character()
            self._collide_character()
            self._kill_character()
            self._calculate_fitness_function_iteration()

            self._draw_all()
            self._write_data_on_screen()
            self._check_loop_iteration_condition()
    def _control_input(self): self.monitor.control_input()
    def _move_environment(self): pass
    def _collide_environment(self): pass
    def _move_enemies(self): pass
    def _collide_enemies(self): pass
    def _kill_enemies(self): pass
    def _move_character(self): pass
    def _collide_character(self): pass
    def _kill_character(self): pass
    def _calculate_fitness_function_iteration(self): pass
    def _draw_all(self): self.monitor.draw(environment=[], enemies=[], character=self.character)
    def _write_data_on_screen(self):
        self.monitor.write_data_on_screen("Test e:{}, i:{}".format(self.epoch, self.iteration))
    def _check_loop_iteration_condition(self):
        self.iteration += 1
        if self.iteration >= self.genetic_algorithm_params.get_max_iteration():
            self.is_iteration_work = False


    def _calculate_fitness_function_epoch(self): pass


    def _save_character_data(self) -> None:pass


    def _create_new_population(self) -> None: pass


    def _check_loop_epoch_condition(self) -> None:
        self._count_epoch()
        self._check_stop_epoch_condition()
    def _count_epoch(self) -> None:
        self.epoch += 1
    def _check_stop_epoch_condition(self) -> None:
        if self.epoch >= self.genetic_algorithm_params.get_max_epoch():
            self.is_epoch_work = False
        else:
            self.is_iteration_work = True
            self.iteration = 0

