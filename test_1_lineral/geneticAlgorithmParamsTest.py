from common.geneticAlgorithmParams import GeneticAlgorithmParams


class GeneticAlgorithmParamsTest(GeneticAlgorithmParams):
    # list_start_population = [16, 64, 256, 1024, 4096]
    # list_count_of_alive_after_epoch = [0.03125, 0.0625, 0.125, 0.25, 0.5]
    # list_mutation_power = [0, 0.0001, 0.001, 0.01, 0.1]
    # list_type_make_new_population = {0: "one father", 1: "cross 1", 2: "cross 2", 3: "cross 4", 4: "lineral"}
    # list_type_breeding = {0: "simple roulette", 1: "outbreeding", 2: "outbreeding", 3: "inbreeding", 4: "inbreeding", 5: "adaptive+1 breeding type gen", 6: "not family breeding"}
    # list_count_elitism = [0, 0.001, 0.01, 0.1, 0.2]
    # list_random_kid = [0, 0.001, 0.01, 0.1, 0.2]
    list_dimension = [1, 2, 4, 6]
    list_with_goal_changing = [0, 1]
    list_with_spin = [0, 1]
    list_out_data_for_one_dimension = [1, 2, 3]
    list_fitness_way_distance = [0, 1] # fitness_distance += 1/(1+x)
    list_fitness_way_side = [0, 1] # fitness_side_x or y += 1
    list_fitness_way_vector = [0, 1] # fitness_vector to goal += from -1 to 1
    list_fitness_way_vector_speed = [0, 1] # fitness_vector_speed += from -1 to 1   speed_absolute/dis_absolute     (if speed_absolute>dis_absolute 0)

    def __init__(self) -> None:
        super(GeneticAlgorithmParamsTest, self).__init__()

        self.start_population = 4000  # Кількість осіб взагалі
        self.count_of_alive_after_epoch = int(self.start_population * 0.3)  # Кількість виживших пісял того як закінчився минулий раунд
        self.mutation_power = 0.02  # Ймовірність мутації гена межі [0 до 1]

        self.crossover_point_number = 2  # Кількість точко кросовера, зазвичай 1, можна до 10
        self.web_layers = [1, 1]  # [6+9, 6, 4]#[6+3*3,4]#[6,4]#[6,6,4]
