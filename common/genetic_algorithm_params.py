class Genetic_algorithm_params:
    def __init__(self) -> None:
        self.max_counter = 1000  # Кількість циклів в 1 еопосі
        self.max_epoch = 1000  # Кількість епох
        self.start_population = 10  # Кількість осіб взагалі

        self.count_of_alive_after_epoch = self.start_population * 0.5  # Кількість виживших пісял того як закінчився минулий раунд
        self.mutation_power = 0.01  # Ймовірність мутації гена межі [0 до 1]
        self.crossover_point_number = 2  # Кількість точко кросовера, зазвичай 1, можна до 10
        self.number_of_parents_couples = self.start_population # кількість осіб які будуть давати потомків
        self.web_layers = [6, 4]  # [6+9, 6, 4]#[6+3*3,4]#[6,4]#[6,6,4]

    def get_max_epoch(self): return self.max_epoch