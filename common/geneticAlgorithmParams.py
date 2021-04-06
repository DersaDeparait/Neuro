class GeneticAlgorithmParams:
    list_max_iteration = [250, 500, 1000, 2000, 4000]
    list_max_epoch = [125, 250, 500, 1000, 2000]
    list_start_population = [16, 64, 256, 1024, 4096]

    list_count_of_alive_after_epoch = [0.03125, 0.0625, 0.125, 0.25, 0.5]
    list_mutation_power = [0, 0.0001, 0.001, 0.01, 0.1]
    dict_type_make_new_population = {1:"one father", 2:"cross 1", 3:"cross 2", 4:"cross 3", 5:"cross 4", 6:"randomize", 7:"average", 8:"lineral"}


    def __init__(self) -> None:
        self.max_iteration = 1000  # Кількість циклів в 1 еопосі
        self.max_epoch = 1000  # Кількість епох
        self.start_population = 1000  # Кількість осіб взагалі

        self.count_of_alive_after_epoch = int(self.start_population * 0.5)  # Кількість виживших пісял того як закінчився минулий раунд
        self.mutation_probability = 0.01  # Ймовірність мутації гена межі [0 до 1]
        self.crossover_point_number = 2  # Кількість точко кросовера, зазвичай 1, можна до 10
        self.number_of_parents_couples = self.start_population # кількість осіб які будуть давати потомків
        self.web_layers = [6, 4]  # [6+9, 6, 4]#[6+3*3,4]#[6,4]#[6,6,4]

    def get_max_epoch(self): return self.max_epoch
    def get_max_iteration(self): return self.max_iteration
    def get_start_population(self): return self.start_population
    def get_count_of_alive_after_epoch(self): return self.count_of_alive_after_epoch
    def get_mutation_probability(self): return self.mutation_probability
    def get_crossover_point_number(self): return self.crossover_point_number
    def get_number_of_parents_couples(self): return self.number_of_parents_couples
    def get_web_layers(self): return self.web_layers
