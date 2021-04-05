class Neuron:
    def __init__(self, fathers: list =[], bias_weigh: int=0, activation_funk=lambda x:x):
        self.fathers_relation = [Relation(fathers[i]) for i in range(len(fathers))]
        self.bias_weigh = bias_weigh
        self.result = 0
        self.activation_funk = activation_funk

    def copy(self):
        neuron = Neuron(fathers=[], bias_weigh=self.bias_weigh, activation_funk=self.activation_funk)
        for i in range(len(self.fathers_relation)):
            neuron.fathers_relation.append(self.fathers_relation)
        return neuron
    def copy_no_weigh(self):
        fathers = [self.fathers_relation[i].get_direction() for i in range(len(self.fathers_relation))]
        neuron = Neuron(fathers=fathers, bias_weigh=self.bias_weigh, activation_funk=self.activation_funk)
        return neuron

    def add_father(self, fathers: list=[]):
        for i in range(len(fathers)):
            self.fathers_relation.append(Relation(fathers[i], 0))
    def get_result(self): return self.result


    def set_result(self, value):self.result = value


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
