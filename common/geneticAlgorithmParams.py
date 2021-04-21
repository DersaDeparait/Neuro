class GeneticAlgorithmParams:
    list_start_population = [16, 64, 256, 1024, 4096]

    list_count_elitism = [0, 0.001, 0.01, 0.1, 0.2]
    list_count_of_alive_after_epoch = [0.03125, 0.0625, 0.125, 0.25, 0.5]
    list_random_kid = [0, 0.001, 0.01, 0.1, 0.2]

    list_mutation_probability = [0, 0.0001, 0.001, 0.01, 0.1]

    list_type_selection = ["roulette", "tournament", "rank", "proportional"]
    list_type_make_new_population = ["cross 1", "cross 2", "cross 3", "cross 4", "random", "lineral", "one father"]
    list_type_breeding = ["simple", "outbreeding genotype", "outbreeding phenotype", "inbreeding genotype", "inbreeding phenotype", "adaptive+1 breeding type gen", "not family breeding"]



    def __init__(self) -> None:
        self._max_iteration = 1000  # Кількість циклів в 1 еопосі
        self._max_epoch = 1000  # Кількість епох

        self._start_population = GeneticAlgorithmParams.list_start_population[4]  # Кількість осіб взагалі
        self._count_elitism = GeneticAlgorithmParams.list_count_elitism[0]
        self._count_of_alive_after_epoch = int(self._start_population * GeneticAlgorithmParams.list_count_of_alive_after_epoch[4])  # Кількість виживших пісял того як закінчився минулий раунд
        self._random_kid = GeneticAlgorithmParams.list_random_kid[0]

        self._mutation_probability = GeneticAlgorithmParams.list_mutation_probability[1] # Ймовірність мутації гена межі [0 до 1]
        self._type_selection = GeneticAlgorithmParams.list_type_selection[0]
        self._type_make_new_population = GeneticAlgorithmParams.list_type_make_new_population[1]
        self._type_breeding = GeneticAlgorithmParams.list_type_breeding[0]

        self._count_web_layers()

    def _count_web_layers(self):
        self._web_layers = [6, 4]  # [6+9, 6, 4]#[6+3*3,4]#[6,4]#[6,6,4]

    def get_max_epoch(self): return self._max_epoch
    def get_max_iteration(self): return self._max_iteration
    def get_start_population(self): return self._start_population
    def get_count_elitism(self): return self._count_elitism
    def get_count_of_alive_after_epoch(self): return self._count_of_alive_after_epoch
    def get_random_kid(self): return self._random_kid

    def get_mutation_probability(self): return self._mutation_probability
    def get_type_selection(self): return self._type_selection
    def get_type_make_new_population(self): return self._type_make_new_population
    def get_type_breading(self): return self._type_breeding

    def get_crossover_point_number(self):
        if self._type_make_new_population == 0: return 1
        elif self._type_make_new_population == 1: return 2
        elif self._type_make_new_population == 2: return 3
        elif self._type_make_new_population == 3: return 4
        else: return 0
    def get_web_layers(self): return self._web_layers
