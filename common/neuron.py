class Neuron:
    def __init__(self, fathers: list =[], children: list =[], bias: int=0, activation_funk=lambda x:x):
        self.fathers = fathers
        self.children = children
        self.bias = bias
        self.result = 0
        self.activation_funk = activation_funk

    def add_father(self, fathers=[]): self.fathers.extend(fathers)
    def add_children(self, children=[]): self.children.extend(children)
    def get_result(self): return self.result

    def calculate_result(self):
        suma = self.sumator()
        return self.activation(suma)
    def sumator(self):
        suma = 0
        for i in range(len(self.fathers)):
            suma += self.fathers[i].get_result()
        return suma
    def activation(self, number):
        return self.activation_funk(number)
