from common.geneticAlgorithmParams import GeneticAlgorithmParams


class GeneticAlgorithmParamsTest(GeneticAlgorithmParams):
    # list_start_population = [16, 64, 256, 1024, 4096]
    #
    # list_count_elitism = [0, 0.001, 0.01, 0.1, 0.2]
    # list_count_of_alive_after_epoch = [0.03125, 0.0625, 0.125, 0.25, 0.5]
    # list_random_kid = [0, 0.001, 0.01, 0.1, 0.2]
    #
    # list_mutation_probability = [0, 0.0001, 0.001, 0.01, 0.1]
    #
    # list_type_selection = ["roulette", "tournament", "rank", "proportional"]
    # list_type_make_new_population = ["cross 1", "cross 2", "cross 3", "cross 4", "random", "lineral", "one father"]
    # list_type_breeding = ["simple", "outbreeding genotype", "outbreeding phenotype", "inbreeding genotype", "inbreeding phenotype", "adaptive+1 breeding type gen", "not family breeding"]

    list_dimension = [1, 2, 4, 6]
    list_with_goal_changing = [0, 1]
    list_with_spin = [0, 1]
    list_out_data_for_one_dimension = [1, 2, 3]

    list_fitness_way_distance = [0, 1] # fitness_distance += 1/(1+x)
    list_fitness_way_side = [0, 1] # fitness_side_x or y += 1
    list_fitness_way_vector = [0, 1] # fitness_vector to goal += from -1 to 1
    list_fitness_way_kill_all_unwanted = [0, 1] # fitness_vector_speed += from -1 to 1   speed_absolute/dis_absolute     (if speed_absolute>dis_absolute 0)

    def __init__(self) -> None:
        super(GeneticAlgorithmParamsTest, self).__init__()

        self._max_iteration = 1000  # Кількість циклів в 1 еопосі
        self._max_epoch = 1000  # Кількість епох

        self._start_population = 1000#GeneticAlgorithmParams.list_start_population[3]  # Кількість осіб взагалі
        self._count_elitism = GeneticAlgorithmParams.list_count_elitism[0]
        self._count_of_alive_after_epoch = int(self._start_population * GeneticAlgorithmParams.list_count_of_alive_after_epoch[4])  # Кількість виживших пісял того як закінчився минулий раунд
        self._random_kid = GeneticAlgorithmParams.list_random_kid[0]

        self._mutation_probability = GeneticAlgorithmParams.list_mutation_probability[2] # Ймовірність мутації гена межі [0 до 1]
        self._type_selection = GeneticAlgorithmParams.list_type_selection[0]
        self._type_make_new_population = GeneticAlgorithmParams.list_type_make_new_population[1]
        self._type_breeding = GeneticAlgorithmParams.list_type_breeding[0]

        self._dimension = GeneticAlgorithmParamsTest.list_dimension[1]
        self._with_goal_changing = GeneticAlgorithmParamsTest.list_with_goal_changing[0]
        self._with_spin = GeneticAlgorithmParamsTest.list_with_spin[0]
        self._out_data_for_one_dimension = GeneticAlgorithmParamsTest.list_out_data_for_one_dimension[0]

        self._fitness_way_distance = GeneticAlgorithmParamsTest.list_fitness_way_distance[1]
        self._fitness_way_side = GeneticAlgorithmParamsTest.list_fitness_way_side[1]
        self._fitness_way_vector = GeneticAlgorithmParamsTest.list_fitness_way_vector[1]
        self._fitness_way_kill_all_unwanted = GeneticAlgorithmParamsTest.list_fitness_way_kill_all_unwanted[1]

        self._web_layers = [self._dimension, self._dimension * self._out_data_for_one_dimension]

    def get_dimension(self): return self._dimension
    def get_with_goal_changing(self): return self._with_goal_changing
    def get_with_spin(self): return self._with_spin
    def get_out_data_for_one_dimension(self): return self._out_data_for_one_dimension

    def get_fitness_way_distance(self): return self._fitness_way_distance
    def get_fitness_way_side(self): return self._fitness_way_side
    def get_fitness_way_vector(self): return self._fitness_way_vector
    def get_fitness_way_kill_all_unwanted(self): return self._fitness_way_kill_all_unwanted
