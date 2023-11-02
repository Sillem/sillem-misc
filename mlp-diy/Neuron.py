from random import uniform

class Neuron:
    def __init__(self, dimension):
        # here dimension + 1, because we will want to have a place for bias
        # it will be at the end of the vector
        self.weights = [uniform(-1, 1) for _ in range(dimension)]
        self.dimension = dimension
        self.delta = 0 #used during backpass
    def backpropagation(cost_function):
        pass
    
    def __str__(self):
        return f"Neuron z {self.dimension}-wymiarowym inputem, z wektorem wag (ostatni jest bias): {self.weights}"
        
        
        
    def calculate_value(self, input, activation_func = False):
        self.previous_layer_input = input
        if len(input) != len(self.weights):
            raise ValueError("Neuron oczekiwał innego wymiaru danych wejściowych.")
        else:
            self.calculated_value = 0
            for component in range(len(input)):
                self.calculated_value += self.weights[component]*input[component]
                
            #here we calculate the bias component to the sum
            
            #self.calculated_value += self.weights[len(self.weights)-1] * 1

            if not activation_func:
                return self.calculated_value 
            else:
                self.calculate_value = activation_func(self.calculated_value)
                return self.calculate_value
class InputNeuron(Neuron):
    def __init__(self,dimension=1):
        self.weights = [1]
        self.dimension=1
        
    def calculate_value(self, input):
        self.calculated_value = input
        return self.calculated_value
        
if __name__ == "__main__":
    n1 = Neuron(3)
    print(n1.calculate_value([1,2,3]))
    
        