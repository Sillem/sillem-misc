from Neuron import Neuron, InputNeuron

class Layer:
    def __init__(self, dimension_of_input, n_nodes=0, hidden = True):
        if hidden:
            self.nodes = [Neuron(dimension_of_input) for _ in range(n_nodes)]
        else:
            self.nodes = [InputNeuron() for _ in range(n_nodes)]
        self.results = [0] * len(self.nodes) ## calculated after forward propagation
    def __getitem__(self, key):
        return self.nodes[key]
    
    def __setitem__(self, key, value):
        self.nodes[key] = value
        
    def __delitem__(self, key):
        del self.nodes[key]
        
    def __len__(self):
        return len(self.nodes)
        
    def get_layer_node_values(self):
        self.results = [node.calculated_value for node in self.nodes]
        return self.results
    
    
if __name__ == '__main__':
    l1 = Layer(3, 2)
    print(l1.results)
    l1.nodes[0].calculate_value([1,2,3])
    l1.nodes[1].calculate_value([1,2,3])
    print(l1.get_layer_node_values())