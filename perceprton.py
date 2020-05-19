import numpy as np

class Perceptron:  

    def __init__(self, w=None, x=None, p=1):        
        self.weights = []
        self.weights.append(np.array(w))
        self.x = {(1,0,0):0,(1,0,1):0,(1,1,0):1,(1,1,1):0}
        self.x_list = list(self.x.keys())
        self.p = p      
    
    def calculate_y(self, counter):
        y = np.dot(np.array(self.weights[-1]),np.array(self.x_list[counter]))
        return 1 if y > 0 else 0

    def new_weight(self, counter):
        new_w = np.array(self.weights[-1]) + self.p * (self.x.get(self.x_list[counter]) - 
        self.calculate_y(counter)) * np.array(self.x_list[counter])
        self.weights.append(new_w)


    def calculate_weights(self):
        i = 0
        while(len(self.weights) < 10000):            
            if len(self.weights) > 4 and (self.weights[-5] == self.weights[-1]).all():
                break
            self.new_weight(i % 4)
            i += 1

    def print_weights(self):
        self.calculate_weights()
        print('Wagi:')
        for i in range(len(self.weights)):           
            print(i+1,self.weights[i])       

class Perceptron2:
    def __init__(self, w=None, x=None, p=1):        
        self.weights = []
        self.weights.append(np.array(w))
        self.x = {(1,0,0):0,(1,0,1):0,(1,1,0):1,(1,1,1):0}
        self.x_list = list(self.x.keys())
        self.p = p    
      
    def calculate_y(self,counter):
        y = np.dot(np.array(self.weights[-1]),np.array(self.x_list[counter]))
        return 1 if y > 0 else 0

    def calculate_vector(self, counter):
        y = self.calculate_y(counter)
        x = self.x.get(self.x_list[counter])
        vector = np.array(self.x_list[counter])
        if y == 0 and x == 1:
            return vector
        elif y == 1 and x == 0:
            return -1*vector
        else:
            return np.array([0, 0, 0])
    
    def calculate_weights(self):
        i = 0
        while(len(self.weights) < 10000): 
            if len(self.weights) > 4 and (self.weights[-5] == self.weights[-1]).all():
                break              
            c = np.array([0,0,0])        
            for i in range(4):
                c += self.calculate_vector(i)
            new_w = self.weights[-1] + c
            self.weights.append(new_w)

    def print_weights(self):
        self.calculate_weights()
        print('Wagi:')
        for i in range(len(self.weights)):           
            print(i+1,self.weights[i])  


perc1 = Perceptron([1,1,1])
perc1.print_weights()
perc2 = Perceptron([-0.12,0.4,0.65],None,0.1)
perc2.print_weights()

print('Metoda 2')

perc3 = Perceptron2([1,1,1])
perc3.print_weights()

perc4 = Perceptron2([-0.12,0.4,0.65])
perc4.print_weights()

