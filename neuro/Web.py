import random

class Web:
    def __init__(self, layers = [4, 4], web = None):
        self.activation_function = lambda number: number
        if web != None:
            self.neurons = [[web.neurons[i][j] for j in range(layers[i])] for i in range(len(layers))]
            self.axon_weigh = [[web.axon_weigh[i][j] for j in range(layers[i] * layers[i + 1])] for i in range(len(layers) - 1)]
        else:
            self.neurons = [[0 for j in range(layers[i])] for i in range(len(layers))]
            self.axon_weigh = [[0 for j in range(layers[i] * layers[i + 1])] for i in range(len(layers) - 1)]

    def randomize(self, size = 0.01):
        for i in range(len(self.axon_weigh)):
            for j in range(len(self.axon_weigh[i])):
                self.axon_weigh[i][j] += random.uniform(-size, size)

    def set_function(self, activation_function):
        self.activation_function = activation_function

    def calculate_all(self, input):
        self.set_input(input)
        self.calculate()
        return self.get_output()
    def set_input(self, input):
        for i in range(len(self.neurons[0])):
            self.neurons[0][i] = input[i]
    def get_output(self):
        return self.neurons[-1]
    def calculate(self):
        for i in range(1, len(self.neurons)):
            for j in range(len(self.neurons[i])):
                sum = 0
                for k in range(len(self.neurons[i - 1])):
                    sum += self.axon_weigh[i - 1][k * len(self.neurons[i]) + j] * self.neurons[i - 1][k]
                self.neurons[i][j] = self.activation_function(sum)