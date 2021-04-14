import random
import math

def sigmoida(x): return 1 / (1 + math.e**(-x))
def tanh(x): return math.tanh(x)
def tanh_div2(x): return math.tanh(x/2)
def tanh_div4(x): return math.tanh(x/4)

class Neuron:
    counter = 0
    def __init__(self, fathers: list =[], bias_weigh: int=0, activation_funk=tanh, randomize_power=None):
        if randomize_power == None:
            self.fathers_relation = [Relation(fathers[i], weigh=0) for i in range(len(fathers))]
        else:
            self.fathers_relation = [Relation(fathers[i], weigh=random.uniform(-abs(randomize_power), abs(randomize_power)))
                                     for i in range(len(fathers))]
        self.bias_weigh = bias_weigh if randomize_power == None else (bias_weigh + random.uniform(-abs(randomize_power), abs(randomize_power)))
        self.result = 0
        self.activation_funk = activation_funk
        self.number = Neuron.counter
        Neuron.counter = Neuron.counter + 1

    def copy(self):
        neuron = Neuron(fathers=[], bias_weigh=self.bias_weigh, activation_funk=self.activation_funk)
        for i in range(len(self.fathers_relation)):
            neuron.fathers_relation.append(self.fathers_relation[i].copy())
        return neuron
    def copy_no_weigh(self):
        fathers = [self.fathers_relation[i].get_direction() for i in range(len(self.fathers_relation))]
        neuron = Neuron(fathers=fathers, bias_weigh=self.bias_weigh, activation_funk=self.activation_funk)
        return neuron
    def copy_random_weigh(self, randomize_power=1, randomize_probability=1):
        neuron = Neuron(fathers=[], bias_weigh=self.bias_weigh, activation_funk=self.activation_funk)
        for i in range(len(self.fathers_relation)):
            neuron.fathers_relation.append(self.fathers_relation[i].copy())
        neuron.randomize(randomize_power=randomize_power, randomize_probability=randomize_probability)
        return neuron
    def randomize(self, randomize_power=1, randomize_probability=1):
        if randomize_power < 0:
            randomize_power -= randomize_power
        for i in range(len(self.fathers_relation)):
            if randomize_probability > random.random():
                self.fathers_relation[i].randomize(randomize_power=randomize_power)
        if randomize_probability > random.random():
            self.bias_weigh = self.bias_weigh + random.uniform(-randomize_power, randomize_power)
        return self
    def get_info(self):
        info = "Neuron N {}, fathers:{} ({}), bias: {}, RESULT = {}".format(self.number,
                                                               len(self.fathers_relation),
                                                               [(f.direction.number, f.weigh) for f in self.fathers_relation],
                                                               self.bias_weigh, self.result)
        return info

    def __eq__(self, o: object) -> bool:
        if type(o) == Neuron:
            equality_val = 0.001
            for i in range(len(self.fathers_relation)):
                if abs(self.fathers_relation[i].weigh - o.fathers_relation[i].weigh) > equality_val:
                    return False
            if abs(self.bias_weigh - o.bias_weigh) > equality_val:
                return False
            return True


    def add_father(self, fathers: list=[]):
        for i in range(len(fathers)):
            self.fathers_relation.append(Relation(fathers[i], 0))
    def get_count_of_axon(self):
        return len(self.fathers_relation) + 1

    def get_result(self): return self.result
    def set_result(self, value):self.result = value

    def get_bias(self): return self.bias_weigh
    def get_weigh(self):
        weigh = []
        for i in range(len(self.fathers_relation)):
            weigh.append(self.fathers_relation[i].get_weigh())
        return weigh
    def get_all_weigh(self):
        all_weigh = self.get_weigh()
        all_weigh.append(self.get_bias())
        return all_weigh

    def set_weigh(self, weigh):
        for i in range(len(self.fathers_relation)):
            self.fathers_relation[i].set_weigh(weigh[i])
    def set_bias(self, bias_weigh): self.bias_weigh = bias_weigh
    def set_all_weigh(self, all_weigh: list):
        self.set_bias(all_weigh.pop())
        self.set_weigh(all_weigh)




    def calculate_result(self):
        suma = self.sumator()
        return self.activation(suma)
    def sumator(self):
        suma = self.bias_weigh
        for i in range(len(self.fathers_relation)):
            suma += self.fathers_relation[i].get_multiply()
        return suma
    def activation(self, number):
        self.result = self.activation_funk(number)
        return self.result

class Relation:
    def __init__(self, direction: Neuron, weigh=0):
        self.direction = direction
        self.weigh = weigh

    def get_multiply(self): return self.weigh * self.direction.get_result()
    def get_direction(self): return self.direction
    def get_weigh(self): return self.weigh
    def set_direction(self, direction): self.direction = direction
    def set_weigh(self, weigh): self.weigh = weigh

    def copy(self): return Relation(self.direction, self.weigh)
    def copy_no_weigh(self, weigh=0): return Relation(self.direction, weigh=weigh)
    def randomize(self, randomize_power): self.weigh = self.weigh + random.uniform(-randomize_power, randomize_power)
