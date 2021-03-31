from common.geneticAlgorithmParams import GeneticAlgorithmParams


class GeneticAlgorithmParamsTest(GeneticAlgorithmParams):
    def __init__(self) -> None:
        super(GeneticAlgorithmParamsTest, self).__init__()
        self.max_iteration = 1000  # Кількість циклів в 1 еопосі
        self.max_epoch = 1000  # Кількість епох
        self.start_population = 100  # Кількість осіб взагалі

        self.count_of_alive_after_epoch = self.start_population * 0.5  # Кількість виживших пісял того як закінчився минулий раунд
        self.mutation_power = 0.01  # Ймовірність мутації гена межі [0 до 1]
        self.crossover_point_number = 2  # Кількість точко кросовера, зазвичай 1, можна до 10
        self.number_of_parents_couples = self.start_population # кількість осіб які будуть давати потомків
        self.web_layers = [6, 4]  # [6+9, 6, 4]#[6+3*3,4]#[6,4]#[6,6,4]

    def get_max_epoch(self): return self.max_epoch
    def get_max_iteration(self): return self.max_iteration
    def get_start_population(self): return self.start_population
    def get_count_of_alive_after_epoch(self): return self.count_of_alive_after_epoch
    def get_mutation_power(self): return self.mutation_power
    def get_crossover_point_number(self): return self.crossover_point_number
    def get_number_of_parents_couples(self): return self.number_of_parents_couples
    def get_web_layers(self): return self.web_layers
