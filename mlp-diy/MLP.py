from Layer import Layer
from Neuron import InputNeuron
import tools
class MLP:
    def __init__(self, dim_of_input, dim_of_output, num_of_h_layers=0, num_of_h_layers_nodes=0, learning_rate=0.001):
        #here we build the structure of the network
        self.layers = []
        self.layers.append(Layer(1, dim_of_input, hidden= False)) #we assume we will have a dim_of_input single digit input nodes
        self.learning_rate = learning_rate
        for layer in range(1, num_of_h_layers+1):
            self.layers.append(Layer(dimension_of_input=len(self.layers[layer-1].nodes),
                                n_nodes = num_of_h_layers_nodes))
            
        self.layers.append(Layer(dimension_of_input=len(self.layers[layer-1].nodes),
                           n_nodes=dim_of_output, hidden=True))
        
        # na użytek __str__ zapiszemy wartości z konstruktora
        self.parameters = {'dim_of_input':dim_of_input,
                           'dim_of_output':dim_of_output,
                           'num_of_h_layers':num_of_h_layers,
                           'num_of_h_layers_nodes': num_of_h_layers_nodes,
                           'learning_rate': learning_rate}
        
        
    def forward_propagation(self, global_input, activation_func = False):
        # here we prepare initial layers to boot
        for index, node in enumerate(self.layers[0].nodes):
            node.calculate_value(global_input[index])
        previous_layer_values = self.layers[0].get_layer_node_values()
        # now we start with later layers
        for index, layer in enumerate(self.layers):
            if index==0: continue
            for node in layer.nodes:
                node.calculate_value(previous_layer_values, activation_func)
            #now we move to the next layer so we update the calculated values
            previous_layer_values = layer.get_layer_node_values()
        self.forward_pass_result = previous_layer_values
        
        
    def backward_propagation(self, desired_output):
        network_output = self.forward_pass_result
        print('obecny błąd to', (network_output[0]- desired_output[0])**2)
        ### calculating the deltas
        for n_l in range(len(self.layers))[::-1]:
            for n_n in range(len(self.layers[n_l])):
                if n_l==len(self.layers)-1:
                    self.layers[n_l][n_n].delta = 2 * (desired_output[n_n]-network_output[n_n])
                else:
                    delta = 0
                    for n_next_n in range(len(self.layers[n_l+1])):
                        #for each neuron we look for all neurons in later layer
                        delta += self.layers[n_l+1][n_next_n].weights[n_n] * self.layers[n_l+1][n_next_n].delta
                        #print(self.layers[n_l+1][n_next_n].delta)
                    self.layers[n_l][n_n].delta = delta
                ### updating weights
                for weight in range(len(self.layers[n_l][n_n].weights)):
                    if n_l != 0:
                        self.layers[n_l][n_n].weights[weight] += self.learning_rate * self.layers[n_l][n_n].delta * self.layers[n_l-1][n_n].calculated_value
                

    def single_epoch_training(self, input, output):
        self.forward_propagation(input)
        self.backward_propagation(output)
    def __str__(self):
        response = ''
        response += f"""
              Sieć MLP z następującymi parametrami:
                - przyjmuje {self.parameters['dim_of_input']}-wymiarowe dane wejściowe
                - produkuje {self.parameters['dim_of_output']}-wymiarowe dane wyjściowe
                - posiada {self.parameters['num_of_h_layers']} ukrytych warstw
                - każda ukryta warstwa ma {self.parameters['num_of_h_layers_nodes']} neuronów
                - learning rate wynosi {self.parameters['learning_rate']}
-------------------------------------------------------------------------------------
              """
        structure = 'STRUKTURA:\n'
        for index, layer in enumerate(self.layers):
            layer_info = f"WARSTWA {index+1}\n"
            for node in layer.nodes:
                layer_info+=str(node)+'\n'
                
            structure+=layer_info
                
            
        return response + structure
        
        
        
    
neural_network = MLP(dim_of_input=3, dim_of_output=1, num_of_h_layers=2, num_of_h_layers_nodes=2)

# przyladowy dataset na szybkosci odleglosc od centrum, metraz, pokoje -> cena
dataset = ([1, 30, 4], [200000])
#print(neural_network)
for i in range(1000):
    neural_network.forward_propagation([1,2,3])
    neural_network.backward_propagation([5])