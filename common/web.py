from common.neuron import Neuron
import random

class Web:
    counter = 0
    def __init__(self, layers: list=[2, 3, 2], web=None, randomize_power: float =None):
        if type(web) == Web: self.layers = list(web.layers)
        else: self.layers = layers or [1]
        self.neurons = [[]]
        for j in range(self.layers[0]):
            self.neurons[0].append(Neuron())
        for i in range(1, len(self.layers)):
            self.neurons.append([])
            for j in range(self.layers[i]):
                self.neurons[i].append(Neuron(fathers=self.neurons[i - 1], randomize_power=randomize_power))
        if type(web) == Web: self.set_weigh_from_else_web(web=web)
        self.number = Web.counter
        Web.counter += 1

    def print_all_info(self):
        print("-------------------------------------------------------------------------------------")
        print(self, "number : {}/{} architect {}".format(self.number, Web.counter, self.layers))
        for i in range(len(self.neurons)):
            print()
            for j in range(len(self.neurons[i])):
                print("Neuron L{},P{}, {}".format(i, j, self.neurons[i][j].get_info()))
    def print_neuro_chain(self):
        print("number : {}/{} architect {}  ".format(self.number, Web.counter, self.layers), end=" ")
        for i in range(len(self.neurons)):
            for j in range(len(self.neurons[i])):
                print(self.neurons[i][j].get_all_weigh(), end=" ")
            print(end=" | ")
        print()


    def calculate_all(self, input):
        self._set_input(input)
        self._calculate()
        return self._get_output()
    def _set_input(self, input):
        for i in range(len(self.neurons[0])):
            self.neurons[0][i].set_result(input[i])
    def _calculate(self):
        for i in range(1, len(self.neurons)):
            for j in range(len(self.neurons[i])):
                self.neurons[i][j].calculate_result()
    def _get_output(self):
        return [self.neurons[-1][i].get_result() for i in range(len(self.neurons[-1]))]


    def __eq__(self, o: object) -> bool:
        if type(o) == Web:
            if len(self.layers) != len(o.layers):
                return False

            for i in range(len(self.layers)):
                if self.layers[i] != o.layers[i]:
                    return False

            for i in range(len(self.neurons)):
                for j in range(len(self.neurons[i])):
                    if self.neurons[i][j] != o.neurons[i][j]:
                        return False
            return True
    def randomize(self, randomize_power=0.01):
        for i in range(len(self.neurons)):
            for j in range(len(self.neurons[i])):
                self.neurons[i][j].randomize(randomize_power)
    def make_mutation(self, randomize_probability = 0.01, randomize_power = 1.):
        for i in range(len(self.neurons)):
            for j in range(len(self.neurons[i])):
                self.neurons[i][j].randomize(randomize_power=randomize_power, randomize_probability=randomize_probability)
    def new_randomize_deep_copy(self, randomize_power = 0.1):
        return Web(self.layers, web=self, randomize_power=randomize_power)
    def set_weigh_from_else_web(self, web):
        if type(web) == Web:
            if len(self.layers) != len(web.layers):
                return
            for i in range(len(self.layers)):
                if self.layers[i] != web.layers[i]:
                    return

            for i in range(len(self.neurons)):
                for j in range(len(self.neurons[i])):
                    self.neurons[i][j].set_weigh(web.neurons[i][j].get_weigh())
                    self.neurons[i][j].set_bias(web.neurons[i][j].get_bias())
    def set_weigh(self, weigh=[[[1,1],[2,2]],[[3,3],[4,4]]], bias = [[1,2],[3,4]]):
        if type(weigh) == list:
            if len(self.layers) != len(weigh):
                return
            for i in range(len(self.layers)):
                if self.layers[i] != len(weigh[i]):
                    print(i)
                    return

            for i in range(len(self.neurons)):
                for j in range(len(self.neurons[i])):
                    self.neurons[i][j].set_weigh(weigh[i][j])
                    self.neurons[i][j].set_bias(bias[i][j])


    def cross_crossover_several(self, neuro_1, point_number: int = 2, return_couple=False):
        if point_number < 1: point_number = 1

        new_neuro_1 = Web(web=self)
        new_neuro_2 = Web(web=neuro_1)
        sum = 0
        for i in range(len(new_neuro_1.neurons)):
            for j in range(len(new_neuro_1.neurons[i])):
                sum += new_neuro_1.neurons[i][j].get_count_of_axon()
        if point_number >= sum: point_number = sum

        possible_points = [i for i in range(sum)]
        points = []
        for i in range(point_number):
            number = random.choice(possible_points)
            points.append(number)
            possible_points.remove(number)
        points.sort()

        start_parent = random.choice([False, True])

        counter = 0
        for i in range(len(new_neuro_1.neurons)):
            for j in range(len(new_neuro_1.neurons[i])):
                neuro_part_1 = new_neuro_1.neurons[i][j].get_all_weigh()
                neuro_part_2 = new_neuro_2.neurons[i][j].get_all_weigh()
                for k in range(len(neuro_part_1)):
                    if len(points) > 0 and counter > points[0]:
                        start_parent = not start_parent
                        points.pop(0)
                    if start_parent:
                        neuro_part_1[k], neuro_part_2[k] = neuro_part_2[k], neuro_part_1[k]
                    counter += 1
                new_neuro_1.neurons[i][j].set_all_weigh(neuro_part_1)
                new_neuro_2.neurons[i][j].set_all_weigh(neuro_part_2)
        return [new_neuro_1, new_neuro_2] if return_couple else [new_neuro_1]
    def cross_randomize(self, neuro_1):
        new_neuro = Web(web=self)
        for i in range(len(new_neuro.neurons)):
            for j in range(len(new_neuro.neurons[i])):
                if random.random() < 0.5:
                    new_neuro.neurons[i][j].set_all_weigh(neuro_1.neurons[i][j].get_all_weigh())
                else:
                    new_neuro.neurons[i][j].set_all_weigh(self.neurons[i][j].get_all_weigh())
        return new_neuro


    def axon_line(self, number): pass # fixme add for save data to file
