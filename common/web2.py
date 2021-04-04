import random
import copy

class Web:
    def __init__(self, layers = [2,2], web = None, randomize = None):
        self.layers = layers
        self.activation_function = lambda number: number
        if web != None:
            self.layers = copy.deepcopy(web.layers)
            self.neurons = [[web.neurons[i][j] for j in range(self.layers[i])] for i in range(len(self.layers))]
            self.axon_weigh = [[web.axon_weigh[i][j] for j in range(self.layers[i] * self.layers[i + 1])] for i in range(len(self.layers) - 1)]
            self.axon_bias = copy.deepcopy(web.axon_bias)
        else:
            self.neurons = [[0 for j in range(self.layers[i])] for i in range(len(self.layers))]
            self.axon_weigh = [[0 for j in range(self.layers[i] * self.layers[i + 1])] for i in range(len(self.layers) - 1)]
            self.axon_bias = [[0]*self.layers[i+1] for i in range(len(self.layers) - 1)]
        if randomize != None: self.randomize(randomize)

    def __eq__(self, o: object) -> bool:
        if type(o) == Web:
            for i in range(len(self.axon_weigh)):
                for j in range(len(self.axon_weigh[i])):
                    if abs(self.axon_weigh[i][j] - o.axon_weigh[i][j]) > 0.001:
                        return False
            for i in range(len(self.axon_bias)):
                for j in range(len(self.axon_bias[i])):
                    if abs(self.axon_bias[i][j] - o.axon_bias[i][j]) > 0.001:
                        return False
            return True


    def randomize(self, size = 0.01):
        for i in range(len(self.axon_weigh)):
            for j in range(len(self.axon_weigh[i])):
                self.axon_weigh[i][j] += random.uniform(-size, size)
        for i in range(len(self.axon_bias)):
            for j in range(len(self.axon_bias[i])):
                self.axon_bias[i][j] += random.uniform(-size, size)
    def make_mutation(self, percent = 0.01, power = 1.):
        dispers = 0
        counter = 0
        for i in range(len(self.axon_weigh)):
            for j in range(len(self.axon_weigh[i])):
                dispers += self.axon_weigh[i][j]
                counter += 1
        for i in range(len(self.axon_bias)):
            for j in range(len(self.axon_bias[i])):
                dispers += self.axon_bias[i][j]
                counter += 1
        dispers = dispers / counter + 0.1
        for i in range(len(self.axon_weigh)):
            for j in range(len(self.axon_weigh[i])):
                if random.random() < percent:
                    self.axon_weigh[i][j] += random.uniform(-dispers * power, dispers * power)
        for i in range(len(self.axon_bias)):
            for j in range(len(self.axon_bias[i])):
                if random.random() < percent:
                    self.axon_bias[i][j] += random.uniform(-dispers * power, dispers * power)
    def new_randomize_deep_copy(self, size = 0.1):
        return Web(self.layers, web = self, randomize= size)
    def new_mutant_deep_copy(self, percent = 0.01, power = 1.):
        web = Web(self.layers, web = self)
        web.make_mutation(percent = percent, power = power)
        return web

    def set_function(self, activation_function):
        self.activation_function = activation_function

    def cross_crossover_one(self, neuro_1):
        new_neuro = Web(web = self)
        count = 0
        for i in range(len(new_neuro.axon_weigh)):
            for j in range(len(new_neuro.axon_weigh[i])):
                count += 1
        for i in range(len(self.axon_bias)):
            for j in range(len(self.axon_bias[i])):
                count += 1

        point = random.randint(0, count - 1)
        counter = 0
        random_val = random.choice([1, -1])
        # if random.random() < 0.5:
        for i in range(len(new_neuro.axon_weigh)):
            for j in range(len(new_neuro.axon_weigh[i])):
                if counter * random_val >= point * random_val:
                    new_neuro.axon_weigh[i][j] = neuro_1.axon_weigh[i][j]
                counter += 1
            for j in range(len(new_neuro.axon_bias[i])):
                if counter * random_val >= point * random_val:
                    new_neuro.axon_bias[i][j] = neuro_1.axon_bias[i][j]
                counter += 1
        # else:
        #     for i in range(len(new_neuro.axon_weigh)):
        #         for j in range(len(new_neuro.axon_weigh[i])):
        #             if counter < point:
        #                 new_neuro.axon_weigh[i][j] = neuro_1.axon_weigh[i][j]
        #             counter += 1
        #         for j in range(len(new_neuro.axon_bias[i])):
        #             if counter < point:
        #                 new_neuro.axon_bias[i][j] = neuro_1.axon_bias[i][j]
        #         counter += 1
        return new_neuro
    def cross_crossover_several(self, neuro_1, point_number : int = 2, return_couple = False):
        if point_number < 1: point_number = 1

        new_neuro = Web(web = self)
        new_neuro_2 = Web(web = neuro_1)
        sum = 0
        for i in range(len(new_neuro.axon_weigh)):
            for j in range(len(new_neuro.axon_weigh[i])):
                sum += 1
            sum += 1
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
        for i in range(len(new_neuro.axon_weigh)):
            for j in range(len(new_neuro.axon_weigh[i])):
                if len(points) > 0 and counter > points[0]:
                    start_parent = not start_parent
                    points.pop(0)
                if start_parent:
                    new_neuro_2.axon_weigh[i][j] = self.axon_weigh[i][j]
                    new_neuro.axon_weigh[i][j] = neuro_1.axon_weigh[i][j]
                counter += 1
            if len(points) > 0 and counter > points[0]:
                start_parent = not start_parent
                points.pop(0)
            if start_parent:
                new_neuro_2.axon_bias[i] = self.axon_bias[i]
                new_neuro.axon_bias[i] = neuro_1.axon_bias[i]
            counter += 1
        return [new_neuro, new_neuro_2] if return_couple else [new_neuro]
    def cross_crossover_multi_several(self, neuro, point_number : int = 3, random_sequence:bool = True):
        if point_number < 1: point_number = 1

        new_neuro = Web(web = self)
        sum = 0
        for i in range(len(new_neuro.axon_weigh)):
            for j in range(len(new_neuro.axon_weigh[i])):
                sum += 1
            sum += 1
        if point_number >= sum: point_number = sum

        possible_points = [i for i in range(sum)]
        points = []
        for i in range(point_number):
            number = random.choice(possible_points)
            points.append(number)
            possible_points.remove(number)
        points.sort()

        neuro.insert(0, self)
        if random_sequence: neuro_sequence = random.choices(neuro, k = len(points) + 1)
        else:
            neuro_sequence = random.choice([
                [neuro[i % len(neuro)] for i in range(len(points) + 1)],
                [neuro[len(neuro) - i % len(neuro) - 1] for i in range(len(points) + 1)]
            ])


        counter = 0
        index = 0
        for i in range(len(new_neuro.axon_weigh)):
            for j in range(len(new_neuro.axon_weigh[i])):
                if len(points) > 0 and counter > points[0]:
                    index += 1
                    points.pop(0)
                new_neuro.axon_weigh[i][j] = neuro_sequence[index].axon_weigh[i][j]
                counter += 1
            if len(points) > 0 and counter > points[0]:
                index += 1
                points.pop(0)
            new_neuro.axon_bias[i] = neuro_sequence[index].axon_bias[i]
            counter += 1
        return new_neuro
    def cross_randomize(self, neuro_1):
        new_neuro = Web(web = self)
        for i in range(len(new_neuro.axon_weigh)):
            for j in range(len(new_neuro.axon_weigh[i])):
                if random.random() < 0.5:
                    new_neuro.axon_weigh[i][j] = neuro_1.axon_weigh[i][j]
            if random.random() < 0.5:
                new_neuro.axon_bias[i] = neuro_1.axon_bias[i]
        return new_neuro
    def cross_average(self, neuro_1, k = 1.25):
        new_neuro = Web(web=self)
        for i in range(len(new_neuro.axon_weigh)):
            for j in range(len(new_neuro.axon_weigh[i])):
                min_value = min(new_neuro.axon_weigh[i][j], neuro_1.axon_weigh[i][j])
                max_value = max(new_neuro.axon_weigh[i][j], neuro_1.axon_weigh[i][j])
                dis = abs(new_neuro.axon_weigh[i][j] - neuro_1.axon_weigh[i][j])
                new_neuro.axon_weigh[i][j] = random.uniform(min_value - (k - 1) * dis, max_value + (k - 1) * dis)
            min_value = min(new_neuro.axon_bias[i], neuro_1.axon_bias[i])
            max_value = max(new_neuro.axon_bias[i], neuro_1.axon_bias[i])
            dis = abs(new_neuro.axon_bias[i] - neuro_1.axon_bias[i])
            new_neuro.axon_bias[i] = random.uniform(min_value - (k - 1) * dis, max_value + (k - 1) * dis)
        return new_neuro
    def cross_lineral(self, neuro_1, ratio = None):
        if ratio == None: ratio = random.random()
        new_neuro = Web(web=self)
        for i in range(len(new_neuro.axon_weigh)):
            for j in range(len(new_neuro.axon_weigh[i])):
                new_neuro.axon_weigh[i][j] = new_neuro.axon_weigh[i][j] + ratio * (neuro_1.axon_weigh[i][j] - new_neuro.axon_weigh[i][j])
            new_neuro.axon_bias[i] = new_neuro.axon_bias[i] + ratio * (neuro_1.axon_bias[i] - new_neuro.axon_bias[i])
        return new_neuro

    def axon_line(self, number):
        to_return = {}
        flat_list = self.__flat_list(self.axon_weigh)
        for i in range(len(flat_list)):
            to_return["n{}-a{}".format(number, i)] = [flat_list[i]]
        return to_return
    def __flat_list(self, value, new_list=[]):
        for i in value:
            if type(i) == int or type(i) == float:
                new_list.append(i)
            else:
                self.__flat_list(i)
        return new_list

    def calculate_all(self, input):
        self._set_input(input)
        self._calculate()
        return self._get_output()
    def _set_input(self, input):
        for i in range(len(self.neurons[0])):
            self.neurons[0][i] = input[i]
    def _calculate(self):
        for i in range(1, len(self.neurons)):
            for j in range(len(self.neurons[i])):
                sum = 0
                for k in range(len(self.neurons[i - 1])):
                    sum += self.axon_weigh[i - 1][k * len(self.neurons[i]) + j] * self.neurons[i - 1][k]
                sum = sum + self.axon_bias[i - 1]
                self.neurons[i][j] = self.activation_function(sum)
    def _get_output(self):
        return self.neurons[-1]




w = [Web([2, 2, 1, 3]) for i in range(2)]
w[1].axon_weigh = [[1, 1, 1, 1], [1, 1],  [1, 1, 1, 1, 1, 1]]
w[1].axon_bias = [[1, 1], [1], [1, 1, 1]]
for i in range(1000):
    w.append(w[0].cross_crossover_one(w[1]))

w[1].axon_weigh[0] = [2, 2, 2, 2]
w[1].axon_weigh[1] = [3, 3, 3, 3, 3, 3]
w[1].axon_bias[0] = [4, 4]
w[1].axon_bias[1] = [5, 5, 5]

# for i in range(len(w)):
#     print(i, w[i].axon_weigh[0], w[i].axon_bias[0], w[i].axon_weigh[1], w[i].axon_bias[1], w[i].axon_weigh[2], w[i].axon_bias[2])



# print(w2.axon_weigh, w2.axon_bias)
# print(w==w2)

for i in range(-220,200):
    print(6*i%7,2*i%7,3*i%7,1*i%7)